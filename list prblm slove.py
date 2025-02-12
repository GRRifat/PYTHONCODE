sum=0

while True :
    n = int(input("Enter Number "))

    if n<0:
        print("skip")
        continue


    elif n==0:
        print("tham baba")
        break

    elif n%2==1:
        sum = sum+n

print("Total number: ",sum)