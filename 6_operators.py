'''
# Arithmetic Operators
x=2
y=5

total=x+y
print(total)

total=x-y
print(total)

total=x*y
print(total)

total=y/x
print(total)

total=y%x
print(total)

total=y**x
print(total)

#comparison operators  output return in boolean value
x=10
y=20

out=x>y
print (out)

out=x==y
print (out)

out=x!=y
print (out)

out=x>=y
print (out)

#Assignment operators
c=0
d=1

print(c)

c+=d #c=c+d
print(c)
c-=d #c=c-d
print(c)

a=20
b=30

x=2
y=8

out = (a<b) or (x>y)
print(out)

out = (a<b) and (x>y)
print(out)

out = (a<b) and (x<y)
print(out)

out = not(a>b)
print(out)
'''
#membership operator

devops=["aws","jenkins","docker",1234,"bash scripting"]
skills = {"devops":("aws","jenkins","ansible"), "development":["java","python","nodejs"]}

ans = "development" in skills
print(ans)