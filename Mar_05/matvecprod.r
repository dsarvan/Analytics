#!/usr/bin/env Rscript
# File: matvecprod.r
# Name: D.Saravanan
# Date: 16/10/2020
# Script to perform matrix vector product

A <- matrix(c(0.90, 0.07, 0.02, 0.01, 0.00, 0.93, 0.05, 0.02, 0.00, 0.00, 0.85, 0.15, 0.00, 0.00, 0.00, 1.00), 4, 4)
x <- c(0.85, 0.10, 0.05, 0.00)

print(x %*% t(A))
