print('******************************************')
print('LCS2021 - Algoritmo para conversão de base')
print('******************************************')

N=int(input('Qual número decimal você deseja converter para binário?\n'))

#passo 0
k=0

n = []
n.append(N)

q=[]
a=[]

while True:
    print('***************************************')
    print('k'+str(k)+'='+str(k))
    print('n'+str(k)+'='+str(n[k]))

    #passo 1
    quoc=int(n[k]/2)
    q.append(quoc)
    print('q'+str(k)+'='+str(q[k]))

    a.append(n[k] % 2)
    print('a'+str(k)+'='+str(a[k]))

    #passo 2
    if q[k] == 0:
        break
    else: n.append(q[k])

    k=k+1

#print(n)
#print(q)
a.reverse()

print('***************************************')
num=''
for i in a:
    num=num+str(i)

print('Número convertido:'+str(num))
print('***************************************')





