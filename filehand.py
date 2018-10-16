#Q.1- Write a Python program to read n lines of a file.
f=open(r"C:\Python\Python36-32\Doc\filehandling.txt","r")
print(f.read())
f1=f.readlines()
for i in f1:
    print(i)
f.close()
print('-'*50)
#Q.2- Write a Python program to count the frequency of words in a file.
f=open(r"filehandling.txt","r")
f1=f.read()
s=input("enter a word for counting its occurence: ")
c=0
for i in f1:
    if i==s:
        c+=1
f.close()
print(s,"occurs",c,"times.")
print('-'*50)
#Q.3- Write a Python program to copy the contents of a file to another file
f=open(r"filehandling.txt","r")
f1=f.read()
f.close()
f2=open(r"abc.txt","w")
f2.write(f1)
f2.close()
print('-'*50)
#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
f=open(r"filehandling.txt","r")
f1=open(r"abc.txt","r+")
for i,j in zip(f,f1):
    f1.write(i+j)
f.close()
f1.close()
print('-'*50)
#Q.5-Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers
#and then store it to another file.
import random
f=open(r"abc.txt","w+")
for i in range(10):
    num=random.randint(1,10)
    f.write(str(num))
f.close()
f=open("abc.txt","r")
f1=f.read()
l=[]
for i in f1:
    i=int(i)
    l.append(i)
l.sort()
f2=open(r"filehandling.txt","w")
for j in l:
    f2.write(str(j))
f2.close()
f.close()
print('-'*50)
