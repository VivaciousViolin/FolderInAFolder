
import time
import os

#directory
directory = "Homework"
 
#parent directory path
parent_dir = "D:/Homework/"

file_number = 1

def make_and_add_path():
    global parent_dir
    
    # Path
    path = os.path.join(parent_dir, directory)
    
    #make the directory
    os.mkdir(path)
    print("Directory in " + path + " created")
    
    #add path and print name
    #add path
    extra_file_path = "Homework/"
    parent_dir += extra_file_path
    
    #file number
    global file_number
    file_add = 1
    file_number += file_add
    
    #print
    print(parent_dir)
    print(file_number)
    return file_number
    return parent_dir
    


for loop in range(10000):
    make_and_add_path()

time.sleep(5)

