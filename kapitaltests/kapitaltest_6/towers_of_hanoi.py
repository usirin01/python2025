# Drei Stacks für das Spiel "Türme von Hanoi"
a = [3, 2, 1]  
b = []
c = []

print("Wir spielen Die Türme von Hanoi mit 3 Scheiben.")
print("Dies ist die Ausgangslage")
print(a, b, c  )

print("Und nun fangen wir an Züge zu nehmen:")

#Bewegung der Scheiben
c.append(a.pop())
print(a, b, c)

b.append(a.pop())
print(a, b, c)

b.append(c.pop())
print(a, b, c)

c.append(a.pop())
print(a, b, c)

a.append(b.pop())
print(a, b, c)

c.append(b.pop())
print(a, b, c)

c.append(a.pop())
print(a, b, c)  

print("Und damit sind wir fertig:")
print()