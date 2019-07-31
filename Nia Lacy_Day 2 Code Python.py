# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello my name is Nia")
print("5*2")
print(5/2)
print(5**2)
print((8/9)*(3))

#functions
def multiply (a,b):
    multiply = a*b
    
def sum (a,b,c):    
    sum = (a+b+c)
    print(sum)
sum(6,7,8)

def area (b,h):
    area = (0.5)*b*h
    print("The value of the base", b," multplied by the value of the height",h," multiplied by .5, equals",area)
area(7,2)



#variables
Cadbury1 = "Milk Chocolate"
Cadbury2 = "Dark Chocolate"
Cadbury3 = "White Chocolate"



cadburryType1 = "and 6 milk chocolate"
cadburryType2 = "5 dark chocolate"
cadburryType3 = "8 white chocolate"

print("there are", cadburryType1, cadburryType2, cadburryType3)

#dict (only hold two pieces of information)
choc1 = {"dark chocolate":6}
choc2 = {"milk chocolate":8}
choc3 = {"white chocolate":5}
         
print(choc1, choc2, choc3)

chocolatebox = {"dark":5, "milk":6, "white":4}
print(chocolatebox)

students = {"steve":32, "lin":28, "vin":45, "katie":38}
print("The students ages are", students)

studentage = {"steve":32, "lin":28, "vin":45, "katie":38}
studentage

studentgender = {"steve":"M", "lia":"F", "vin":"M", "katie":"F"}
studentgender

#lists (when you use a list you dont need to make dicts, because lists hold more information)
studentlist = [["steve", 32, "M"], ["lia", 28, "F"],["vin", 45, "M"], ["katie", 38, "F"]]
studentlist

#dataframes
import pandas
dir(pandas) 

studentdf = pandas.DataFrame(studentlist, columns=("name", "age", "gender"))
studentdf

import pandas
dir(pandas)
chocolateslist = [["milk", 5], ["dark", 6], ["white", 8]]
chocolateslist

chocolateslistdf = pandas.DataFrame(chocolateslist, columns=("type", "amount"))
chocolateslistdf

#referencing dataframes
studentdf["name"]
studentdf["age"]



chocolateslistdf["type"]
chocolateslistdf["amount"]


#changing the row names
studentlist = [["steve", 32, "M"], ["lia", 28, "F"],["vin", 45, "M"], ["katie", 38, "F"]]
studentlist

import pandas
dir(pandas) 

studentdf = pandas.DataFrame(studentlist, columns=("name", "age", "gender"),index=["1st","2nd","3rd","4th"])
studentdf


#bargraphs

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as graph

studentbar = graph.Bar(x=studentdf["name"], y=studentdf["age"])
plot([studentbar])

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as graph
chocolatesbar = graph.Bar(x=chocolateslistdf["type"], y=chocolateslistdf["amount"])
plot([chocolatesbar])

#title
title=graph.Layout(title = "number of chocolates by type")  
chocolatesbar = graph.Bar(x=chocolateslistdf["type"], y=chocolateslistdf["amount"])

fig=graph.Figure(data=[chocolatesbar], layout=title)                      
plot(fig)
