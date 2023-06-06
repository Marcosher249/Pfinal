import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import firebase_admin
from firebase_admin import credentials, firestore, auth
from Pfinal import MainWindow

# Configuración de Firebase
cred = credentials.Certificate('bottrade-8153d-firebase-adminsdk-uhun7-3593f323d3.json')  
firebase_admin.initialize_app(cred)
db = firestore.client()

class LoginRegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login / Registro")
        self.setGeometry(100, 100, 900, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Campos de correo y contraseña
        self.email_field = QLineEdit()
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)

        # Botones de login y registro
        login_button = QPushButton("Iniciar sesión")
        login_button.clicked.connect(self.login)
        register_button = QPushButton("Registrarse")
        register_button.clicked.connect(self.register)

        # Agregar widgets al diseño
        layout.addWidget(QLabel("Correo electrónico:"))
        layout.addWidget(self.email_field)
        layout.addWidget(QLabel("Contraseña:"))
        layout.addWidget(self.password_field)
        layout.addWidget(login_button)
        layout.addWidget(register_button)

    def login(self):
        email = self.email_field.text()
        password = self.password_field.text()

        try:
            user = auth.get_user_by_email(email)
            print("Inicio de sesión exitoso. ID de usuario:", user.uid)

            # Mostrar la ventana MainWindow
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        except Exception as e:
            print("Error al iniciar sesión:", str(e))

    def register(self):
        email = self.email_field.text()
        password = self.password_field.text()

        # Registrar un nuevo usuario en Firebase
        try:
            user = auth.create_user(email=email, password=password)
            print("Registro exitoso. ID de usuario:", user.uid)
        except Exception as e:
            print("Error al registrar usuario:", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginRegisterWindow()
    window.show()
    sys.exit(app.exec_())