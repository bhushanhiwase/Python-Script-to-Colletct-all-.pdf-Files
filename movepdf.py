# program to copy all the pdf files in the system in a directory

import subprocess
import time

subprocess.run("ls >> listshow.txt", shell = True)              # create a list of all the directories

lst = []
with open('listshow.txt', "r+") as file:
    for lines in file:
        data = file.readline()
        lst.append(data[0:-1])
    lst.append("/home/ubuntu")            # to get the files peresrnt at home location
    

while True:
    for item in lst:
        string = "cp " + item + "/*.pdf /home/ubuntu/destination"
        if "." not in item:		 # to consorder onlt the directory
    	    subprocess.run(string, shell = True)

    time.sleep(30)			#repeats the block after every 30 sec
