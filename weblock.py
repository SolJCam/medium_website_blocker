#Import Libraries
import time
from datetime import datetime as dt

#Path to host file
#(host file: can be used to map hostnames to IP addresses(redirect websites or block them by pointing them to localhost))
host_path = "./hosts"

#Redirect to local host
redirect = "127.0.0.1"

#Websites to block
website_list = ["www.netflix.com", "www.facebook.com"]

#Condition
while True:
    #Check for the current time
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Rihanna")
        #Open file and read the content; also "file" is not a python keyword but rather an object returned by open(). Removed from python3?
        file = open(host_path, "r+")
        content = file.read()
        for website in website_list:
            if website in content:
                pass #used when a statement is required syntactically but you do not want any command or code to execute.
            else:
                #Write the ip of localhost and name of the websie to block
                file.write(redirect + " " + website + "\n")
    else:
        print("Drake")
        #Open hosts file and read content from it- line by line
        file = open(host_path, "r+")
        content = file.readlines()
        #Take back pointer to starting of the file from the end of file
        file.seek(0)
        for line in content:
            if not(website in line for website in website_list):
                file.write(line)
            # truncates the file's size by removing either the top or end empty lines
            file.truncate()
    time.sleep(5)


# Project url
# https://towardsdatascience.com/master-python-through-building-real-world-applications-part-3-17d08eda58e