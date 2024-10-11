var=float(input("the first number : "))
var1=input("comp /*+- : ")
var2=float(input("the second number : "))
if var1== "+":
    print(var+var2)
elif var1=="*":
    print(var*var2)
elif var1=="/":
    if var2==0:
        print("error")
    else:
        print(var/var2)
elif var1=="-":
    print(var-var2)

