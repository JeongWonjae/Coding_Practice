#-*- coding:utf-8 -*-
import os
import time

source='"C:\\backup"'
target_dir='D:\\backup'
#os.sep=\
target=target_dir+os.sep+time.strftime('%Y_%m%d_%H%M%S')+'.zip'
if not os.path.exists(target_dir): os.mkdir(target_dir)
zip_command=f"zip -r {target} {source}"
print("Zip command is : ")
print(zip_command)
print("Running:")
os.system(zip_command)
if os.system(zip_command)==0: print("Successful backup to ", target)
else: print("Backup Failed")
