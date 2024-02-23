# input data (defult string)
text = input()

# input data with msg (defult string)
text = input("please inter text : ")

# input data with msg (convert integer)
number = int(input("please inter number : "))

# get number from user and *10 
number = int(input("please inter number : "))
print(number*10)

# get number from user and show result
number = int(input ("please inter number : "))
if 10<=number<=20:
    print ("you are passed")
elif 0 <= number <10:
    print ("WTF")

# get number from user and show result
number = int(input ("please inter number : "))
if number< 20 and number % 2 == 0:
    print (number)
