```python:
f = open("myfile.txt","w")
l1 = input("Enter the Text")
l2 = input("Enter the TEXT 2")
l3 = input("Enter the text")
f.write(l1)
f.write("\n")
f.write(l2)
f.write("\n")
f.write(l3)
f.write("\n")
f.close()

print(" Test of myfile.txt :")
f=open("myfile.txt","r")
d = f.read()
print(d)
f.close
```
