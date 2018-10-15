#Q.1- Print the current day using Datetime module.
from datetime import date
import calendar
my_date=date.today()
print(calendar.day_name[my_date.weekday()])
print('-'*50)

#Q.2-  Open your browser
#and play a video using webbrowser module in python.
import webbrowser
import time

total_breaks=3
break_count=0
while(break_count<total_breaks):
    print("this is program on:"+time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=VBN3bjxlTGc")
    break_count+=1
print('-'*50)

#Q.3-  Write a program to rename all the files in a directory
#and convert them into .jpg file format.

import os
path='D:\Python\Python37-32\Doc'
files=os.listdir(path)
i=1

for file in files:
    os.rename(os.path.join(path,file),os.path.join(path,str(i)+'.jpg'))

    i+=1
    print("work done")
