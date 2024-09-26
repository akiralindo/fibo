a=input("Digite a string: ")
count=0
for i in range(len(a)):
    if a[i] == 'a' or a[i] == 'A':
        count += 1
print(count)
