#!/usr/bin/python3.12

#Exec. Write a function to remove duplicates from a list.

listnum = [10,12,13,12,10]
set1 = set(listnum)
print(f'The list without duplicate: {set1}')

#Exec. Print the common values between set1 and set2
list2 = [12,200,10,12,13]
set2 = set(list2)
print(f'set2 = {set2}')

common =  set1 & set2
print(f'The command values are : {common}')
