#Q.1- Write a python code to find a valid email address from a text.

import re
str1='The valid email id is sharmaniharika94182@gmail.com Thank you!'
address=re.findall(r'[\w\.-]+@[\w\.-]+',str1)
print(address)

#Q.2-Write a python program to find a valid Indian phone number
#from a text.(Valid Indian numbers will start with "+91-"
#and after that [6-9] followed by 9 digits. )


import re
pattern=r"[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$"
str1=(' my phone no is 9882812376')
valid_no=re.findall(pattern,str1)
print(valid_no)
