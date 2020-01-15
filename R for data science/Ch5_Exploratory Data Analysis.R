library(ggplot2)
library(tidyverse)
library(nycflights13)
library(Lahman)
library(modelr)
windows()
## Explanatory Data Analysis (EDA)
# This is an iterative cycle.
# 1. Generate questions about your data
# 2. Search for answers by visualizing, transforming, and modeling your data
# 3. Use what you learn to refine your questions and/or generate new questions
# usually consists of visualization, transformation, and modeling of data
# it is important to make quaility questions, by making quantity of questions.
# those two types of questions will always be useful for making discoveries within the data
# 1. what type of variation occurs within my variables?
# 2. what type of covariation occurs between my variables?

## variation
# tendency of the values of a variable to change from measurement to measurement.

## visualizing distributions
ggplot(data = diamonds)+
  geom_bar(mapping = aes(x = cut)) # the y-axis indicates how many observations occured
diamonds %>%
  count(cut)

ggplot(data = diamonds) +
  geom_histogram(mapping = aes(x = carat), binwidth = 0.5)
diamonds %>%
  count(cut_width(carat, 0.5))

smaller <- diamonds %>%
  filter(carat < 3)
ggplot(data = smaller, mapping = aes(x = carat))+
  geom_histogram(binwidth = 0.1)

ggplot(data = smaller, mapping = aes(x = carat, colour = cut)) +
  geom_freqpoly(binwidth = 0.1)

## Typical values
# which values are the most common/rare? why? does that match your expectation?
# can you see any unusual patterns? what might explain them?
ggplot(data = smaller, mapping = aes(x = carat)) +
  geom_histogram(binwidth = 0.01)
# this histogram suggests several interesting questions:
# why are there more diamonds at whole carats and common fractions of carats?
# why are there more diamonds slightly to the right of each peak than there are slightly 
# to the left of each peak?
# why are there no diamonds bigger than 3 carats?

## in general, clusters of similar values suggest that subgroups exist in the data
# to understant the subgroups, ask:
# how are the observations within each cluster similar to each other?
# how are the observations in separate clusters different from each other?
# how can you expalin or describe the clusters?
# why might the appearance of clusters be misleading?

ggplot(data = faithful, mapping = aes(x = eruptions)) + # eruptions= minutes of eruptions
  geom_histogram(binwidth = 0.25)
view(faithful)
# this shows that the eruption times appear to be clustered into two groups:
# short eruptions(around 2 mins), long eruptions(around 4-5 mins)

## unusual values - outliers
ggplot(diamonds) +
  geom_histogram(mapping = aes(x = y), binwidth =  0.5)
# unusually wide limits on the x-axis indicates that there are rare observations
ggplot(diamonds) +
  geom_histogram(mapping = aes(x= y), binwidth = 0.5)+
  coord_cartesian(ylim = c(0, 50)) # sets limitation to the y-axis to make rare observations visible
unusual <- diamonds %>%
  filter(y <3 | y > 20) %>%
  arrange(y)
view(unusual)
# now we can see that there are observations that appear to be wrong:
# ones with width of 0 mm, and 32mm, 59mm that don't cost much
# it is good to remove the outliers if they don't affect the result and cannot figure out why they are there.
# but if they have a substential effect on the result, you should not drop them without justification
# should figure out why they are there and what caused them, and disclose that you removed them

## missing values
# when encountered unusual values, there are two choices:
# drop the row entirely, 
diamonds2 <- diamonds %>%
  filter(between(y, 3, 20))
# or replace the unusual values with missing values. 
# this is recommended because just because one measurement is invalid, doesn't mean all the measurements are.
diamonds2 <- diamonds %>%
  mutate(y = ifelse(y< 3 | y >20, NA, y))
ggplot(data = diamonds2, mapping = aes(x = x, y = y))+
  geom_point() # if na.rm = TRUE is not stated, it will show a warning message with number of NAs

ggplot(data = diamonds2, mapping = aes(x = y))+
  geom_histogram() # histogram removes the missing values automatically

ggplot(data = diamonds2, mapping = aes(x = y))+
  geom_bar() # bar also removes the missing values

## in the flights data, missing values in dep_time indicates that the flight was cancelled.
# so might want to compare the scheduled departure times for cancelled and non-cancelled times.
flights2 <- nycflights13::flights %>%
  mutate(
    cancelled = is.na(dep_time),
    sched_hour = sched_dep_time %/% 100,
    sched_min = sched_dep_time %% 100,
    sched_dep_time = sched_hour + sched_min / 60
  )

ggplot(data = flights2, mapping = aes(sched_dep_time)) +
  geom_freqpoly(
    mapping = aes(colour = cancelled),
    binwidth = 1/4
  )
# however, this plot doesn't really help since there are too many non-cancelled flights.

## covariation
# variation describes the behaviour 'within' a variable,
# covariation describes the behaviour 'between' variables.
# the best way to describe covariation is by visualizing the relationship between variables.
# for price vs. quality,
ggplot(data = diamonds, mapping = aes(x = price)) +
  geom_freqpoly(mapping = aes(colour = cut), binwidth = 500)
ggplot(diamonds)+
  geom_bar(mapping = aes(x = cut))
# the ones above are hard to see the difference in distribution

ggplot(
  data = diamonds,
  mapping = aes(x = price, y = ..density..)
) +
  geom_freqpoly(mapping = aes(colour = cut), binwidth = 500)

# boxplot
ggplot(data = diamonds, mapping = aes(x = cut, y = price)) +
  geom_boxplot()

ggplot(data = mpg) + 
  geom_boxplot(mapping = aes(x = reorder(class, hwy, FUN = median),
                                 y = hwy)) # this reorders variables on x-axis according to median
ggplot(data = mpg) + 
  geom_boxplot(mapping = aes(x = reorder(class, hwy, FUN = median),
                             y = hwy))+
  coord_flip()

ggplot(data = flights2, mapping = aes(x = cancelled, y = sched_dep_time, colour = cancelled))+
  geom_boxplot(position = "dodge")+
  coord_flip()

## two categorical variables
ggplot(data = diamonds) +
  geom_count(mapping = aes(x = cut, y = color))
diamonds %>%
  count(color, cut) %>%
  ggplot(mapping = aes(x = color, y = cut))+
  geom_tile(mapping = aes(fill = n))

## two continuous variables
ggplot(data = smaller) +
  geom_hex(mapping = aes(x = carat, y = price))
ggplot(data = smaller, mapping = aes(x = carat, y = price)) +
  geom_boxplot(mapping = aes(group = cut_number(carat, 20)))

ggplot(data = diamonds) +
  geom_point(mapping = aes(x = x, y = y)) +
  coord_cartesian(xlim = c(4,11), ylim = c(4,11))

## patterns and models
ggplot(data = faithful) +
  geom_point(mapping = aes(x = eruptions, y = waiting))

mod <- lm(log(price) ~ log(carat), data= diamonds)
diamonds2 <- diamonds %>%
  add_residuals(mod) %>% # resid= view of the price of the diamonds once the effect of carat has been removed
  mutate(resid = exp(resid))
ggplot(data = diamonds2) +
  geom_point(mapping = aes(x = carat, y = resid))

ggplot(data = diamonds2) +
  geom_boxplot(mapping = aes(x= cut, y= resid))
