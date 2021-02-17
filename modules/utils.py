import os
import re
import argparse

def get_file_names(folderpath,out):
    listOfFiles = os.listdir(folderpath)
    with open(out, "w") as o:
        for x in listOfFiles:
            o.write(x + "\n")

def get_all_file_names(folderpath,out):
    listOfFiles = os.listdir(folderpath)
    with open(out, "w") as o:
        for x in listOfFiles:
            if os.path.isdir(folderpath + "/" + x):
                o.write("Directory: " + x + "\n")
                subDir = os.listdir(folderpath + "/" + x)
                for xx in subDir:
                    o.write(" - " + xx + "\n")
            
            else:
                o.write(x + "\n")

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    pass

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    pass

def write_headlines(md_files, out):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    pass

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--fp', nargs='*')
        
    args = parser.parse_args()
   
    if not (args.file):
        print_file_content('files/week02_noFile.txt')
    else:
       # print_file_content(args.file)
        print_file_content("files/week02_input.txt")