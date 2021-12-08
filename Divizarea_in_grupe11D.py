with open('D:/Lista 11D.txt','r') as f:

    a=list(f)
    f.close()
n=suma=0

print('Nume','Prenume','\tNota','Grupa',sep='\t')
for linie in a:
    campuri=linie.split()
    n1=int(campuri[2])
    n+=1
    suma+=n1
    print(linie)    
s1=s2=0
print("Media celor",n,"studenti este",round(suma/n,2))
x1=x2=0
g1=[]
g2=[]

for linie in a:
    campuri=linie.split()
    if campuri[3]=="engl1":
        s1+=int(campuri[2])
        x1+=1
        g1.extend([linie])
    if campuri[3]=="engl2":
        x2+=1
        s2+=int(campuri[2])
        g2.extend([linie]) 

with open("D:/grupa1.txt","w") as f:
    for p in g1:    
        f.write(p)
        f.write("\n")
with open("D:/grupa2.txt","w") as f:
    for p in g2:    
        f.write(p)
        f.write("\n")

print("Media grupa 1 este",(s1/x1,2))
print("Media grupa 2 este",(s2/x2,2))
