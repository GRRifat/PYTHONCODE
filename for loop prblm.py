A=["Rifat","Fahi","Ashad","najmuls","Samiyais"]

if not A :
    print("Empty")

else :
    a = A[0]
    for x in A :
         if len(x) > len(a) :
             a=x
    print(a)





