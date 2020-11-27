a=str(input("dati primul cuvant "))
b=str(input("dati al doilea cuvant "))
c=str(input("dati al treilea cuvant "))
d=str(input("dati al patrulea cuvant "))
if (len(list(a))<3)or(len(list(b))<3)or(len(list(c))<3)or(len(list(d))<3):
    print("scrie cuvinte formate din minim 3 litere")
else:
    x=int((len(d))/2)
    print("cuvintele erau :",a,b,c,d)
    print("cuvantul format :"a[:1]+b[0]+c[2]+d[:x])