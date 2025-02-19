#!/usr/bin/python3.12
#List is an ordered, mutable and allows duplicate

itinerary = ["india","srilanka","bangaladesh","nepal","butan"]
print(f'print the full list: {itinerary}')

#looping the list:
for country in itinerary:
  print(f'the index position of {country} is {itinerary.index(country)}')

print("Print the country in the reserver order:")
x = -1
for itr in itinerary:
  print(f'The -ve index of {x} is {itinerary[x]}')
  x=x-1

#Create a list using the method list()
crtlist = list(("asia","eu","na","sa","aus","africa"))
print(f'The continent list is {crtlist}')

print(f'Print the 1st continet using the index [0] {crtlist[0]}')

print(f'Print the values in the list using range like [2:4]: {crtlist[2:4]}')
print(f'Print the values from the index to end using range like [2:]: {crtlist[2:]}')
print(f'Print the values from the beginning to the value before the list using range like [:4]: {crtlist[:4]}')

if "sa" in crtlist:
    print("yes sa in the continent list")
else:
    print("No sa is not in the continent list")


if "ant" not in crtlist:
    print("True, yes Antartica is not in crtlist")
else:
    print("False, Antartica is in crtlist")

#Changing the list values:
itinerary[2] = "Maldives"
print(f'Change the itinerary, modify bangaladesh to Maldives {itinerary}')

#change the range of item values
itinerary[1:3] = ["Burma","Malaysia"]
print(f'using index range [1:3] modify the values in list {itinerary}')

#Insert new values in the list
itinerary[1:2] =["Korea","japan"]
print(f'Insert new values in the list eg:[1:2]: {itinerary}')

#insert method
itinerary.insert(4,"Russia")
print(f'Use insert(4,"Russia") in to the list: {itinerary}')

#append method
itinerary.append("indonesia")
print(f'append() will add the value to the end of the list:{itinerary}')

#sort method
itinerary.sort()
print(f'The list can be sorted using sort method: {itinerary}')
itinerary.sort(reverse = True)
print(f'The list can be sorted in reverse order: {itinerary}')

#reverse method
itinerary.reverse()
print(f'The reverse method will print in reverse order:{itinerary}')

#Extend method to add two list
eulist = ["Belgium","France","Swiss"]
itinerary.extend(eulist)
print(f'Extending the itinerary with eu list : {itinerary}')

#len method
print(f'The length of the list: {len(itinerary)}')
#remove method
itinerary.remove("Korea")
print(f'Remove the values Korea from the list using remove() method: {itinerary}')


#pop method
itinerary.pop()
print(f'pop() method will remove the last value from the list: {itinerary}')
itinerary.pop(4)
print(f'pop(4) method will remove the value from the index in the list: {itinerary}')

#del keyword
del itinerary[3]
print(f'del keyword with index will remove the value at that index: {itinerary}')
del itinerary

#print(f'del keyword will empty the lis: {itinerary}')

itinerary = ["ind","sa","aus"]
itinerary.clear()
print(f'clear() method will empty list : {itinerary}')
                                                          
#Search the number and depth using the Binary search.
numlist = [20,343,23,10,45,12,60]
print(numlist.sort())

print("Enter the number you want to search")
search = input()
start = 0
notfound = 1
depth = 0
end = (len(numlist))
while notfound:
    mid=int((start + end)/2)
    if numlist[mid] == (int(search)):
        print(f'The number {search} is at {mid}')
        notfound = 0
    elif numlist[mid] < int(search):
        start = mid + 1
    else:
        end = mid - 1
    depth+=1
print(f'The Depth of the number is {depth}')
## Sum the positive number from the list
print("enter the list of number")
numlist = input()
numdup=numlist.split(",")
total=0
### CM logic
for i in range(0,len(numdup)):
    if int(numdup[i]) > 0:
        total=total + int(numdup[i])
print(f'The sum of all integer numbers is {total}')

##SK Logic
total =0   
for x in numdup:
  if int(x) > 0:
    total = total + int(x)

print(f'The sum of all integer numbers is {total}')


## Validation of Palindrome
def palindrome(s):
    s1 = s[::-1]
    if s == s[::-1]:
        print(s1)
        return True
    else:    
        print(s1)
        return False
print("Enter the String:")
name=input()
print(palindrome(name))  
