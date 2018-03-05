int1 = 1
float1 = 1
str1 = '1'

print(type(int1)) # <class 'int'>
print(type(str1)) # <class 'str'>

print(float(str1))

print(int1 == str1) # False
print(float1 == float(str1)) # True
print(int1 == float(str1)) # True