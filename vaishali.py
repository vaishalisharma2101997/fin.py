#!/usr/bin/python
import os
import commands
x=raw_input('Enter the directory name')
y=raw_input('Enter the file name')
t,r=commands.getstatusoutput('find / -type d -name {}'.format(x))
#commands.getstatusoutput('sudo echo 'os.system('find / -type d -name vaish')' >>/root/Desktop/try.py')
#os.system('python try.py')
#os.system("sudo chmod 777 /root/Desktop/{}".format(x))
if os.path.isdir(x):
	os.system("sudo touch {}/{}".format(r,y)) 
else:
	os.system("sudo mkdir /root/Desktop/{}".format(x))
	os.system("sudo touch /root/Desktop/{}/{}".format(x,y))
	
        

