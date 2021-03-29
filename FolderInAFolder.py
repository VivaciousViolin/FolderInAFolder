
import time
import os

#directory
directory = "Homework"
 
#parent directory path
parent_dir = "D:/Homework/"


def make_and_add_path():
    global parent_dir
    # Path
    path = os.path.join(parent_dir, directory)
    
    #make the directory
    os.mkdir(path)
    print("Directory in " + path + " created")
    
    #add path
    extra_file_path = "Homework/"
    parent_dir += extra_file_path
    print(parent_dir)
    return parent_dir


for loop in range(10000):
    make_and_add_path()

time.sleep(5)

