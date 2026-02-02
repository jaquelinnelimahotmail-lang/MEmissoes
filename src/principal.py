import sys
from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

from models.usuario import Usuario

from controllers.usuarioControl import UsuarioControl

class Principal(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self) 
        self.init_components()
        self.controle_usuarios = UsuarioControl()
        self.init_usuarios()

    def init_components(self):
        # Componentes da tela de login 
        self.label_erro.hide()
        self.stackedWidget.setCurrentWidget(self.page)  # Tela login
        self.pushButton_conectar.clicked.connect(self.realizar_login)
        self.pushButton_criar_conta.clicked.connect(self.ir_para_criar_conta)
        self.pushButton_esqueci_senha.clicked.connect(self.ir_para_esqueci_senha)
        #self.label_erro.setVisible(False)

        # Componetes tela de cadastro 
        self.pushButton_salvar_medicoes.clicked.connect(self.pushButton_salvar_medicoes)

        # Componetes tela de registros 
        self.pushButton_editar.clicked.connect(self.pushButton_salvar_medicoes)
        self.pushButton_sair.clicked.connect(self.pushButton_sair)
        self.pushButton_exportar.clicked.connect(self.pushButton_exportar)
        self.pushButton_salvar_medicoes.clicked.connect(self.pushButton_excluir)
        self.pushButton_excluir.clicked.connect(self.pushButton_excluir)

        # Componentes da tela criar usuario 
        self.pushButton_confirmar_conta.clicked.connect(self.pushButton_confirmar_conta)

        # Ccomponente da tela esqueceu a senha 
        self.pushButton_confirma_nova_senha.clicked.connect(self.pushButton_confirma_nova_senha)


        # ---------------- CONEXÕES ----------------
        self.pushButton_conectar.clicked.connect(self.realizar_login)
        self.pushButton_criar_conta.clicked.connect(self.ir_para_criar_conta)
        self.pushButton_esqueci_senha.clicked.connect(self.ir_para_esqueci_senha)

        #self.pushButton_2.clicked.connect(self.voltar_login)
        #self.pushButton_3.clicked.connect(self.voltar_login)

        self.pushButton_confirmar_conta.clicked.connect(self.criar_conta)
        self.pushButton_confirma_nova_senha.clicked.connect(self.redefinir_senha)

        # BOTÃO SAIR DA TELA DE REGISTRO (page_2)
        self.pushButton_sair.clicked.connect(self.sair_sistema)

    def init_usuarios(self):
        usuario_1 = Usuario()
        usuario_1.nome = 'jaque'
        usuario_1.email = 'jaque@memissoes.com'
        usuario_1.senha_1 = '12345'
        usuario_1.senha_2 = '12345'
        self.controle_usuarios.add_usuario(usuario_1)

        usuario_2 = Usuario()
        usuario_2.nome = 'luana'
        usuario_2.email = 'luana@memissoes.com'
        usuario_2.senha_1 = '67890'
        usuario_2.senha_2 = '67890'
        self.controle_usuarios.add_usuario(usuario_2)


    # ================= LOGIN =================
    def realizar_login(self):
        login = self.lineEdit_usuario.text()
        senha = self.lineEdit_senha.text()

        for usuario in self.usuario:
            if login == usuario['usuario'] and senha == usuario['senha']:
                self.stackedWidget.setCurrentWidget(self.page_2)
                self.label_erro.setVisible(False)
                return

        self.label_erro.setVisible(True)
        self.label_erro.setText("Login ou senha incorretos")


    # ================= CRIAR CONTA =================
    def criar_conta(self):
        nome = self.lineEdit_nome_usuario.text()
        senha = self.lineEdit_nova_senha.text()
        confirma = self.lineEdit_confirma_senha.text()

        if QMainWindow == "" or senha == "" or confirma == "":
            QMainWindow.warning(self, "Erro", "Preencha todos os campos.")
            return

        if senha != confirma:
            QMainWindow.warning(self, "Erro", "Senhas não coincidem.")
            return

        self.lista_usuario.apped({"usuario": nome, "senha": senha})

        QMainWindow.information(self, "Sucesso", "Conta criada com sucesso!")
        self.voltar_login()

    # ================= REDEFINIR SENHA =================
    def redefinir_senha(self):
        usuario_digitado = self.lineEdit_usuario.text()
        nova_senha = self.lineEdit_nova_senha.text()

        for usuario in self.lista_usuario:
            if usuario_digitado == usuario['usuario']:
                usuario['senha'] = nova_senha
                QMainWindow.information(self, "Sucesso", "Senha alterada com sucesso!")
                self.voltar_login()
                return

        QMainWindow.warning(self, "Erro", "Usuário não encontrado.")

    # ================= TROCAR TELAS =================
    def ir_para_criar_conta(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

    def ir_para_esqueci_senha(self):
        self.stackedWidget.setCurrentWidget(self.page_4)

    def voltar_login(self):
        self.stackedWidget.setCurrentWidget(self.page)

    # ================= SAIR =================
    def sair_sistema(self):
        resposta = QMainWindow.question(
            self,
            "Sair",
            "Deseja realmente sair?",
            QMainWindow.StandardButton.Yes | QMainWindow.StandardButton.No
        )

        if resposta == QMainWindow.StandardButton.Yes:
            self.lineEdit_usuario.clear()
            self.lineEdit_senha.clear()
            self.stackedWidget.setCurrentWidget(self.page)

    # ================= VISUALIZAR SENHA =================
    def visualizar_senha(self):
        if self.lineEdit_senha.echoMode() == QLineEdit.EchoMode.Password:
            self.lineEdit_senha.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEdit_senha.setEchoMode(QLineEdit.EchoMode.Password)
    # acesso 
    def acessar_cadastro(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
