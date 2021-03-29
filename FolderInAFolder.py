
import time
import os

#directory
directory = "Homework"
 
#parent directory path
parent_dir = "D:/Homework/"
    
def define_and_make_directory(directory, parent_dir):
    # Path
    path = os.path.join(parent_dir, directory)
    
    #make the directory
    os.mkdir(path)
    print("Directory in " + path + " created")
    
def edit_directory():
    # Using join()
    # adding one string to another
    edited_parent_dir = "".join((parent_dir, "Homework/"))
    print(edited_parent_dir)
    


define_and_make_directory(directory, parent_dir)
edit_directory()

print(parent_dir)
time.sleep(3)