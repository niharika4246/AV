#Q.1-Create a user defined dictionary
#and get keys corresponding to the value using for loop.
dict={}
for i in range (int(input("Enter the key-values :"))):
    dict[i]=i
n=int(input("Enter the value :"))
for key in dict.keys():
    if dict[key]==n:
        print(key)
    else:
        print("key not found!!!")
print("total elements present are:",dict[i])

#Q.2- Create a dictionary and store student names
#and create nested dictionary to store the subject wise marks of every student.
#Print the marks of a given student from that dictionary for every subject.

students={
          "Rahul":{"networks":44,"python":56,"java":40},
          "Ria":{"networks":86,"python":96,"Artificial intelligence":90}
          }
stu_name=input("Enter the name of student you want to search:").title()
if stu_name in students:
    print("stu_name")
    for key,value in students[stu_name].items():
        print(key,value)
else:
    print("No such student in the list.")



