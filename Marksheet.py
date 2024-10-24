a=int(input("Enter a Urdu Marks: "))
b=int(input("Enter a English Marks: "))
c=int(input("Enter a Maths Marks: "))
d=int(input("Enter a physics Marks: "))
e=int(input("Enter a Chemistry Marks: "))
f=int(input("Enter a Islamiat Marks: "))
g=int(input("Enter a pak studies Marks: "))
sum=a+b+c+d+e+f+g
print(sum)
percentage=sum/700*100
print(percentage,"%")

if(percentage>=80):
    print("Grade = A+ ")
elif(percentage>=70 and percentage<79):
    print("A grade")
elif(percentage>=60 and percentage<69):
    print("B grade")
elif(percentage>=50 and percentage<59):
    print("C grade")
else:
    print("You are failed")
    100




