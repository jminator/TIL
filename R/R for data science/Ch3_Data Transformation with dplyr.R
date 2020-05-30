install.packages("nycflights13")
library(nycflights13)
library(tidyverse)

flights
view(flights) ## shows the data in a separate window

jan1 <- filter(flights, month ==1, day ==1)
(dec25<- filter(flights, month == 12, day == 25))
filter(flights, month == 1 | month == 12) ## | means 'or'
filter(flights, !(arr_delay > 120 | dep_delay > 120))
filter(flights, arr_delay <= 120, dep_delay <= 120) ## they mean the same thing

## dealing with missing values
## filter() automatically excludes both false and NA. to include them,
df <- tibble(x = c(1, NA, 3))
df
filter(df, x > 1)

## had and arrival delay of two or more hours
filter(flights, (arr_delay >= 120))
## flew to houstom (IAH or HOU)
filter(flights, dest == "IAH" | dest == "HOU")

## Arrange the rows
arrange(flights, year, month, day)
arrange(flights, desc(arr_delay)) ## missing values are sorted at the end

## to bring the missing values to the start:
arrange(flights, desc(is.na(dep_time)))

## select columns:
select(flights, year, month, day)
select(flights, year:day)
select(flights, -(year:day))
select(flights, origin, starts_with("U"))

## add columns:
(flights_sml <- select(flights, 
                      year:day,
                      ends_with("delay"), ## select variables that has delay at ends
                      distance,
                      air_time
                      ))
(mutate(flights_sml,
       gain = arr_delay - dep_delay,
       speed = distance / air_time * 60,
       gain_per_hour = gain / hours))

transmute(flights, ## transmute only keeps the new variables
          gain = arr_delay - dep_delay,
          hours = air_time / 60,
          gain_per_hour = gain / hours
          )

transmute(flights, 
          dep_time,
          hour = dep_time %/% 100, ## integer division
          minute = dep_time %% 100) ## remainder

## grouped summaries:
summarize(flights, delay = mean(dep_delay, na.rm = TRUE)) ## collapses a dataframe to a single row

(by_day <- group_by(flights, year, month, day))
summarize(by_day, delay = mean(dep_delay, na.rm = TRUE))
## summarize is usually used with group_by()

## relationship between the distance vs. average delay for each location
by_dest <- group_by(flights, dest)
(delay <- summarize(by_dest,
                   count = n(),
                   dist = mean(distance, na.rm = TRUE),
                   delay = mean(arr_delay, na.rm = TRUE)
                   ))
(delay <- filter(delay, count > 20, dest != "HNL"))
ggplot(data = delay, mapping = aes(x = dist, y = delay)) +
  geom_point(aes(size = count), alpha = 1/3) +
  geom_smooth(se = FALSE)
windows()

## however, the above can be simplified using 'pipe':
delays <- flights %>% ## %>% is pronounced as 'then'
  group_by(dest) %>%
  summarize(
    count = n(),
    dist = mean(distance, na.rm = TRUE),
    delay = mean(arr_delay, na.rm = TRUE)
  ) %>%
  filter(count > 20, dest != "HNL")

## counts
not_cancelled <- flights %>%
  filter(!is.na(dep_delay), !is.na(arr_delay))
not_cancelled %>%
  group_by(year, month, day) %>%
  summarize(mean= mean(dep_delay))

delays <- not_cancelled %>%
  group_by(tailnum) %>%
  summarize(
    delay = mean(arr_delay)
  )
ggplot(data = delays, mapping = aes(x = delay)) +
  geom_freqpoly(binwidth = 10)

delays <- not_cancelled %>%
  group_by(tailnum) %>%
  summarize(
    delay = mean(arr_delay, na.rm = TRUE),
    n = n()
  )
ggplot(data = delays, mapping = aes(x = n, y = delay))+
  geom_point(alpha = 1/10)

## it is often useful to remove ones with small number of observations
delays %>%
  filter(n> 25) %>%
  ggplot(mapping = aes(x = n, y = delay))+
  geom_point(alpha = 1/10)

install.packages("Lahman")
library(Lahman)
Batting
batting <- Lahman::Batting
batters <- batting %>%
  group_by(playerID) %>%
  summarize(
    ba = sum(H, na.rm = TRUE) / sum(AB, na.rm = TRUE),
    ab = sum(AB, na.rm = TRUE)
  )
batters %>%
  filter(ab > 100) %>%
  ggplot(mapping = aes(x = ab, y = ba)) +
  geom_point() +
  geom_smooth(se = FALSE)
windows()

## Useful summary functions
## measure of location - mean, median
not_cancelled %>%
  group_by(year, month, day) %>%
  summarize(
    #average delay:
    avg_delay1 = mean(arr_delay),
    #average positive delay:
    avg_delay2 = mean(arr_delay[arr_delay > 0])
  )

## measure of spread :sd(), IQR(), mad() where mad=median absolute deviation
not_cancelled %>%
  group_by(dest) %>%
  summarize(distance_sd = sd(distance)) %>%
  arrange(desc(distance_sd))

## measure of rank: min(), quantile(), max()
#when do the first and last flights leave each day?
not_cancelled %>%
  group_by(year, month, day) %>%
  summarize(
    first = min(dep_time),
    last = max(dep_time)
  )

## measure of position: first(), nth(x, 2), last()
not_cancelled %>%
  group_by(year, month, day) %>%
  summarize(
    first_dep = first(dep_time),
    last_dep = last(dep_time)
  )
not_cancelled %>%
  group_by(year, month, day) %>%
  mutate(r = min_rank(desc(dep_time))) %>%
  filter(r %in% range(r))

## counts
not_cancelled %>%
  group_by(dest) %>%
  summarize(carriers = n_distinct(carrier)) %>% # n_distinct counts the number of unique values.
  arrange(desc(carriers))
not_cancelled %>%
  count(tailnum, wt = distance)

# how many flights left before 5am?
not_cancelled %>%
  group_by(year, month, day) %>%
  summarize(n_earlyl = sum(dep_time < 500))

# what proportion of flights are delayed by more than an hour?
not_cancelled %>%
  group_by(year, month, day) %>%
  summarize(hour_perc = mean(arr_delay > 60))

## group by mulitple variables
daily <- group_by(flights, year, month, day)
(per_day <- summarize(daily, flights = n()))
(per_month <- summarize(per_day, flights = sum(flights)))
(per_year <- summarize(per_month, flights = sum(flights)))

## ungrouping
daily %>%
  ungroup() %>%
  summarize(flights = n())

## grouped mutates and filters
# find the worst members of each group
flights_sml %>%
  group_by(year, month, day) %>%
  filter(rank(desc(arr_delay)) < 10)
# find all groups bigger than a threshold
popular_dests <- flights %>%
  group_by(dest) %>%
  filter(n() > 365)
popular_dests %>%
  filter(arr_delay > 0) %>%
  mutate(prop_delay = arr_delay / sum(arr_delay)) %>%
  select(year:day, dest, arr_delay, prop_delay)
