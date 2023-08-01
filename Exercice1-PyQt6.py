#Class Babari - EMRivas
# exercice - creer un bouton (+) qui augmente
# creer un bouton (-) qui decrese
# fork

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
fen.setGeometry(200, 200, 299, 200)

# QLabel
lblNum = QLabel(fen)
lblNum.setText("0")
lblNum.setGeometry(135, 25, 75, 40)

# btnPlus
btnPlus = QPushButton(fen)
btnPlus.setText("Plus (+)")
btnPlus.setGeometry(50, 50, 75, 90)
btnPlus.clicked.connect(Plus)

# btnMoins
btnMoins = QPushButton(fen)
btnMoins.setText("Plus (+)")
btnMoins.setGeometry(150, 50, 75, 90)
btnMoins.clicked.connect(Moins)

fen.show()
app.exec()