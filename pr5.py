cnp=str(input("dati cnp :"))
a=0
b=0
for i in cnp:
    if ord(i) in range(48,58):
        a+=1
    else:
        b+=1
if (f!=0) or (len(cnp)!=13):
    print("cnp este incorect")
else:
    print("cnp este corect")