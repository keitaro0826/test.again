D=[]
E=[]
with open("input.txt") as input:
    for line in input:
        line=line.strip()
        if  str(line).isdecimal()==False:
            D.append(line)
        else:
            num=int(line)
for i in D:
    a,b=i.split(":")
    E.append((int(a),b))
E=sorted(E)
words=[]
for i in range(len(E)):
    if num%E[i][0]==0:
        words.append(E[i][1])
word="".join(words)
print(word)
