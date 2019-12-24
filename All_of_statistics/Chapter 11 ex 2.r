## Chapter 11 ex 2
# Let Xl, ... , Xn rv Normal(mu, 1).

# (a) Simulate a data set (using mu = 5) consisting of n=l00 observations.
# (b) Take f(mu) = 1 and find the posterior density. Plot the density.
library(tidyverse)
n <- 100
x <- rnorm(n,mean=5,1)
post <- function(mu_values){
  (((1/sqrt(2*pi))^n) * exp(-sum(((x - mu_values)^2)/2)))
}
mu <- seq(from=4, to=6, by = 0.01)
plot(mu, lapply(mu, post), type="l")

# (c) Simulate 1,000 draws from the posterior. Plot a histogram of the
# simulated values and compare the histogram to the answer in (b).
B <- 1000
post_d <- lapply(mu, post)
p_samples <- sample(mu, size = B, replace=TRUE, prob = as.numeric(post_d))

plot(mu, lapply(mu, post), type="l", main="comparison between (b) and (c)", 
     xlab="", ylab="", yaxt = 'n' )
par(new=TRUE)
hist(p_samples, xlim=c(4,6), freq=FALSE, xlab="", ylab="", main=NULL, yaxt = 'n' )
# The plots look very similar

# (d) Let theta = exp(mu). Find the posterior density for theta analytically and by simulation.
theta <- exp(p_samples)
hist(theta)

# (e) Find a 95 percent posterior interval for mu.
(post_i <- quantile(mu, prob=c(0.025,0.975) ))

# (f) Find a 95 percent confidence interval for theta.
z <- qnorm(1-.025, 0, 1)
mean_theta <- mean(theta)
se <- sqrt(var(theta))
(ci <- c(mean_theta - z*se, mean_theta + z*se))