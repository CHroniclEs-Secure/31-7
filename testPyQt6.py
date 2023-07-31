#Class rbabari - EMRivas
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel

# Étape 1: Créer(instancier) 1 objet app: type: QApplication
# qui provient de la librairie PyQt6
app = QApplication([])

# Étape 2: Créer un objet fenetre QWidget
fen = QWidget()
fen.setGeometry(20, 313, 1320, 200) #location, dimention
fen.setWindowTitle("Ma premiere Fenetre ^^,")

# Étape 5: ajout du Label
lbl1 = QLabel(fen)
lbl1.setText("On reprend avec la Foi en Dieu.")

# Étape 3: Rentrer la fenetre visible
fen.show()

# Étape 4: Execute l'application
app.exec()