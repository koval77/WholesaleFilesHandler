from pathlib import Path
from os import chdir
import os
import shutil

path=Path('..')

print(f'now u are in:{path.cwd()}')

chdir(path)

print(f'now u are in:{path.cwd()}')

#path=Path('C:\\Users\Wojtek\OneDrive\Desktop\fonts')
#myglob=path.glob()
#print(myglob)
#ob1=path.iterdir()
#print(type(ob1))
#ar1=list(ob1)
#print(ar1)
mypath=Path('C:\\Users\Wojtek\OneDrive\Desktop\myfonts')
p1=path.home()/'OneDrive\Desktop\\fonts'
l1=list(mypath.iterdir())
print(l1)
chdir('C:\\Users\Wojtek\OneDrive\Desktop\myfonts')
print(f'now u are in:{path.cwd()}')
print(f"curent dir from os:{os.getcwd()}")
#p=os.getcwd()
for file in l1:
    os.popen(f'tar -xf {file}')
os.popen('tar -xf bukkumi.zip')
