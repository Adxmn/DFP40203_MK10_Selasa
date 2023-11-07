import glob
import os

def rename():

    old_file_name = input("Enter the old file name (including path): ")
    new_file_name = input("Enter the new file name (including path):")

    if os.path.exists(old_file_name):
        os.rename(old_file_name, new_file_name)
        print(f"File '{old_file_name}' has been renamed to '{new_file_name}'.")
    else:
        print(f"File '{old_file_name}' does not exist.")

def main():
    filelist = glob.glob("../DFP40203_MK10_Selasa/*.txt")
    for filename in filelist:
        print(filename)

    rename()

if __name__ == '__main__':
    main()

