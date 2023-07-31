#Class rbabari - EMRivas
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

# Étape 1: Créer(instancier) 1 objet app: type: QApplication
# qui provient de la librairie PyQt6
app = QApplication([])

# Étape 2: Créer un objet fenetre QWidget
fen = QWidget()

# Étape 3: Rentrer la fenetre visible
fen.show()

# Étape 4: Execute l'application
app.exec()