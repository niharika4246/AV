import requests
import json
response=requests.get(" https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?")
print(response.content)
b'?({"quoteText":"dont feel distessed when you are friendzone it is a new begining of life".  ", "quoteAuthor":"abc ", "senderName":"", "senderLink":"", "quoteLink":"http://forismatic.com/en/aaa6789fa/"})'
