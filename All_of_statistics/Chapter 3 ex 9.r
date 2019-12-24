## Chapter 3 ex9
# (Computer Experiment.) Let Xl, X 2 , ... , Xn be N(O, 1) random variables
# and let Xn = n-IL~=IXi' Plot Xn versus n for n = 1, ... ,10,000.
# Repeat for Xl, X 2 , .. . , Xn rv Cauchy. Explain why there is such a difference.
# library(tidyverse)

norm_x <- function(){
  x_val <- rnorm(n = n, mean = 0, sd = 1)
  x_mean <- c()
  for (i in 1:n){
    x_mean <- c(x_mean, sum(x_val[1:i] / i))
  }
  return(x_mean)
}

cauchy_x <- function(){
  x_val <- rcauchy(n = n)
  x_mean <- c()
  for (i in 1:n){
    x_mean <- c(x_mean, sum(x_val[1:i] / i))
  }
  return(x_mean)
}

n <- 10000
x_axis <- c(1:n)
norm_mean <- norm_x()
cauchy_mean <- cauchy_x()

## X ~ Normal
plot(x = x_axis, y = norm_mean)

## X ~ Cauchy
plot(x = x_axis, y= cauchy_mean)
# Cauchy plot shows a number of jumps since the distribution concerns location and scale only. 
# It doesn't take mean, variance, or higher moments into account.