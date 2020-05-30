library(tidyverse)
library(ggplot2)
windows()

table1 # this one is the only tidy data
table2
table3
table4a
table4b

# example of using the data = table1
table1 %>%
  mutate(rate = cases / population * 10000) %>%
  count(year, wt = cases) %>%
  
ggplot(data = table1, mapping = aes(year, cases)) +
  geom_line(mapping = aes(group = country), colour = "grey50") +
  geom_point(mapping = aes(colour = country))


## example of using the data = table2
table2
# number of TB cases per country per year
(table2a <- filter(table2, type == "cases"))
(table2b <- filter(table2, type == "population"))
(table2c <- select(table2a, country, year))
table2c %>%
  mutate(cases = table2a$count) %>%
  mutate(population = table2b$count) %>%
  mutate(rate = cases / population * 10000) %>%
  {. ->> table2c } # saving the table
table2c
ggplot(data = table2c, mapping = aes(year, cases)) +
  geom_line(mapping = aes(group = country), colour = "grey50") +
  geom_point(mapping = aes(colour = country))

## spreading and gathering
# gathering
table4a # 1999 and 2000 should be values, not names of variables. need to gather those columns
(tidy4a<- table4a %>%
  gather("1999", "2000", key = "year", value = "cases"))

table4b
(tidy4b<- table4b %>%
    gather("1999", "2000", key = "year", value = "population"))

left_join(tidy4a, tidy4b)

# spreading
table2 # cases and population should be variables, not values
(spread(table2, key = type, value = count))

# separating and pull
table3
table3 %>%
  separate(col = rate, into = c("cases", "population"), sep = "/", convert = TRUE)
args(separate)
table3 %>%
  separate(col = year, into = c("century", "year"), sep= 2) %>%
  separate(col = rate, into = c("cases", "population"), sep = "/", convert = TRUE)
# unite