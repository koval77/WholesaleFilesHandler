# This is a sample Python script.
from PyQt5.QtWidgets import QWidget,QFontComboBox, QComboBox, QRadioButton, QLineEdit, QPushButton,QMessageBox, QGraphicsEffect, QStylePainter, QApplication,QFrame, QBoxLayout,QLabel,QFileDialog
from PyQt5.QtCore import QDateTime
import pathlib
from PyQt5.QtGui import QPainter
import os
import sys
from os.path import join,getsize
from pathlib import Path
from PyQt5.QtGui import QIcon
import glob
import shutil
from app import menu


#todo Make icon in photoshop

p=Path('d:\\Download\\Assets\\Materials')
subdirs=[x for x in p.iterdir()]
print(f'Length of subdir(1): {len(subdirs)}')
print(f'Subdirectories: {subdirs}')
subdirs2=[y for y in p.glob('*')]
print('*'*100)
print(f'Length of globs:{len(subdirs2)}')
print(f'Globs: {subdirs2}')
subdirs3=[z for z in p.rglob('*')]
print(f'Length of rglob is: {len(subdirs3)}')
print(f'Rglob content is: {subdirs3}')

def print_dir_content(content_list):
    print(f'So inside of this ({[name for name in globals() if globals()[name] is content_list]})')

print('???'*100)
print(globals())
print(f'Length of globals is: {len(globals())}')
print('???'*100)
print(type(globals()))
print_dir_content(subdirs3)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
service=os.environ.get('K_SERVICE','Unknown service')
revision=os.environ.get("K_REVISION",'Unknown service')
print(f'service:{service}, \nrevision:{revision}')

# print(help(pathlib))
# print(help(os))
for root, dirs, files in os.walk('d:\\Download\\Assets\\Materials'):
            print(root, "consumes", end=" ")
            print(sum(getsize(join(root, name)) for name in files), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def make_list_of_all_files_in_folder(folder):
    print('*',*100)
    for file_name in glob.glob('*.txt'):
        new_path=os.path.join('archive',file_name)
        shutil.move(file_name,new_path)

print('Hello')
print('world')

def main():
    menu()
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(600, 400)
    w.move(300, 300)
    w.setGeometry(100,100,600,800)
    w.setWindowTitle('Wholesale Files Manager')
    label1=QLabel(w)
    label1.setText("Choose your option")
    label1.move(100,130)
    label1.show()
    for i in range(4):
        [k for k in locals().items()]
        # print(k)
    btn1=QPushButton(w)
    btn1.setText("Beheld")
    btn1.move(110,150)
    btn1.show()
    btn1.clicked.connect(dialog)
    btn2=QPushButton(w)
    btn2.setText("Unpack nested files")
    btn2.move(230,150)
    btn2.show()
    btn2.clicked.connect(nested_files_window)
    label2=QLabel(w)
    label2.setText("Your options:")
    label2.show()
    edit1=QLineEdit(w)
    # edit1.show()
    rad=QRadioButton(w)
    rad.setText("Use admin credentials?")
    rad.show()
    drop=QComboBox(w)
    drop.addItems(["Option 1","Option 2","Option 3","Exit"])


    w.show()
    sys.exit(app.exec_())


def dialog():
    mbox = QMessageBox()
    mbox.setText("Hello, enjoy using this application.")
    mbox.setDetailedText("Check help if you have any problems.")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox.exec_()

def nested_files_window(folder='empty'):
    nested_files_box=QMessageBox()
    nested_files_box.setText("Nested files")
    nested_files_box.setDetailedText(f"Those are all the files that are descendant from {folder}")
    # nested_files_box.setStandardButtons(QMessageBox.Accepted)
    nested_files_box.exec_()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
