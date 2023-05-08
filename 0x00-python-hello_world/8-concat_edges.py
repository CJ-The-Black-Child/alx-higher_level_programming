#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = '{}{}{}'.format(str[37:67], str[-22:-17], str[:6])[2:]
print(str)
