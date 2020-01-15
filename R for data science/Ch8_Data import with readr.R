library(tidyverse)
# read_csv: reads comma-delimited files
# read_csv2: reads semicolon-separated files
# read_tsv: reads tab-delimited files
# read_delim: reads files with any delimiter
# read_log: reads apache style log files

read_csv("a,b,c
         1,2,3
         4,5,6")

read_csv("the first line of metadata
         the second line of metadata
         x, y, z
         1, 2, 3", skip = 2)

read_csv("# a comment i want to skip
         x, y, z
         1, 2, 3", comment = "#")

read_csv("1,2,3\n4,5,6", col_names = FALSE)
read_csv("1,2,3\n4,5,6", col_names = c("x", "y", "z"))

read_csv("a,b,c\n1,2,." , na = ".") # this treats . as a missing value


## parsing a vector
## parsing: 구문분석. xml, json등의 원시파일이 있을 때 이것을 코드단에서 사용하기 위해 
## 구문을 분석하여 원하는 언어의 구조에 맞게 변환하는 작업.

# parse_* functions take a char vector and return a mor specialized vector like a logical, integer, or date
x <- c("TRUE", "FALSE", "NA")  # class(x) returns 'character'
x2 <- parse_logical(x) # class(x2) returns 'logical'
str(parse_logical(x))
str(parse_integer(c("1", "2", "3")))
str(parse_date(c("2010-01-01", "1979-10-14")))
?str() # str shows internal 'structure' of an object. don't confuse with string
# * includes logical, double, character, factor(for categorical variables), date, time, datetime, etc.

# numbers:
parse_number("$100") # this ignores th e"$". _number is useful when extracting just numbers.
parse_number("20%")
parse_number("it costs $123.45")

parse_number("123,456,789")
parse_number("123.456.789", locale= locale(grouping_mark = "."))
parse_number("123'456'789", locale= locale(grouping_mark = "'"))

# change type of variable
challenge <- read_csv(
  readr_example("challenge.csv"),
  col_types = cols(
    x = col_double(),
    y = col_date()
  )
)

challenge2 <- read_csv(readr_example("challenge.csv"),
                       col_types = cols(.default = col_character()))

# writing to a file
write_csv(challenge, "challenge.csv") # note that type info is lost when save to csv