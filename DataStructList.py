# Lecture 7 Data Structure List
# Syntax: separated by commmas and enclosed in []
Lst=['Sanidhihya',21]
print(Lst)
# Using list in list
ll=['Sanidhiya',21,['Sharma', 9]]
print(ll)
print(ll[-1])
# List are mutable
ll[0]='bruh'
print(ll)
# '+' joining two list
l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
l3=l1+l2
print(l3)
# Changing str in list
Strtolist="Sanidhiya"
listconv=list(Strtolist)
print(listconv)
# List Method
# append(): To add in the end
l1.append(10)
print(l1)
# extend(): To add multiple values
num=[1,2,3,4]
addn=[5,7,9]
num.extend(addn)
print(num)
# assignment vs copy function
a=[1,2,3]
b=a
print(a,b)
a[-1]=1
print(a,b)
# Above assignment assigns the idx to the variable that is change in one is seen in other too.
c=a.copy()
a[0]=3
print(a,b,c)
# copy(): replicate at different location
# count(): count the occurence of the character entered
print(c.count(1))
# clear(): delete the content of list
print(a.clear())
# index(): return the index of the character
idx=c.index(1)
print(idx)
# reverse(): reverse the list
num.reverse()
print(num)
# sort(): used to sort the list
unsrt=[1,4,2,3,5,7,1]
unsrt.sort()
print(unsrt)
# min and max function
print(min(unsrt))