w=['airline']
n=8
r=[]
h=[]
l=len(w)
c=8
x=w[0]
y=x[0]
b=len(y)
o=len(x)
for i in range (n):
    g=input("ENTER THE GUESS")
    c=c-1
    for j in range (o):
        if(x[j]==g):
            r.append(g)
            print("RIGHT GUESS")
        else:
            ("SORRY! WRONG GUESS")
    for r in range(b):
        for k in range(r):
            if(r[k]==w[j]):
               s=r[k]
               print("%d"%s)
    print(" ATTEMPTS:- %d"%c) 

