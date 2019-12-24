## Ch8. ex 2
# (Computer Experiment.) Conduct a simulation to compare the various
# bootstrap confidence interval methods. Let n = 50 and let T(F) =
# integral{(x-mu)^3 dF(x)} / sigma^3 be the skewness. Draw Y1 , ... , Yn ~ N(0,l) and
# set Xi = exp(Yi), i = 1, ... , n. Construct the three types of bootstrap 95
# percent intervals for T(F) from the data Xl,...,Xn . Repeat this whole
# thing many times and estimate the true coverage of the three intervals.

library(tidyverse)
n <- 50 # number of samples
N <- 100  # number of iterations
B <- 1000
alpha <- 0.05
za <- abs(qnorm(alpha/2,0,1))
ci_norm <- c()
ci_q <- c()

sk <- function(x){
  ss_x <- (1/n) * sum((x - mean(x))^3)
  sig_hat <- sqrt( (1/n) * ( (x - mean(x)) %*% (x-mean(x)) ) )
  skewness <- ss_x / sig_hat^3
  return(skewness)
}

for (i in 1: N){
  y <- rnorm(n, 0,1)
  x <- exp(y)
  sk_hat <- sk(x)
  
  Tboot <- c()
  for (i in 1:B){
    xstar <- sample(x,n, repl=TRUE)
    Tboot[i] <- sk(xstar)
  }
  se_boot <- sqrt(var(Tboot)) # (B-1)/B -> 1 as B gets large
  
  ci_norm <- rbind(ci_norm, c(sk_hat - za * se_boot, sk_hat + za*se_boot))
  ci_q <- rbind(ci_q, quantile(Tboot, probs=c(.025, .975)))
}

c(mean(ci_norm[,1]), mean(ci_norm[,2]))  # normal C.I.
c(mean(ci_q[,1]), mean(ci_q[,2]))   # quantile C.I.