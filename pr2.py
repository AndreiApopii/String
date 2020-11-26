a=0
b=0
c=0
n=str(input("dati un sir de caractere :"))
for i in n:
    if ord(i) in range(65,91):
        a+=1
    if ord(i) in range(48,58):
        b+=1
    if (ord(i) in range (33,48)) or (ord(i) in range(58,64)) or (ord(i) in range(91,97)) or (ord(i) in range(123,127)):
        c+=1
print(a,"litere majuscule")
print(b,"cifre")
print(c,"caractere speciale")