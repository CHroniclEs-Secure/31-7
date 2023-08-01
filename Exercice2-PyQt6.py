# Class Babari - EMRivas
# Creer un calculatrice
# besoin 12 boutons
#        -> bouton de 0 à 9
#        -> bouton + et -
# les boutons doivent être dans une liste

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
def Plus():
    num = int(lblNum.text())
    num = num + 1
    lblNum.setText(str(num))


def Moins():
    num = int(lblNum.text())
    num = num - 1
    lblNum.setText(str(num))


#Body
app = QApplication([])
fen = QWidget()
fen.setGeometry(250, 130, 500, 500)

# QLabel
lblNum = QLabel(fen)
lblNum.setText("0")
lblNum.setGeometry(135, 20, 75, 40)

#btnZero
btnZero = QPushButton(fen)
btnZero.setText("0")
btnZero.setGeometry(200, 350, 75, 90)
btnZero.clicked.connect(Plus)

#btnOne
btnOne = QPushButton(fen)
btnOne.setText("1")
btnOne.setGeometry(50, 50, 75, 90)
btnOne.clicked.connect(Plus)

#btnTwo
btnTwo = QPushButton(fen)
btnTwo.setText("2")
btnTwo.setGeometry(200, 50, 75, 90)
btnTwo.clicked.connect(Plus)

#btnThree
btnThree = QPushButton(fen)
btnThree.setText("3")
btnThree.setGeometry(350, 50, 75, 90)
btnThree.clicked.connect(Plus)

#btnFour
btnFour = QPushButton(fen)
btnFour.setText("4")
btnFour.setGeometry(50, 150, 75, 90)
btnFour.clicked.connect(Plus)

#btnFive
btnFive = QPushButton(fen)
btnFive.setText("5")
btnFive.setGeometry(200, 150, 75, 90)
btnFive.clicked.connect(Plus)

#btnSix
btnSix = QPushButton(fen)
btnSix.setText("6")
btnSix.setGeometry(350, 150, 75, 90)
btnSix.clicked.connect(Plus)

#btnSeven
btnSeven = QPushButton(fen)
btnSeven.setText("7")
btnSeven.setGeometry(50, 250, 75, 90)
btnSeven.clicked.connect(Plus)

#btnEight
btnEight = QPushButton(fen)
btnEight.setText("8")
btnEight.setGeometry(200, 250, 75, 90)
btnEight.clicked.connect(Plus)

#btnNine
btnNine = QPushButton(fen)
btnNine.setText("9")
btnNine.setGeometry(350, 250, 75, 90)
btnNine.clicked.connect(Plus)

# btnPlus
btnPlus = QPushButton(fen)
btnPlus.setText("Plus (+)")
btnPlus.setGeometry(50, 350, 75, 90)
btnPlus.clicked.connect(Plus)

# btnMoins
btnMoins = QPushButton(fen)
btnMoins.setText("Moins (-)")
btnMoins.setGeometry(350, 350, 75, 90) #x, y
btnMoins.clicked.connect(Moins)

fen.show()
app.exec()