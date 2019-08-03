x = 15
y = 3
z = "This is a string"
a = "concatenated"

print (z,a)

mylist = [1,2,45,67];

for i in range (0,10,2):
    print(i)

for i in mylist:
    print(i)

def myPrint(words):
    print(words, "ok" );

myPrint("are you");

def myFunction(vList):
    for i in vList:
        print(i)

myFunction([1,'abc']);



def myRecursiveFunction(vList):
    if len(vList) > 0:
        print(vList.pop())
        myRecursiveFunction(vList)

myRecursiveFunction(["hello", 1, "abc"])