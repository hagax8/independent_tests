# Independent tests
Some scripts to compute the number of independent tests.

## 1. Compute the number of independent tests from a correlation matrix using PCA

This defines N, the internal dimension of the kernel (correlation matrix), as the number of principal components accounting for 99.5% of the variance explained. The number of individual tests T is then (N*N-N)/2, and the Bonferroni cut-off 0.05/T. The default strategy to handle missing values is to replace them by the median (imp = SimpleImputer(strategy='median')) - you can change this behaviour in navigome_independent_tests.py.

### Run script
```
python run_independent.py your_correlation_matrix_file
```
your_correlation_matrix_file must be a file containing a squared correlation matrix in csv format with no header.

### Requirements
1. Download navigome_independent_tests.py and run_independent.py and put them in the same directory
2. If not already done, install sklearn and numpy (scikit-learn has to be at least v0.20)
```
pip install scikit-learn==0.20
pip install numpy
```

### Example output
```
Internal dimension of kernel matrix (N): 161
Number of individual tests ((N*N-N)/2): 12880
Bonferroni cut-off: 3.88e-06
```




