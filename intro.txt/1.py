w = open("intro.txt","w")
text=input("Enter input the Text:")
w.write(text)
w.close()

print("Content of  into.txt file is:")
w = open("intro.txt","r")
d = w.read()
print(d)
w.close
