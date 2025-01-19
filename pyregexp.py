#Python script to validate the IPv4 address using regular expression.
import re

ipv4 = ["339.12.5.6","10.10.10.10","2345.4.5.6","3.4.5.345","5.5.5","xx.yy.aa.bb"]
for ip in ipv4:
  octdiv = ip.split(".")
  res = 1
  if len(octdiv) == 4:
    for dig in octdiv:
      if len(dig) == 3:
        x = re.findall("25[0-5]|2[0-4][0-9]|1[0-9][0-9]", dig)
        if x:
          res =1
        else:
          res = 0
      elif len(dig) == 2:
        x = re.findall("\d\d",dig)
        if x:
          temp = 1
        else:
          res = 0
      elif len(dig) == 1:
        x = re.findall("\d",dig)
        if x:
          temp = 1
        else:
          res = 0
      else:
        res = 0
    if res:
      print(f'{ip} is a valid IP address')
    else:
      print(f'{ip} is an invalid IP address')
  else:
    print(f'{ip} is an Invalid IP address')   

###
exp = "This is the string to check regular expression"
x = re.findall("^This", exp)
print(f'The status of the regular expression is: {x}')


ex = "helXo"
y = re.findall("he..o",ex)
print(y)

ex2 = "moul"
z = re.findall("i$",ex2)
print(z)

ex3 = "kannan"
a = re.findall("^k", ex3)
print(a)

b = re.findall("kan*",ex3)
print(b)
i = 0

#Print the name that starts with letter M
li = ["Murali","Mouli","Sri","Sathish","kannan"]
for x in li:
    y = re.findall("^M",x)
    if y:
        if y[0]== "M" :
          print(f'The Names start with M are: {li[i]}')
        else:
          print("No Match")
    i+=1
#Print the names that ends with the letter i
i = 0
#li = ["Murali","Mouli","Sri","Sathish","kannan"]
for x in li:
    y = re.findall("i$",x)
    if y:
        if y[0]== "i" :
          print(f'The Names ends with are: {li[i]}')
        else:
          print("No Match")
    i+=1


