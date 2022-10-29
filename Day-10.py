if __name__ == '__main__':
    n = int(input().strip())
    c=0
    lst=[]
    for i in str(bin(n))[2:]:
        if i=="1":
            c+=1
        if i=="0":
            lst.append(c)            
            c=0
    lst.append(c)
            
    print(max(lst))