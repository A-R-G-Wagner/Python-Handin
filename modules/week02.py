import argparse
import csv

def print_file_content(file):
    with open(file) as file_object:
        contents = file_object.read()

    print(contents)
def write_list_to_file(output_file, lst):
    with open(output_file, "w") as o:
        o.write(" ".join(lst) + "\n")
        
def write_strings_to_file(output_file, *str):
    for s in str:
        with open(output_file, "w") as o:
            o.write(" ".join(str) + "\n")
            
def write_to_file(output_file, lst):
        with open(output_file, "w") as o:
            for x in lst:
                for y in x:
                    o.write(x + "\n")
            
def read_csv(input_file):
    inputList = []
    with open(input_file) as o:
            reader = csv.reader(o)
            
            for row in reader:
                inputList.append(row)
            
    return inputList


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Solution to handin week 2')
    parser.add_argument('--file', nargs='*')
    #parser.add_argument('--help', 
    
    args = parser.parse_args()
   
    if not (args.file):
        print_file_content('files/week02_noFile.txt')
    else:
       # print_file_content(args.file)
        print_file_content("files/week02_input.txt")
    
       