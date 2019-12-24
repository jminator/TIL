## Chapter 11 ex 4
# Suppose that 50 people are given a placebo and 50 are given a new treatment. 
# 30 placebo patients show improvement while 40 treated patients
# show improvement. Let tau = P2 - P1 where P2 is the probability of
# improving under treatment and P1 is the probability of improving under placebo.

# (b) Find the standard error and 90 percent confidence interval using the
# parametric bootstrap.
tau_mle <- 1/5
z_90 <- qnorm(1-.1/2)
n <- 50

x <- rbinom(B, 50, 3/5) / 50
y <- rbinom(B, 50, 4/5) / 50

pair <- cbind(x,y)
index <- sample(1:B, size=B, repl=TRUE)
b_sample <- pair[index,]
Tboot <- b_sample[,2] - b_sample[,1]
(se <- sd(Tboot))
(CI_b <- c(tau_mle-z_90*se, tau_mle+z_90*se))


# (c) Use the prior f(P1, P2) = 1. Use simulation to find the posterior mean 
# and posterior 90 percent interval for tau.
x_placebo <- 30
x_treat <- 40
placebo_b <- rbeta(B, x_placebo+1, n-x_placebo+1)
treat_b <- rbeta(B, x_treat+1, n-x_treat+1)

tau <- treat_b - placebo_b
(mean(tau))
se <- sd(tau)
(CI_b <- c(tau_mle-z_90*se, tau_mle+z_90*se))


# (e) Use simulation to find the posterior mean and posterior 90 percent interval for psi.
n <- 50
p1 <- rbeta(B, x_placebo+1, n-x_placebo+1)
p2 <- rbeta(B, x_treat+1, n-x_treat+1)
psi <- log((p1 / (1-p1)) / (p2 / (1-p2)))
mean(psi)
post_i <- quantile(psi, prob=c(0.05, 0.95))
hist(psi)