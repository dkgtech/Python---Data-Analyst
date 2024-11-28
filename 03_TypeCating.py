# there are two types of type-casting --> implicit & explicit

#implicit - where python itself converts one datatype into another
#explicit - where the user converts one datatype into another


name = "Dipesh"
print(type(name))

age = 24
print(type(age))

#implicit

a = 123
b = 1.23
print("Type of a is ",type(a))
print("Type of b is ",type(b))

c= a+b
print("The sum of a + b is ",c)
print("Type of c is ",type(c))