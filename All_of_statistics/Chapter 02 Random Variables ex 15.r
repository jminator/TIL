## Chapter 2 ex 15
# (A universal random number generator.) Let X have a continuous, strictly
# increasing CDF F. Let Y = F(X). Find the density of Y. This is called
# the probability integral transform. Now let U rv Uniform(O,l) and let
# X = F-I(U). Show that X rv F. Now write a program that takes
# Uniform (0,1) random variables and generates random variables from
# an Exponential (,6) distribution.

library(tidyverse)

ran_exp <- function(n, beta) {
  U <- runif(n = n, min = 0, max = 1)
  E <- 1/beta * exp(-1/beta * U)
  return(E)
}

A2_ex15 <- function(){
  n15 <- 10
  beta <- 1/10
  ran_exp(n15, beta)
}

A2_ex15()