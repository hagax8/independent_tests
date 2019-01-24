# Independent tests
Some scripts to compute the number of independent tests.

## 1. Compute the number of independent tests from a correlation matrix using PCA

### Run script
```
python run_independent.py your_correlation_matrix_file
```
your_correlation_matrix_file must be a file containing a squared correlation matrix in csv format with no header.

### Requirements
1. Download navigome_independent_tests.py and run_independent.py and put them in the same directory
2. Import sklearn and numpy:
```
pip install sklearn
pip install numpy
```

### Example output
```
Internal dimension of kernel matrix (N): 161
Number of individual tests ((N*N-N)/2): 12880
Bonferroni cut-off: 3.88e-06
```




