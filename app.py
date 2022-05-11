import os
import sys
from pathlib import Path, PurePath, PureWindowsPath
import shutil

def menu():
    print('Chose option:')
    print('1. Extract files\n2. About\n3. Exit')
    choice=int(input())
    if(choice==1):
        extraction_as_path_objects()
    elif(choice==2):
        about()
    elif(choice==2):
        sys.exit(1)

def about():
    print('About')

def extraction():
    print('Which folder do you want to extract:')
    folder=input()
    print('What files do you want to extract?')
    files_to_extract=input()
    fileslist=[]
    files_list_as_path_objects=[]
    for root, dirs, files in os.walk(folder):
        print(f'this is root:{root}')
        for file in files:
            print(f'so the root is:{root}')
            fileslist.append(os.path.join(root,file))
            file_str=str(os.path.join(root,file))
            path_library_file=Path(file_str)
            print(path_library_file,type(path_library_file),'and the root is:',root)
            print(f'so the root is:{root}')

    for name in fileslist:
        print(name)

def extraction_as_path_objects():
    """Similar to extract function, but gives instead list of files as Path objects"""
    print('Which folder do you want to extract:')
    folder = input()
    print('What files do you want to extract?')
    files_to_extract = input()
    files_list_as_path_objects = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_string=str(os.path.join(root,file))
            file_as_path_object=Path(file_string)
            files_list_as_path_objects.append(file_as_path_object)
    for name in files_list_as_path_objects:
        save_files(str(name))
    return files_list_as_path_objects

def save_files(file, target_folder=Path('D:\Download\Assets\Materials\pictures')):
    if(not Path.exists(target_folder)):
        os.mkdir(target_folder)
    shutil.copy(file,target_folder)

