library(tidyverse)
## tibbles are data frames with some older behaviour
iris
class(iris) ## gives us data.frame
iris2 <- tibble(iris)
class(iris2)
iris2

# tibble vs. data.frame
# tibbles only shows 10 rows
tb<- tibble(
  a = lubridate::now() + runif(1e3) * 86400,
  b = lubridate::today() + runif(1e3) * 30,
  c = 1:1e3,
  d = runif(1e3),
  e = sample(letters, 1e3, replace = TRUE)
)

## subsetting
# if you want to pull out a single variable, $ and [[ can be used
# $ only extracts by name, [[ extracts by name or position
df <- tibble(
  x = runif(5),
  y = rnorm(5)
)
df
# extract by name
df$x
df[["x"]]
# extract by pposition
df[[0]] # error. R starts with 1
df[[1]]
df[[2]]
# to use pipe
df %>% .$x
