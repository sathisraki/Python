#!/usr/bin/python3.12
thisdict = dict(name = "John", age = "36", country = "Norway")
print(f'The Original Dictionary is ; {thisdict}')


for x in thisdict.values():
#    print(x)
    y = x.isalpha()
    if(y):
        print(f'{x} is String')
    else:
        print(f'{x} is numeric')
        z=int(x)+50
        print(z)
        if int(x) < 100:
            print("the number is less than 100")

#Exec: Given a list of dictionaries, write a function to merge them into a single dictionary
dic1 = { "name" : "sathish", "age" : "41" }
dic2 = { "name" : "kannan", "age" : "41" }
dic3 = { "name" : "mouli", "age" : "32" }

master = { "list1" : dic1 , "list2" : dic2 , "list3" : dic3 }

print(f'The master dictionary is : { master }')
print(master["list1"]["name"])

#Exec:Write a function to invert a dictionary (swap keys and values).
invertdic = dict()
for key in thisdict:
    invertdic.update({thisdict[key] : key })

print(f'The inverted dic is : {invertdic}')
