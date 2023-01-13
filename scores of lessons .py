#scores of students's lessons
#assignment2-3

name =input("Enter name here:")
familyname= input("Enter familyname here:")
lesson1=float(input("enter score of lesson1="))
lesson2=float(input("enter score of lesson2="))
lesson3=float(input("enter score of leson3="))

average = (lesson1+lesson2+lesson3)/3

print(name, familyname, "average=",average)


if average >=17:
 print(" staatus=great")

if  12<= average <17:
 print("status =normal")

 if average <12:
    print("status=fail")









