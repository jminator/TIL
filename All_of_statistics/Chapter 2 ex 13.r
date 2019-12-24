# Chapter 2 ex 13
# Generate a vector x = (Xl, ... ,XlO,OOO) consisting
# of 10,000 random standard Normals. Let Y = (YI,"" YIO,OOO)
# where Yi = eX;. Draw a histogram of Y and compare it to the PDF you
# found in part (a).

library(tidyverse)

pdf_y <- function(Y) {
  pY <-  (1/Y) * (1/sqrt(2*pi)) * exp((-(log(Y))^2) / 2)
  return(pY)
}
curve(expr = pdf_y, from = 0, to = 5, xname = "Y")

hist_Y <- function(){
  n <- 10000
  X <- rnorm(n, 0, 1)
  eY <- exp(X)
  data <- data.frame(x = X, exp_Y = eY)
  hist(x = data$exp_Y, breaks = 100)
}
hist_Y()