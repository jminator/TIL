cp <- function(true_p, ci_lower, ci_upper){
  
  ci <- cbind(ci_lower, ci_upper)
  prob_list = c()
  
  for (j in 1:length(true_p)){
    prob <- 0
    bin_probs <- dbinom(seq(0,n,by=1), n, true_p[j])
    for (i in 1:(n+1)){
      if (ci[i,1] < true_p[j] & true_p[j] <= ci[i,2]){
        prob <- prob + bin_probs[i]
      }
    }
    prob_list <- c(prob_list, prob)
  }
  return(prob_list)
}
n = 100
q = qnorm(0.025) # -1.96
p_hat = (0:n)/n
true_p = as.vector(seq(0,1,by=0.001))

## Wald CI
wald_ci_upper = p_hat + (-q) * sqrt(p_hat * (1-p_hat) / n)
wald_ci_lower = p_hat - (-q) * sqrt(p_hat * (1-p_hat) / n)
wald_cp <- cp(true_p, wald_ci_lower, wald_ci_upper)

## Agresti-Coull
y = c(0:100)
cs = q^2
p_tilda = (y + cs / 2) / (n + cs)
n_tilda = n + cs

ac_upper = p_tilda + 1.96 * sqrt(p_tilda * (1-p_tilda) / n_tilda)
ac_lower = p_tilda - 1.96 * sqrt(p_tilda * (1-p_tilda) / n_tilda)
ac_cp = cp(true_p, ac_lower, ac_upper)

## Continuity Corrected
cc_upper = p_hat + (-q) * sqrt(p_hat * (1-p_hat) / n) + (1/(2*n))
cc_lower = p_hat - (-q) * sqrt(p_hat * (1-p_hat) / n) - (1/(2*n))
cc_cp = cp(true_p, cc_lower, cc_upper)


windows()
par(mfrow = c(2,2))
plot(true_p, wald_cp, type="l", main="Wald CI"); abline(a=0.95, b=0)
plot(true_p, ac_cp, type='l', main="Agresti-Coull CI"); abline(a=0.95, b=0)
plot(true_p, cc_cp, type='l', main="Continuity-corrected CI"); abline(a=0.95, b=0)