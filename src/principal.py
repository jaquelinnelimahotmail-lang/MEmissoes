import sys
from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPixmap, QIcon

from models.usuario import Usuario

from controllers.usuarioControl import UsuarioControl

class Principal(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self) 
        self.init_components()
        self.controle_usuarios = UsuarioControl()
        self.init_usuarios()
        self.cor_sucesso = 'background-color: rgb(101, 184, 145)'
        self.cor_erro = 'background-color: rgb(204, 41, 54); color: rgb(255, 255, 255)'

    def init_components(self):

        # Componentes da tela de Login
        self.frameLoginError.hide()
        self.labelLoginImagem.setPixmap(QPixmap('src/img/icon'))
        self.pushButtonLoginConectar.clicked.connect(self.realizar_login)
        self.pushButtonLoginCriarConta.clicked.connect(self.acessar_cad_usuario)
        self.pushButtonLoginEsqSenha.clicked.connect(self.acessar_recuperacao)
        self.pushButtonLoginError.clicked.connect(lambda: self.frameLoginError.hide())

        # Componentes da tela Cadastro de Emissões
        self.frameCadastrosError.hide()
        self.pushButtonCadastrosSalvar.clicked.connect(self.salvar_cadastro)
        self.pushButtonCadastrosExcluir.clicked.connect(self.excluir_cadastro)
        #self.pushButtonCadastrosLimpar.clicked.connect()
        self.pushButtonCadastrosDados.clicked.connect(self.acessar_dados)
        self.pushButtonCadastrosSair.clicked.connect(self.acessar_login)
        self.pushButtonCadastrosError.clicked.connect(lambda: self.frameCadastrosError.hide())

        # Componentes da tela Dados
        self.frameDadosError.hide()
        self.pushButtonDadosAlterar.clicked.connect(self.alterar_cadastro)
        self.pushButtonDadosExcluir.clicked.connect(self.excluir_cadastro_dados)
        self.pushButtonDadosVoltar.clicked.connect(self.acessar_cadastros)
        self.pushButtonDadosSair.clicked.connect(self.acessar_login)
        self.pushButtonDadosError.clicked.connect(lambda: self.frameDadosError.hide())

        # Componentes da tela Cadastro de Usuarios
        self.frameCadUsuarioError.hide()
        self.pushButtonCadUsuariosCadastrar.clicked.connect(self.cadastrar_usuario)
        self.pushButtonCadUsuariosVoltar.clicked.connect(self.acessar_login)
        self.pushButtonCadUsuarioError.clicked.connect(lambda: self.frameCadUsuarioError.hide())

        # Componentes da tela Recuperação
        self.frameRecuperacaoError.hide()
        self.pushButtonRecuperacaoSalvar.clicked.connect(self.recuperacao_senha)
        self.pushButtonRecuperacaoVoltar.clicked.connect(self.acessar_login)
        self.pushButtonRecuperacaoError.clicked.connect(lambda: self.frameRecuperacaoError.hide())

    def init_usuarios(self):
        usuario_1 = Usuario()
        usuario_1.nome = 'Jaqueline'
        usuario_1.sobrenome = 'Lima'
        usuario_1.user = 'jaque'
        usuario_1.email = 'jaque@memissoes.com'
        usuario_1.senha_1 = '12345'
        usuario_1.senha_2 = '12345'
        self.controle_usuarios.add_usuario(usuario_1)

        usuario_2 = Usuario()
        usuario_2.nome = 'Luana'
        usuario_2.sobrenome = 'Silva'
        usuario_2.user = 'luana'
        usuario_2.email = 'luana@memissoes.com'
        usuario_2.senha_1 = '67890'
        usuario_2.senha_2 = '67890'
        self.controle_usuarios.add_usuario(usuario_2)

    # Métodos da Classe
    def realizar_login(self):
        pass

    def salvar_cadastro(self):
        pass

    def excluir_cadastro(self):
        pass

    def alterar_cadastro(self):
        pass

    def excluir_cadastro_dados(self):
        pass

    def cadastrar_usuario(self):
        pass

    def recuperacao_senha(self):
        pass

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
    
    # Métodos de Navegação
    def acessar_login(self):
        self.stackedWidget.setCurrentWidget(self.pageLogin)

    def acessar_cadastros(self):
        self.stackedWidget.setCurrentWidget(self.pageCadastros)
    
    def acessar_dados(self):
        self.stackedWidget.setCurrentWidget(self.pageDados)

    def acessar_cad_usuario(self):
        self.stackedWidget.setCurrentWidget(self.pageCadUsuario)
    
    def acessar_recuperacao(self):
        self.stackedWidget.setCurrentWidget(self.pageRecuperacao)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
