#Program to enter marks of Five Subjects and Display the Total, Avg and Class
"Computer Programming Tutor,Sept 3, 2021"

a = int(input("Enter Marks: Soil Mechanics:"))
b= int(input("Enter Marks: Fluid Mechanics:"))
c = int(input("Enter Marks: Topographical Surveying:"))
d = int(input("Enter Marks: Computer Science:"))
e = int(input("Enter Marks: Theory of Structures 1:"))

total = a + b + c + d + e
avg = total/5

print("Total Marks: ",total)
print("Average Marks:",avg)
