'''
Type Checking-is used to check the value 

'''
a = 10
b = 15.5
c = "Sreeja"
d = [1,2,3,4,5,6]
e = (1,2,3,10,45,6)
f = {1,2,3,4,5,6}
g = {"name":"Sreeja"}
print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,list))
print(isinstance(e,list))
print(isinstance(f,set))
print(isinstance(g,dict))
#checking with multiple data types
x = 'Jagath'
if isinstance(x,(int,float)):
    print("x is a number")
else:
    print("x is a String")

#checking of object's class:
class A:
    pass
class B:
    pass
b = B()
print(isinstance(b,A))
print(isinstance(b,B))


#example
def process(data):
    if isinstance(data, int):
        return data*2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data,list):
        return len(data)
print(process(10))
print(process("Sreeja"))
print(process([1,2,3,4,5,6,7,8]))

#how they ask in interviews
class A:
    pass
class B:
    pass
obj = B()
print(type(obj) == B)
print(type(obj) == A)
print(isinstance(obj,B))
print(isinstance(obj,A))