library(ggplot2)
library(gcookbook)
install.packages("gcookbook")

qplot(mtcars$wt, mtcars$mpg)

qplot(temperature, pressure, data=pressure, geom=c("point", "line"))

table(mtcars$cyl)
barplot(table(mtcars$cyl))
qplot(cyl, data=mtcars, geom="bar", stat="identity")

ggplot(BOD, aes(x=Time, y=demand)) + geom_bar(stat="identity")
qplot(Time, demand, data=BOD, geom="bar", stat='identity')

qplot(mtcars$mpg)
qplot(mpg, data=mtcars, binwidth = 4)

qplot(supp, len, data=ToothGrowth, geom="boxplot")

myfun <- function(xvar) {
  1/(1 + exp(-xvar + 10))
}
curve(myfun(x), from=0, to=20)
x = c(0,20)
qplot(x = c(0,20), fun = myfun(x), stat="function", geom="line")

library(plyr)

Cultivar <- c("c39", "c39", "c39", "c52", "c52", "c52")
Date <- c("d16","d20","d21","d16","d20","d21")
Weight <- c(3.18, 2.80, 2.74, 2.26, 3.11, 1.47)
sd <- c(0.95, 0.27, .098, 0.44, 0.79, 0.21)
se <- c(0.30, 0.08, 0.31, 0.14, 0.25, 0.06)
n <- c(10)

cabbage_exp <- data.frame(Cultivar, Date, Weight, sd, n, se)
cabbage_exp

ggplot(cabbage_exp, aes(x=Date, y=Weight, fill=Cultivar, order= desc(Cultivar)))+
  geom_bar(stat="identity")

windows()

ggplot(cabbage_exp, aes(x=Date, y=Weight, fill= Cultivar))+
  geom_bar(stat="identity", colour="black")+
  guides(fill=guide_legend(reverse=TRUE)) +
  scale_fill_brewer(palette="Pastel1")

ddply(cabbage_exp, "Date", transform, percent_wegith = Weight / sum(Weight)*100)

ggplot(cabbage_exp, aes(x=interaction(Date, Cultivar), y=Weight)) +
  geom_bar(stat="identity") +
  geom_text(aes(label=Weight), vjust=-0.2)+
  ylim(0, max(cabbage_exp$Weight)* 1.05)

ggplot(cabbage_exp, aes(x= Date, y= Weight, fill=Cultivar))+
  geom_bar(stat="identity", position="dodge") +
  geom_text(aes(label=Weight), vjust=1.5, colour="white",
            position= position_dodge(0.9), size= 3)
