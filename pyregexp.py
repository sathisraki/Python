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

### Validating IP using other logic ###
import re

ipv4 = ["339.12.5.6","10.10.10.10","2345.4.5.6","03.4.5.345","5.5.5","xx.yy.aa.bb","03.04.06.04"]

for ip in ipv4:
  octdiv = ip.split(".")
  op = 1
  if len(octdiv) == 4:
    for x in octdiv:
      res = re.findall("^((2[0-4][0-9]|25[0-5])$|^1|0\d\d$|^\d\d$|^\d$)",x)
      if res:
        temp = 0
      else:
        op = 0
  else:
    op = 0
  if op:
    print(f'The IP {ip} is valid')
  else:
    print(f'The IP {ip} is invalid')

### Very simplified logic to validate the IPv4 address.

import re

ipv4 = ["339.12.5.6","10.10.10.10","2345.4.5.6","03.4.5.345","5.5.5","xx.yy.aa.bb","03.04.06.04","255.255.255.255","256.255.255.255"]

for ip in ipv4:
  res = re.findall("^((2[0-4][0-9]|25[0-5][.])|[0-1]\d\d[.]|\d\d[.]|\d[.]){3}((25[0-5]|2[0-4][0-9])|[0-1]\d\d|\d\d|\d)$",ip)
  if res:
    print(f'{ip} is valid')
  else:
    print(f'{ip} is invalid')
    
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

#Print the name that starts with letter M
i = 0
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

## Write a regular expression script to match the MAC address:
import re

mac1 = "11:22:33:dd:gf:ff"

print(mac1[2])
maclist = mac1.split(":")
print(maclist)
lom = len(maclist)
print(lom)
res = 0
if lom < 6 | lom > 6:
 print("Not a valid mac")
else:
 print("Valid MAC count")
 for mac in maclist:
   if len(mac) == 2:
     x = re.findall("\d\d|^[a-f]\d|^\d[a-f]|^[a-f][a-f]",mac)
     if x:
       res = 0
     else:
       res = 1
   else:
     print("Not a valid MAC due to Octect lenght")
     res = 1
 
if res == 0:
  print("The given MAC address is valid")
else:
  print("The given MAC is invalid")
  

mac2 = "aa-bb-dd-GA-22-44" 
res = re.findall("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$",mac2)
if res:
  print(f'The valid MAC is {res}')
else:
  print("Invalid MAC2")

#### Validate an email id using re.match #####
import re
email = "xyz_abc.kan@exp.in"
x = re.match("^[a-z0-9_\.]+@[a-z0-9]+\.[0-9a-z]+$", email)
if x:
  print(f'{email} is Valid Email id')
else:
  print(f'{email} is Invalid email id')
