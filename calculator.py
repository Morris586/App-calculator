from PyQt5.QtWidgets import  QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont 
import ast 
from sympy import sympify

class Calc_App(QWidget):
    def __init__(self):
        super().__init__()

    #App settings
        self.setWindowTitle("My Calculator")
        self.resize(250, 350)

        #What is required 
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Arial", 30))
        self.grid = QGridLayout()

        self.buttons = [
            '9', '8', '7', '/',
            '6', '5', '4', '*',
            '3', '2', '1', '+',
            '0', '.', '=', '-'
        ]
        
        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushbutton{font: 25px Comic Sans MS: padding: 10px:}")
            self.grid.addWidget(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton('Clear')
        self.delete = QPushButton('<')
        self.clear.setStyleSheet("QPushbutton{font: 25px Comic Sans MS: padding: 10px:}")
        self.delete.setStyleSheet("QPushbutton{font: 25px Comic Sans MS: padding: 10px:}")

        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        bottom_row = QHBoxLayout()
        bottom_row.addWidget(self.clear)
        bottom_row.addWidget(self.delete)
        master_layout.addLayout(bottom_row)
        master_layout.setContentsMargins(30, 30, 30, 30)
        

        self.setLayout(master_layout)
        
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)


       


    def button_click(self):
        button = app.sender()    #get the button that triggered the click
        text = button.text()      #get the text that is displayed on the button

        if text == '=':
            symbol = self.text_box.text()
            
            try:  #Parse and evaluate the mathematical expression safely
                res = sympify(symbol)
                self.text_box.setText(str(res))
            except Exception:
                self.text_box.setText('Error')

        elif text == 'Clear':  
            self.text_box.clear()

        elif text == '<':
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text) #for any other button append the button's text to the existing text in the text box

if __name__ in ("__main__"):
    app = QApplication([])
    main_window = Calc_App()
    main_window.setStyleSheet("QWidget{  background-color:#f0f0f8}")

    main_window.show()
    app.exec_()


        