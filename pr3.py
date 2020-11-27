a=str(input("ce faci? "))
b=str(input("ce vrei sa faci? "))
c=str(input("unde ai fost azi? "))
d=str(input("cine te asteapta acasa? "))
if(len(a.split(" "))>1)or(len(b.split(" "))>1)or(len(c.split(" "))>1)or(len(d.split(" "))>1):
    print("raspunde printr-un cuvant")
else:
    print("cuvintele erau :",a,b,c,d)
    print(f'Acum {a}, vreau {b}, am fost la {c}, acasa ma asteapta {d}.')