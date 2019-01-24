from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import numpy as np
from sys import argv

def internal_dimension(data,percentage=0.995):
        pca = PCA(random_state=42, n_components=percentage)
        data = pca.fit_transform(data)
        return(pca.n_components_)

def bonferroni_cutoff(filename):
    data = np.genfromtxt(filename, delimiter=",", dtype=np.float64)
    imp = SimpleImputer(strategy='median')
    data = imp.fit_transform(data)
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    ndims = internal_dimension(data)
    indep_tests = (ndims*ndims-ndims)/2
    indep_tests_pvalue = 0.05/indep_tests
    print("Internal dimension of kernel matrix (N): %s" % (ndims))
    print("Number of individual tests ((N*N-N)/2): %s" % (indep_tests))
    print("Bonferroni cut-off: %.2e" % (indep_tests_pvalue))
    return(indep_tests_pvalue)


def main():
    indep = bonferroni_cutoff(argv[1])

if __name__ == "__main__":
    main()
