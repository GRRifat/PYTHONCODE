"""
#read file
file = open("Rifat.txt","r")
text = file.read()
#print(file.readable())
print(text)
file.close()
"""

#write kora
file = open("Rifat.txt","a")

file.write("\nRifat is good boy")
file.close()

