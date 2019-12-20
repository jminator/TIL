library(tidyverse)

FlipCoin <- function(n) {
  p <- 0.03
  k <- 0
  proportion <- c()
  
  for (i in 1:n){
    k <- k + sum(sample(c("H","T"), size = 1, replace = TRUE, prob = c(p, 1-p)) == "H")
    proportion <- c(proportion, k / i)
  }
  return(proportion)
}

main <- function(){
  n <- 1000
  df <- data.frame(proportion <- FlipCoin(n), trials <- (1:n))
  head(df)
  
  windows()
  ggplot(data = df, aes(x = trials, y = proportion))+
    scale_y_continuous(breaks = c(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), limits=c(0,1))+
    geom_line(colour = "Blue")
}

main()