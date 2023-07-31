#Class rbabari - EMRivas

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel

# Étape 7: On definit l'action des boutons.
def action1():
    print("On continue.")

def action2():
    print("On recomence.")


# Étape 1: Créer(instancier) 1 objet app: type: QApplication
# qui provient de la librairie PyQt6
app = QApplication([])

# Étape 2: Créer un objet fenetre QWidget
fen = QWidget()
fen.setGeometry(20, 313, 1320, 200) #location, dimention
fen.setWindowTitle("Ma premiere Fenetre ^^,")

# Étape 5: ajout du Label
lbl1 = QLabel(fen) #contenu de la fenetre
lbl1.setText("On reprend avec la Foi en Dieu."
             "-------------------------------"
             "On étudie avec beaucoup d'effort"
             "--------------------------------")

# Étape 6: ajout bouton.
btn1 = QPushButton(fen)
btn1.setText("...Continuer...")
btn1.setGeometry(20, 30, 200, 25)
btn1.clicked.connect(action1)

btn2 = QPushButton(fen)
btn2.setText(". Recomencer...")
btn2.setGeometry(40, 60, 200, 25)
btn2.clicked.connect(action2)

# Étape 3: Rentrer la fenetre visible
fen.show()

# Étape 4: Execute l'application
app.exec()