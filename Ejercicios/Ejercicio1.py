cantidad=0
lista=[]
for i in range(1, 101):
	if i%2!=0:
		lista.append(i)
		cantidad=cantidad+1

print(lista, end=" ")
print(cantidad)