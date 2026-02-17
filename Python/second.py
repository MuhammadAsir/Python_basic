a=100
print(a,type(a))
number=input("enter a number ")

number=int(number)
if number%2==0:
        print("EVEN")
else:
        print("ODD")
        

w=68.7
h=1.79
bmi=w/(h**2)
print(bmi,type(bmi),"\n")

x="my name is asir"
print(x,type(x),"\n")

y=True
print(y,type(y),"\n")
z='abc'
a='def'
print(z+a,type(z+a),"\n")

family=["asir","sadia","mahir"] #array or list
print(family,type(family),"\n")

fam2=[["asir",26],["sadia",24],["mahir",33]]
print(fam2,type(fam2),"\n")

fam3=['1', '2', '3', "emma", '14', '15', '16', '16']
print(fam3[3:5],"\n") # 3 to 4

print(fam3[:6]) # 0 to 5

print(fam3[2:]) # 2 to end

family=family+["abir"] #adding element to list
print(family)

del(family[3]) #deleting element from list
print(family)

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

areas_copy = list(areas) #copy of original list is created

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas) #original list is not changed
print(areas_copy) #copy of original list is changed

print(max(areas)) #maximum value in the list