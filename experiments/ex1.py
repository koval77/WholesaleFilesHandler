import sys
from PySide6.QtWidgets import QApplication,QWidget, QVBoxLayout, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("moja apka experymrenytlna")
        layout=QVBoxLayout()

        button=QPushButton("to ja, press me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        btn2=QPushButton("a to ja, press me!!!")
        btn2.clicked.connect(self.btn2signal)
        btn2.setCheckable(False)
        btn3=QPushButton("make btn2 checkable on/off")
        btn3.clicked.connect(self.btn2_cheable_toggle)
        # self.setCentralWidget(button)
        # self.setCentralWidget(btn2)
        layout.addWidget(button)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        central_widget=QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def btn2_cheable_toggle(self):
        self.btn2.setCheckable(True)



    def the_button_was_clicked(self):
        print("Clicked!")

    def btn2signal(self):
        print("oh, thank you!")

# help(QMainWindow)
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()