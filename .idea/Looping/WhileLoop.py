count =0
while(count<3):
    count=count + 1
    print("hello")

#Using else statement with while loops
while(count<3):
    count = count+1
    print("hello")
else:
    print("In else when condition get false")

n=4
for i in range(0, n):
    print(i)

print("List Iterator")
l=["Namanand", "Saudagar", "Dada"]
for i in l:
    print(i)

# Iterating over a String
s="Saudagar"
for i in s:
    print(i)

# Iterating over dictionary
d=dict()
d['xyz']=123
d['asd']=234
for i in d:
    print("%s  %d" % (i, d[i]))

# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),

list = ["geeks", "for", "geeks"]
print(len(list))
for index in range(len(list)):
    print(list[index])

list=["saudagar", "Kumar", "Bhosale"]
for index in range(len(list)):
    print(list[index])
else:
    print("this else")
