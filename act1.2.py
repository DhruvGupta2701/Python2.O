'''demonstrate the use of following functions in python:
abs(),len(),min(),round(),isalnum(),type()'''

#The abs() function returns the absolute value of a number
print(abs(-10))

#The len() function returns the length of a string 
print(len("Welcome to MIET"))

#The min() function returns the minimum value of a sequence
print(min([10,20,30]))

#The round() function rounds a number to a specified number of decimal places
print(round(3.14159,2))

#The isalnum() function returns True if a string contains only alphanumeric characters, False otherwise
print("CSE, 3rd sem!".isalnum())
print("123abc".isalnum())

#The type() function returns the type of an object
print(type(10))
print(type("AI and ML"))

#all()-Returns True if all elements in an iterable are true, otherwise returns false
list1= [True,True,True]
list2= [True,False,True]
print(all(list1))
print(all(list2))

#any()-Returns True if any element in an iterable are true, otherwise returns false
list3= [False,False,False]
list4= [True,False,False]
print(any(list3))
print(any(list4))

#ascii-Returns a string containing a printable representation of an object
#But not its ascii value
print(ascii("Kot, \nBhalwal!"))

#ord()-Returns the unicode code point of a character which is a more impressive character encoding than ASCII
print(ord("a"))
print(ord(" "))
print(ord(","))
print(ord("*"))
