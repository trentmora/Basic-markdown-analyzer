#Trent Mora
#ITS 211
# Mora_P5
# Project 5
from  FileStatus import FileStatus
from FileAnalysis import FileAnalysis
import os #to work with directories

#here we need to get information to define an instance of a object. 
#namely, we need to ask the user here, pass it to FileStatus, such as the file directory

# 1. Ask the user for the folder path
folderpath = input("Enter the folder path that contains your .md files: ")

try:
    # 2. Get a list of *names* of everything in that folder
    entries = os.listdir(folderpath) #listdir is a function lists a directory
    
    print("\nMarkdown files found in this folder:\n")

    md_files = [] #store a list of .md files

    # 3. Loop through them and filter for .md
    for name in entries:
        if name.endswith(".md"):   # only markdown files
            full_path = os.path.join(folderpath, name)  # filepath + filename
            #print(f"\n{full_path}\n")
            md_files.append(full_path)
    # after scanning, if no .md files are found:
    #raise exception!
    if len(md_files) == 0:
        raise Exception(f"No .md files were found in this folder:\n{folderpath}")
    else: #.md files exist, output what .md files we have, and print number of .md files
        #print(md_files)
        print(f"\nTotal number of .md files: {len(md_files)}\n")
        filestatus_list = [] #create a list to store file statuses
        for path in md_files: #for every path of each .md file
            status_obj = FileStatus(path) #create a corresponding status object
            filestatus_list.append(status_obj) #put the status objects in a list
        for obj in filestatus_list:
            obj.check_yaml()
            obj.check_howmanywords()
            obj.check_gpt()
        #create an analysis object 
        analysis = (FileAnalysis(filestatus_list))
        #ask FileAnalysis for summary stats
        yaml_count, gpt_count, total_words, orphaned_count = analysis.summary() 

        print("\n==== Summary ====")
        print("Total files:", len(analysis)) #lenth of analysis
        print("Files with YAML:", yaml_count)
        print("Files mentioning GPT:", gpt_count)
        print("Total words:", total_words) #>=3 letters
        print("Orphaned Notes: ", orphaned_count)
        analysis.write_report()
        print("Wrote report.txt")
except FileNotFoundError:
    print("Error: That folder does not exist.")
except PermissionError:
    print("Error: You don't have permission to read that folder.")
except Exception as e:
    print("Error:", e)

#print(f"The list of x objects: {filestatus_list}")
#===================================================================
'''     OLD TEST OUTPUT:

        print("\nCreated FileStatus objects for:")
        for obj in filestatus_list: #iterate through the list of file status objects
            print(obj.get_filepath()) #print the filepath of each individual .md file
            print(f"YAML Status: {obj.get_hasYAML()}") # interfaces with self.has_YAML @FileStatus.py
            print(f"GPT Status: {obj.get_hasGPT()}") # interfaces with self.has_GPT @FileStatus.py
            print(f"Word Count (>=3 letters): {obj.get_numOfWords()}")
'''
# =================== SAVE YOUR FILES EVERY TIME ========================== #