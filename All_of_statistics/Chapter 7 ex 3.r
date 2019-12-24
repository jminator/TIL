## Ch7. ex 3

# (Computer Experiment.) Generate 100 observations from a N(O,l) distribution.
# Compute a 95 percent confidence band for the CDF F (as
# described in the appendix). Repeat this 1000 times and see how often
# the confidence band contains the true distribution function. Repeat using
# data from a Cauchy distribution.

library(tidyverse)

## Initial Values
n = 100 # number of samples
alpha = 0.05
F_hat <- seq(0.01:1, by = 1/n)
se <- sqrt( (1/(2*n)) * log(2/alpha))
upper <- pmin(1, F_hat + se)
lower <- pmax(0, F_hat - se)
N = 1000 # number of iterations

## Normal
norm_total <- 0
for (i in 1:N){
  n_x <- sort(rnorm(n = n, mean = 0, sd = 1), decreasing = FALSE) # Normal samples
  Fn_values <- pnorm(n_x, mean = 0, sd = 1) # F(n_x)
  if (any(upper - Fn_values < 0) || any(lower - Fn_values > 0)){
    norm_total <- norm_total +1
  }
}
graphs <- function(x, F_values) {
  data = data.frame(x, F_hat, upper, lower, F_values)
  ggplot(data = data, aes(x = x)) +
    geom_point(aes(y = F_hat)) +
    geom_line(aes(y = upper), colour = 'RED') +
    geom_line(aes(y = lower), colour = 'BLUE') +
    geom_line(aes(y = F_values), colour = 'GREEN')+
    ylim(0,1)
}

norm_total
graphs(x = n_x, F_values = Fn_values)

## Cauchy
cauchy_total <- 0
for (i in 1:N){
  c_x <- sort(rcauchy(n = n), decreasing = FALSE) # Cauchy samples
  Fc_values <- pcauchy(c_x) # F(c_x)
  if (any(upper - Fc_values < 0) || any(lower - Fc_values > 0)){
    cauchy_total <- cauchy_total + 1
  }
}
graphs <- function(x, F_values) {
  data = data.frame(x, F_hat, upper, lower, F_values)
  ggplot(data = data, aes(x = x)) +
    geom_point(aes(y = F_hat)) +
    geom_line(aes(y = upper), colour = 'RED') +
    geom_line(aes(y = lower), colour = 'BLUE') +
    geom_line(aes(y = F_values), colour = 'GREEN')+
    ylim(0,1)
}
cauchy_total
graphs(x = c_x, F_values = Fc_values)