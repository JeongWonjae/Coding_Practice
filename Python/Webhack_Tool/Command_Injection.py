#_*_ coding:utf-8 _*_
import subprocess

print('Send ping a device')
wrd=input("Enter your IP address : ")
string=subprocess.call(f"ping {wrd}", shell=True)
print(string)

