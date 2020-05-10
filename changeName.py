

"""This program is to convert normal named 
files to jekyll minima format i.e `YYYY-MM-DD-name-of-the-file.extention` . This uses python3 so it will be easily available as a standalone file.
Future plan is add it to github actions. So files will be renamed automatically"""


import os  # os helps to list and change directories
import datetime  # datetime helps to get current date and time from system
import shutil

# first check for three available directories _posts,_word,_notebooks
root_folder = "."  # define the root of the directory

file_list = os.listdir('.')

folder_list = ["_posts", "_word", "_notebooks"]

file_format = {"_posts": ".md", "_word": ".docx", "_notebooks": ".ipynb"}


#choose only 3 folders in all the 
available_folders = list(set(file_list).intersection(set(folder_list)))  # incase if someone delete one or more folders

# array to add the known directories



def rename_files(x):
	name_of_files = os.listdir(x)
	print("entering into "+ x)
	print("files in " + x)# remove this file so it won't get renamed
	print(name_of_files)
	name_of_files.remove("README.md")
	print("readme removed")
	for single_file in name_of_files:
		path = os.path.join(os.getcwd(),x)
		file_name = os.path.abspath(single_file) # to get extention of files in a folder
		file_name,file_extention = os.path.splitext(file_name)
		if(file_format[x] == file_extention): #make sure not to convert other formats like images 
			if not (single_file[0:4].isdigit()):  # minima looks for posts with year , # we change normal format to minima format
				print("changeing file name", single_file)
				date_to_add = datetime.date.today().strftime("%Y-%m-%d-")

				split_file_name = single_file.split(" ")  # split using only spaces

				new_file_name = "-".join(split_file_name)
				# no need for extention , it will be automatically added in the last element of split_file_name

				final_file_name = date_to_add + new_file_name
				# rename the file
				# file_path = os.getcwd()+"/"
				single_file = os.path.join(path,single_file)
				print(single_file)
				final_file_name = os.path.join(path,final_file_name)
				print(final_file_name)
				shutil.move(single_file,final_file_name)
				print("file rename to " + final_file_name)


for x in available_folders:
    rename_files(x)