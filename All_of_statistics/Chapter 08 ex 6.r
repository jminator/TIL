## Chapter 8 ex 6
# (Computer Experiment.) Let Xl,...,Xn Normal(mu, 1). Let theta = exp(mu) and let theta_hat = exp(X_bar). 
# Create a data set (using mu = 5) consisting of n=100 observations.
# (a) Use the bootstrap to get the se and 95 percent CI for theta.
# (b) Plot a histogram of the bootstrap replications. This is an estimate
# of the distribution of theta_hat. Compare this to the true sampling distribution of theta_hat.

library(tidyverse)
n <- 100
mu <- 5
x <- rnorm(n, mu,1)
theta_hat <- exp(mean(x))
za <- abs(qnorm(0.05/2, 0,1))

# (a) bootstrap to get theta_star
B <- 1000
Tboot <- c()
for (i in 1:B){
  x_star <- sample(x, size=n, repl=TRUE)
  Tboot[i] <- exp(mean(x_star))
}
(se <- sqrt(var(Tboot)))
(norm_ci <- t(c(theta_hat - za*se, theta_hat + za*se)))

# (b) histogram
hist(Tboot, freq=FALSE, xlab="", ylab="", xlim=c(100, 240), ylim=c(0,0.03),  
     main="Comparison between bootstrap and true distribution")
par(new=TRUE)
plot(seq(from = 100, to = 240, by = 1), xlim=c(100, 240), ylim=c(0,0.03), 
     dlnorm(seq(from = 100, to = 240, by = 1),5,0.1), type="l", xlab="", 
     ylab="", main=NULL)