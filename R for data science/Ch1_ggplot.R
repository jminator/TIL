install.packages("tidyverse")
install.packages("maps")
library(tidyverse)
mpg

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) ## displ = engine size, hwy = fuel efficiency
## geom_point adds a layer of points to the plot.
## mapping argument is always paired with aes()
## aes: short for aesthetics
windows()

## adding aesthetics(colour, size, shape, etc):
ggplot(data=mpg) +
  geom_point(mapping = aes(x= displ, y= hwy, colour = class))
ggplot(data=mpg) +
  geom_point(mapping = aes(x= displ, y= hwy, size = class))
ggplot(data=mpg) +
  geom_point(mapping = aes(x= displ, y= hwy, alpha = class))
ggplot(data=mpg) +
  geom_point(mapping = aes(x= displ, y= hwy, shape = class))

ggplot(data=mpg) +
  geom_point(mapping = aes(x= displ, y= hwy), colour = "blue") ## turns every point blue
ggplot(data=mpg) +
  geom_point(mapping = aes(x= displ, y= hwy), shape = 8, colour = "red")


## creating subplots(Facets)
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) +
  facet_wrap(~ class, nrow = 2)

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) +
  facet_grid(. ~ cyl)

## geometric objects
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y= hwy, colour = drv))

ggplot(data = mpg) +
  geom_smooth(mapping = aes(x = displ, y = hwy))

ggplot(data = mpg) +
  geom_smooth(mapping = aes(x = displ, y = hwy, linetype = drv, colour = drv))

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y= hwy)) +
  geom_smooth(mapping = aes(x = displ, y = hwy))

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y=hwy, colour = drv)) +
  geom_smooth(mapping = aes(x = displ, y=hwy, colour = drv))

## to tidy up the code,:

ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) +
  geom_point(mapping = aes(colour = class)) +
  geom_smooth()

ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) +
  geom_point(mapping = aes(colour = class))+
  geom_smooth(
    data = filter(mpg, class == "subcompact"),  ## line graph will show class = subcompact
    se = FALSE ## the line graph will not show standard error area
  )

## bar graphs
ggplot(data = diamonds, mapping = aes(x = cut)) +
  geom_bar()
## this is the same as:
ggplot(data = diamonds, mapping = aes(x = cut)) +
  stat_count()

## position adjustments
ggplot(data = diamonds, mapping = aes(x = cut)) +
  geom_bar(mapping = aes(fill = cut))

ggplot(data = diamonds, mapping = aes(x = cut)) +
  geom_bar(mapping = aes(fill = clarity))

ggplot(data = diamonds, mapping = aes(x=cut, fill = clarity)) +
  geom_bar(alpha = 1/5, position = "identity")
ggplot(data = diamonds, mapping = aes(x=cut, colour = clarity)) +
  geom_bar(fill = NA, position = "identity")

ggplot(data = diamonds) +
  geom_bar(
    mapping = aes(x = cut, fill = clarity),
    position = "fill" ## makes each set of stacked bars the same height
  )

ggplot(data = diamonds) +
  geom_bar(
    mapping = aes(x = cut, fill = clarity),
    position = "dodge" ## places overlapping objects directly beside one another
  )

## only useful for scatterplot:
ggplot(data = mpg) +
  geom_point(
    mapping = aes(x = displ, y = hwy),
    position = "jitter" ## adds small noise to each point to avoid overplotting to see the weight of the data
  )

args(geom_jitter)


## coordinate system
ggplot(data = mpg, mapping = aes(x = class, y = hwy))+
  geom_boxplot()
ggplot(data = mpg, mapping = aes(x = class, y = hwy))+
  geom_boxplot() +
  coord_flip() ## switches x and y axes.

nz <- map_data("nz")
ggplot(nz, aes(long, lat, group = group)) +
  geom_polygon(fill = "white", colour = "black")
ggplot(nz, aes(long, lat, group = group)) +
  geom_polygon(fill = "white", colour = "black") +
  coord_quickmap() ## sets the aspect ratio correcly for maps

bar <- ggplot(data = diamonds) +
  geom_bar(
    mapping = aes(x = cut, fill = cut),
    show.legend = FALSE,
    width = 1
  ) +
  theme(aspect.ratio = 1)+
  labs(x = NULL, y = NULL)

bar + coord_flip()
bar + coord_polar()
