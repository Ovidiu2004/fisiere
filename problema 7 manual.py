f=open("D:\Fisiere.txt",'w')
c=str(input('Dati  sirul'))
f.write(c)
f.close()

f=open("D:\Fisiere.txt",'r')
cr=f.read()
print("Sirul:",cr)
f.close()

v=[]
for i in range(0,len(cr)):
    if cr[i]=='a' or cr[i]=='i' or cr[i]=='e' or cr[i]=='o' or cr[i]=='u' or cr[i]=='A' or cr[i]=='E' or cr[i]=='I' or cr[i]=='U' or cr[i]=='O':
      v.extend(cr[i])

f=open("C:\Informatica vocale.txt",'w')
f.write(str(v))
f.write("\n ")
f.write(str(len(v)))
f.write("vocale")
f.close()