
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


make_and_add_path()
make_and_add_path()
make_and_add_path()
make_and_add_path()
make_and_add_path()
make_and_add_path()

time.sleep(5)


"""
#define D:/homework and make additional directory in it
def define_and_make_directory(directory, parent_dir):
    # Path
    path = os.path.join(parent_dir, directory)
    
    #make the directory
    os.mkdir(path)
    print("Directory in " + path + " created")
    
#add Homework/ to the end of D:/Homework/
def edit_directory():
    extra_file_path = "Homework/"
    global final_dir
    final_dir = parent_dir + extra_file_path
    print(final_dir + "1")


#make another directory with final_dir
def continuation(directory, final_dir):
    # Path
    path = os.path.join(final_dir, directory)
    
    #make the directory
    os.mkdir(path)
    print("Directory in " + path + " created")
    
    
define_and_make_directory(directory, parent_dir)
edit_directory()
continuation(directory, final_dir)



#make this step loop
#i = 1
#while i < 6:
  #print(i)
  #i += 1

"""
