# strings in python
# Strings are  sequences of characters. In Python, a string is alwayes written in '' or " "  

print("Hello World")   # Hello World

# Assingn String to a variable 

a = 'Australia'
print(type(a))
print(a[1])    # returns the character at position of index[1]



#loops in String

a = 'banana'
for n in a:     # loop through each character in the string
    print(n)



# String Methods

b=[x for x in a if 'a' in x ]
print (b)



# multi lins string

mul_line_str ='''all this lines are 
in one single multiline string '''
print(type(mul_line_str))
print(mul_line_str)



# Strip method

c= "     hello world"
print(c)
print(c.lstrip())     # removes the  whitespaces in the left side of the  string
M="hello World      "
print(M)
print(M.rstrip())     # removes the  whitespaces in the right side of the  string
print(M)

d="   This Is A Test String For Check   "
print(d.strip())      # Removes the white spaces in both left and right sides of the string

c = "!!hello world!!"
print(c.strip('!'))   # returns 'hello world' by removing ! on the right and left sides



# Modify strings

e= "Hello, World!"
print(e.upper())            # Converts all characters to uppercase

F = "Hello, World!"
print(F.replace("H", "J"))  # replaces H with J 

G = 'I ,Love ,Coding '
print(type(G))
print(G.split(','))         # Splits the string at the commas 



#concatinate  Strings

h1= 'hello'
h2= 'world'
h3=h1+" "+h2 #concatenates two strings using + operator
print(h3)


a = "Hello"
b = "World"
c = a + b
print(c)
