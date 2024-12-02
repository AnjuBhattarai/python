#list-->array(js)
#dictionary-->object(js),key value from ma hunxa
#tuple-->immutable,change,manipulate garna mildaina -("hello")
#set-->unique only rakxa,duplicate hataidinxa
#constant data matra halinxa tuple ma
# list ma [] hunxa,and tuple ma ( )small brackets matra use hunxa and dict-->{}
shoes=["nike","adidas"]
shoes.append("puma")
print(shoes)
shoes2= ("puma","nike")
#firstName #-->camelcase
#first_name#-->snakecase(python ma mostly use hunxa)
my_set = {"anju","anju","bhattarai"}
print(my_set)
is_raining=True
if is_raining:
      print("carry an umberlla")
else:
      print("Dont carry umberlla")

temperture = 23

if temperture>30:
     print("hot weather")
elif temperture>20:
      print(" normal weather")
else:
      print("cold weather")  
      #indentation
      days =["sunday","monday","tuesday"]
      for hello in days:
            print(hello)

      fruits= ("apple","mango")
      for fruit in fruits:
            print(fruit)

def sayHello(name):
      print(f"Hello {name}")

sayHello("Anju")  


#days=["sunday","monday","tuesday","wednesday"]
#make = function that prints each day by looping using for in

days=["sunday","monday","tuesday","wednesday"]
def myFun(days):
      for day in days:
            print(day)

myFun(days)



      





