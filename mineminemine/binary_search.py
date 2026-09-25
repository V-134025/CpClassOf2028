numb = ["A","B","C","D","E","F"]
import math

search = int(input("What letter?"))         # idk how to convert C to the number 3

Low = 0
High = len(numb)-1
Mid = int((Low+High)/2)

while Low < High:
    if search == (Mid):
        print ("Found")
        Low=High
    elif search < Mid:
        High = Mid
        print(Mid)
        Mid=int((Low+High)/2)
    elif search > Mid:
        Low=Mid
        print(Mid)
        Mid=math.ceil((Low+High)/2)         # for some reason it doesnt round 4.5 to 5 unless i import this