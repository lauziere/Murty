## Python3 implementation of Murty's algorithm \[1\]

## Introduction

This repository is a Python3 rewrite of an R implementation of Murty's algorithm \[3\]. NumPy and SciPy are the only dependencies. 

The R implementation allows a choice of minimization vs maximization of the objective and allows for the linear program to be solver by either the Hungarian algorithm or as a general linear program. Both extensions will be added to this repository; however, it currently only supports minimization via Jonker-Volgenant algorithm. 

This Jonker-Volgenant algorithm is provided by Scipy: scipy.optimize.linear_sum_assignment

Murty's algorithm yields the top *K* solutions to a size *n* assignment problem. See [2] for an introduction to assignment problems. This implementation requires a square (*n*x*n*) matrix. 

## Use

The function 'getkBestNoRankHung(matNR, k_bestNR)' takes in as input the *n*x*n* matrix 'matNR' and a positive integer *K*: 'k_bestNR' specifying the number of desired solutions. The function returns two numpy arrays: 'all_solutions' and 'all_objectives'. 'all_solutions' is of size '(k_bestNR, n, n)' and 'all_objectives' is size 'n'. The solutions are permutation matrices matching row indices to columns. 

## Future work

1. Add SciPy linear program solver as an option.
2. Allow for maximization as well as minimization.
3. Benchmarks
4. Upload to PyPi

## References

\[1\] Murty, K. (1968). An Algorithm for Ranking all the Assignments in
Order of Increasing Cost. *Operations Research, 16*(3), 682-687.
Retrieved from <http://www.jstor.org/stable/168595>

\[2\] Burkard, R., Dell’Amico, M., Martello, S. (2009). *Assignment
Problems*. Philadelphia, PA: Society for Industrial and Applied
Mathematics, 160-61.

\[3\] https://github.com/arg0naut91/muRty
