#!/usr/bin/python3.12
a = "LightSpan!"
#String access using indexing:
print(a[1])

i = 0
for x in a:
  print(f'the {i} index of the string is {x}')
  i+=1

#Length of the string using len()
print(f'the length of the string is {len(a)}')

#check the existance of string in the statement, return true or false

str = "Python is a great scripting language"
print("great" in str)
print("word" in str)
print("word" not in str)

# if condition to check the presence of word in the statement
if "great" in str:
    print("yes the work great present in the sentencd")

# if condition to check the absence of word in the statement
if "word" not in str:
    print("yes, the word is absent in the statement")

#String slicing operation:
print(f'print the string from 3rd to 7th index a[5:9] is:: {a[5:9]}')

print(f'print the string as a[:5], which start from the beginning to the index : {a[:5]}')

print(f'print the string as a[5:], which prints from index value of 5 to end: {a[5:]}')

print(f'print the string using -ve indexing as a[-5:-1], which prints as : {a[-5:-1]}')

i = -1
for x in a:
    print(f'The index value of {i} is: {a[i]}')
    i-=1
#String built-in methods:upper() lower() split() strip()
a = "lightspan!"
print(f'Convert the lowercase to UPPERCASE using upper() method: {a.upper()}')
b = "LIGHTSPAN!"
print(f'Convert the UPPERCASE to lowercase  using lower() method: {b.lower()}')

c=" The string with space "
print(f'Split will convert the string to list with the space  between the sentence \" The string with space \" as: {c.split()}')

print(f'Remove the white space in the beginning and end of the sentence \" The string with space \": and convert to string as: {c.strip()}')

print(f'Replace method will replace the character in the string,eg: replace s by \" \" in lightspan!{a.replace("s"," ")}')

print(f'check the presence of \"with\" in sentence \" The string with space \" and returns the index position: {c.find("with")}')
#String concatenation:
a = "Light"
b = "Span!"
c = a + b
print(f'we can concat {a} and {b} using a+b to form {c}')
print(f'Lets add space between {a} and {b} using a+\" \"+b to form {a +" "+b}')
                                                                                 
