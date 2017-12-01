import io
import os

def checkCharacter(str):
 str1=str2=str3=''
 if(len(str) <= 60):
    str1 = str
 elif(len(str) > 60 and len(str) <= 120):
  #print(len(str))
  str1=str[0:59]
  i=str1.rfind(' ')
  str1 =str[0:i]
  str2 = str[i+1:]
 elif(len(str) > 120 and len(str) <= 180):
  #print(len(str))
  str1=str[0:59]
  i=str1.rfind(' ')
  str1 =str[0:i]
  str = str[i+1:]
  str2=str[0:59]
  i=str2.rfind(' ')
  str2 =str[0:i]
  #print(str2)
  str3 = str[i+1:]

 print('str1 -'+str1)
 print('str2-'+str2)
 print('str3-'+str3)



checkCharacter('Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullam')
