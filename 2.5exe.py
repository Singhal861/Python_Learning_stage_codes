def fun1(a, b):
    """"This function is used print star pattern according to your no. & boolean expretion"""
    if b==True:
        i=0
        while(i<a):
            i=i+1
            print("*"*i)
    if b==False:
        i=a
        while(i>0):
            print("*"*i)
            i=i-1
print(fun1.__doc__)
try:
    a = int(input("Enter your no.= "))
    b = bool(int(input("Enter your boolean(0/1) no.= ")))
    fun1(a,b)
except Exception as z:
    print(z)

