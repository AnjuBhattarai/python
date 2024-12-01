# variable
# it is something that contains value
bottle = "pani"
print(bottle)
print(f"water is called {bottle} in nepali")
# f vaneko dynamic contant halna paiyo
print("there is "+bottle)

#list/variable
shoe1 = "nike"
shoe2 = "adidas"


#if the data is of same category then use list

shoes = ["nike","adidas","umbro"]
#its better practice to use list then variable if the data is of same type
#list is always in square bracket
#to print adidas only like you can print in such a way
print(shoes[1])

print(shoes[-1])#and to print only of last you can do


print(shoes[0:2])#you can also print in range,so in this data nike and adidas will be printed

print(len(shoes))#now to print the length of list yo can do


shoes.append("infinity")#to add data on the list you can use append
print(shoes)

shoes.pop()#delete last data from list
print(shoes)

shoes.insert(0,"Hello")#insert data in defined index
print(shoes)

name = "hello"
planet ="earth"
#so,in such case use variable instead of list couse data are different


#*******************************************
#dictonary
me={
    "name" : "anju",
    "age" : 22
}
print(me["name"])#only to print name from the defined dictonary
del me["age"] #by th euse of del you can delete data of the dictonary
print(me)

#left ko keys , right ko values in dictonary
print(me.keys())
print(me.values())