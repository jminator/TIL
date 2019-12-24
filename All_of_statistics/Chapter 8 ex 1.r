## Chapter 8 ex 1
# Consider the data in Example 8.6. Find the plug-in estimate of the
# correlation coefficient. Estimate the standard error using the bootstrap.
# Find a 95 percent confidence interval using the Normal, pivotal, and
# percentile methods.

library(tidyverse)
y <- c(576,635,558,578,666,580,555,661,651,605,653,575,545,572,594)
z <- c(3.39,3.30,2.81,3.03,3.44,3.07,3.00,3.43,3.36,3.13,3.12,2.74,2.76,2.88,3.96)
n <- length(y)
alpha <- 0.05
za <- abs(qnorm(alpha/2,0,1))
table <- cbind(y, z)
rho_hat <- cor(table)[1,2]

# Bootstrap
B <- 10000
Tboot <- c() # creates a vector of zeros
for (i in 1:B)
{
  index <- sample(1:n, size = n, repl = T)
  b_sample <- table[index,]
  Tboot[i] <- cor(b_sample)[1,2]
}
(se = sqrt(((B-1)/B)*var(Tboot)))

(normal_ci <- c((rho_hat - za * se), min(1,rho_hat + za * se)))
(pivotal_ci <- c(2*rho_hat - quantile(Tboot, probs=0.975), 
                 2*rho_hat - quantile(Tboot, probs=0.025)))
(q_ci <- (quantile(Tboot, probs=c(.025, .975))))