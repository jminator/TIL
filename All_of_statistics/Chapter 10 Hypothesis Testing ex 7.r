## Chapter 10 ex 7
# In 1861, 10 essays appeared in the New Orleans Daily Crescent. They
# were signed "Quintus Curtius Snodgrass" and some people suspected
# they were actually written by Mark Twain. To investigate this, we will
# consider the proportion of three letter words found in an author's work.
# From eight Twain essays we have:
# .225 .262 .217 .240 .230 .229 .235 .217
# From 10 Snodgrass essays we have:
# .209 .205 .196 .210 .202 .207 .224 .223 .220 .201

# (a) Perform a Wald test for equality of the means. Use the nonparametric
# plug-in estimator. Report the p-value and a 95 per cent confidence
# interval for the difference of means. What do you conclude?
library(tidyverse)
x <- c(.225,.262,.217,.240,.230,.229,.235,.217)
y <- c(.209, .205, .196, .210, .202, .207, .224, .223, .220, .201)

se1 <- (mean(x) * (1-mean(x))) / length(x)
se2 <- (mean(y) * (1-mean(y))) / length(y)
se <- sqrt(se1 + se2)

t_obs <- mean(x) - mean(y)
W <- t_obs / se
(p_value <- 2 * pnorm(-W, 0, 1)) # p-value

alpha <- 0.05
z_value <- qnorm(1-alpha/2,0,1)
(CI_95 <- c(t_obs - z_value*se, t_obs+z_value*se)) # confidence interval
# The p-value shows a very weak evidence against H0 and the confidence interval includes zero.  
# Therefore, cannot reject H0


# (b) Now use a permutation test to avoid the use oflarge sample methods.
# What is your conclusion? (Brinegar (1963)).
data <- c(x, y)
N <- length(data)
B <- 10000
I <- 0
t_perm <- c()

for (i in 1:B){
  perm <- sample(data, size= N, repl=FALSE)
  t_perm[i] <- mean(perm[1:length(x)]) - mean(perm[(length(x)+1):N])
  if( t_perm[i] > t_obs ){
    I <- I + 1 
  }
}
(p_value <- I / B )
# The p-value shows a very strong evidence against H0. Therefore, reject H0