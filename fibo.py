a=0
b=1
c=0
n=int(input("Digite o número: "))
while c<n:
    c=a+b
    a=b
    b=c
    print(c)
    if c==n:
        print("Está na sequencia")
        break
    if c>n:
        print("Não está na sequencia")
        break
    
        
