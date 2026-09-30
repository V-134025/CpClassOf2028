numb = ["A","B","C","D","E","F","G","H"]
#        0   1   2   3   4   5   6   7

search = input("What letter?")

Low = 0
High = len(numb)-1

while Low <= High:
    Mid = (Low+High)//2
    
    if numb[Mid] == search:
        print("Found")
        Low = High + 1
    elif numb[Mid] < search:
        Low = Mid + 1
    else:
        High = Mid - 1