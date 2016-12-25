# A static website blocker application for blocking websites in local system
# Author: Prashant nair
# For Python Bootcamp Workshop
import time
from datetime import datetime as dt
#Using temporary file to test the code
host_temp = "hosts_tmp"
host_location = r"/etc/hosts"

# For Windows r"C:\Windows\System32\drivers\etc\hosts"

#list of websites to be blocked by local computer
website_list = ["www.facebook.com","facebook.com"]

#Ensure all blocked website present in list will be redirected to the localhost
redirect = "127.0.0.1"

# Loop until exited
# from datetime import datetime as dt
# dt.now() --> (year,month,date,hours,minutes,seconds,millisec)
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15):
        print("Working Hours")
        with open(host_temp,'r+') as file:
            content=file.read()
            #print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(host_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            # While reading the file the pointer goes to the EOF post which
            #all writes will append. So here we are ensuring the write to happen
            #from first location

            #We use readlines to get the list of all lines instead of chars
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Free Hours")

    time.sleep(2)
# To schedule the program in Windows, you can change the extension of the program
# file extension i.e. .py to .pyw. Try it and enjoy the code

# To schedule the program in Linux and Mac, sudo crontab -e
# @reboot python /home/prashant/pythoncodes/script1.py
# Save the file

# Further assignment for the code
# 1. Write a program that will detect the OS and based on OS figure out which
#    hosts file is to be edited.
