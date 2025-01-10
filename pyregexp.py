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
  
