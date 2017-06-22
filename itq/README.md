## Summarizing the PCA approach
Listed below are the 6 general steps for performing a principal component analysis, which we will investigate in the following sections.

1. Take the whole dataset consisting of ***d***-dimensional samples ignoring the class labels
2. Compute the ***d***-dimensional mean vector (i.e., the means for every dimension of the whole dataset)
3. Compute the covariance matrix (alternatively, the covariance matrix) of the whole data set
4. Compute eigenvectors (**e**<sub>1</sub>,**e**<sub>2</sub>,...,**e**<sub>*d*</sub>) and corresponding eigenvalues (**λ**<sub>1</sub>,**λ**<sub>2</sub>,...,**λ**<sub>*d*</sub>)
5. Sort the eigenvectors by decreasing eigenvalues and choose ***k*** eigenvectors with the largest eigenvalues to form a d×k dimensional matrix **W** (where every column represents an eigenvector)
6. Use this ***d×k*** eigenvector matrix to transform the samples onto the new subspace. This can be summarized by the mathematical equation: **y=W<sup>*T*</sup> × x** (where x is a ***d×1***-dimensional vector representing one sample, and ***y*** is the transformed ***k×1***-dimensional sample in the new subspace.)

### Reference
* [Implementing a Principal Component Analysis](http://sebastianraschka.com/Articles/2014_pca_step_by_step.html)
* [The mathematical principles of PCA](http://dataunion.org/13702.html)

## Summarizing the ITQ approach
1.  Dimensionality Reduction : **PCA|CCA**
2.  Binary Quantization
    + A. initialization ***R*** (c*c matrix) as a random orthogonal matrix
    + B. Fix ***R*** and update ***B*** (n*c matrix)
    + C. Fix ***B*** and update ***R***
    + D. Judge iterations finish, return to step B if no

### Reference
* [Iterative Quantization: A Procrustean Approach to Learning Binary Codes](http://www.cs.unc.edu/~lazebnik/publications/cvpr11_small_code.pdf)

### Dependencies
* *Numpy 1.9.2* Library in Python

## Large Data Solution
* PCA: Block and split the data set _n*c matrix_ by columns into several file, such as _n*10 matrix_, which stores several whole columns of the data set. And calculate each block of the __covariance matrix__ and embed them back to the blank of original big _n*c matrix_. Finaly write the _c*c covariance matrix_ to disk.
* ITQ: Limited by the memory, we can't put all the matrix into memory for calculating the R matrix. Instead, we use the part of dataset randomly selected to calculate result though it may influence the effect.
* After testing in the MIH module following, we found that PCA process will highly reduce the information in original double codes. It better performs using only ITQ completing the transformation.
