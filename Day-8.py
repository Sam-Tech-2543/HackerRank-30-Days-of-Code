# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

myDict = {}

for i in range(n):
    s=input()
    s1=s.split()[0]
    s2=s.split()[1]
    myDict[s1] = s2
    

while True:
    try:
        s=input()
        if s in myDict.keys():
            print("{}={}".format(str(s),str(myDict[s])))
        else:
            print("Not found")
    except EOFError:
        break            