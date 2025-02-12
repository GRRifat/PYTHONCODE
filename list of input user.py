numofwords = 0
numofletter = 0
numofdigit = 0

text = input("Enter number: ")

for x in text :
    if x >= 'a' and x <= 'z' :

        numofletter = numofletter + 1

    elif x >= '0' and x <= '9':

        numofdigit = numofdigit + 1

    elif x >= ' ' :

        numofdigit = numofdigit + 1

print(numofwords+1)
print(numofletter)
print(numofdigit)