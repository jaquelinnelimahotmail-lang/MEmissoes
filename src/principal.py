import sys
from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtWidgets import QTableWidgetItem, QLineEdit 
from PyQt6.QtGui import QPixmap

from models.usuario import Usuario
from models.emissao import Emissao

from controllers.usuarioControl import UsuarioControl
from controllers.emissaoControl import EmissaoControl

class Principal(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_components()
        self.controle_usuarios = UsuarioControl()
        self.controle_emissoes = EmissaoControl()
        self.init_usuarios()
        self.__usuario_logado = ''
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
        self.pushButtonCadastrosLimpar.clicked.connect(self.limpar_form_emissao)
        self.pushButtonCadastrosDados.clicked.connect(self.acessar_dados)
        self.pushButtonCadastrosSair.clicked.connect(self.acessar_login)
        self.pushButtonCadastrosError.clicked.connect(lambda: self.frameCadastrosError.hide())

        # Componentes da tela Dados
        self.frameDadosError.hide()
        self.pushButtonDadosAlterar.clicked.connect(self.alterar_cadastro)
        self.pushButtonDadosExcluir.clicked.connect(self.excluir_cadastro)
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

    # METODOS DE LOGIN

    def init_usuarios(self):
        usuario_1 = Usuario()
        usuario_1.nome = 'Jaqueline'
        usuario_1.sobrenome = 'Lima'
        usuario_1.usuario = 'jaque'
        usuario_1.email = 'jaque@memissoes.com'
        usuario_1.senha_1 = '12345'
        usuario_1.senha_2 = '12345'
        self.controle_usuarios.add_usuario(usuario_1)

        usuario_2 = Usuario()
        usuario_2.nome = 'Luana'
        usuario_2.sobrenome = 'Silva'
        usuario_2.usuario = 'luana'
        usuario_2.email = 'luana@memissoes.com'
        usuario_2.senha_1 = '67890'
        usuario_2.senha_2 = '67890'
        self.controle_usuarios.add_usuario(usuario_2)

    def realizar_login(self):
        user = self.lineEditLoginUsuario.text()
        senha = self.lineEditLoginSenha.text()

        if self.controle_usuarios.validar_acesso(user, senha):
            self.lineEditLoginUsuario.clear()
            self.lineEditLoginSenha.clear()
            self.frameLoginError.hide()
            self.acessar_cadastros()
            self.__usuario_logado = user
            print('Login realizado com sucesso')
        else:
            self.labelLoginError.setText('Usuário ou Senha incorretos')
            self.labelLoginError.setStyleSheet(self.cor_erro)
            self.frameLoginError.show()

    # METODOS DE EMISSAO

    def salvar_cadastro(self):
        indice = self.tableWidget.currentRow()

        emissao = Emissao()
        emissao.local = self.lineEditCadastrosLocal.text()
        emissao.latitude = self.lineEditCadastrosLatitude.text()
        emissao.longitude = self.lineEditCadastrosLongitude.text()
        emissao.tipo_gas = self.lineEditCadastrosTipoDeGas.text()
        emissao.valor = self.lineEditCadastrosValor.text()
        emissao.unidade = self.lineEditCadastrosUnidade.text()
        emissao.limite = float(self.lineEditCadastrosLimite.text())
        if len(emissao.error) != 0:
            self.labelCadastrosError.setText(emissao.error)
            self.labelCadastrosError.setStyleSheet(self.cor_erro)
            self.frameCadastrosError.show()
        else:
            if indice >= 0:
                msg = self.controle_emissoes.alterar_emissao(indice, emissao)
                self.labelCadastrosError.setText(msg)
                self.labelCadastrosError.setStyleSheet(self.cor_sucesso)
                self.frameCadastrosError.show()
                self.tabelar_dados()
                self.limpar_form_emissao()
                self.tableWidget.clearSelection()
            else:
                msg = self.controle_emissoes.add_emissao(emissao)
                self.labelCadastrosError.setText(msg)
                self.labelCadastrosError.setStyleSheet(self.cor_sucesso)
                self.tabelar_dados()
                self.limpar_form_emissao()

    def tabelar_dados(self) -> None:
        count_linhas = 0
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(self.controle_emissoes.lista_emissoes))
        for emissao in self.controle_emissoes.lista_emissoes:
            self.tableWidget.setItem(count_linhas, 0, QTableWidgetItem(self.usuario_logado))
            self.tableWidget.setItem(count_linhas, 1, QTableWidgetItem(emissao.local))
            self.tableWidget.setItem(count_linhas, 2, QTableWidgetItem(emissao.latitude))
            self.tableWidget.setItem(count_linhas, 3, QTableWidgetItem(emissao.longitude))
            self.tableWidget.setItem(count_linhas, 4, QTableWidgetItem(emissao.tipo_gas))
            self.tableWidget.setItem(count_linhas, 5, QTableWidgetItem(emissao.valor))
            self.tableWidget.setItem(count_linhas, 6, QTableWidgetItem(emissao.unidade))
            self.tableWidget.setItem(count_linhas, 7, QTableWidgetItem(str(emissao.limite)))
            count_linhas += 1

    def alterar_cadastro(self):
        indice = self.tableWidget.currentRow()
        if indice >= 0:
            emissao = self.controle_emissoes.acessar_emissao(indice)
            self.lineEditCadastrosLocal.setText(emissao.local)
            self.lineEditCadastrosLatitude.setText(emissao.latitude)
            self.lineEditCadastrosLongitude.setText(emissao.longitude)
            self.lineEditCadastrosTipoDeGas.setText(emissao.tipo_gas)
            self.lineEditCadastrosValor.setText(emissao.valor)
            self.lineEditCadastrosUnidade.setText(emissao.unidade)
            self.lineEditCadastrosLimite.setText(str(emissao.limite))
            self.acessar_cadastros()
        else:
            msg = 'Erro: selecione o cadastro de emissão que deseja alterar'
            self.labelDadosError.setText(msg)
            self.labelDadosError.setStyleSheet(self.cor_erro)
            self.frameDadosError.show()

    def excluir_cadastro(self):
        indice = self.tableWidget.currentRow()
        if indice >= 0:
            msg = self.controle_emissoes.excluir_emissao(indice)
            self.labelDadosError.setText(msg)
            self.labelDadosError.setStyleSheet(self.cor_sucesso)
            self.labelDadosError.show()
            self.tabelar_dados()
        else:
            msg = 'Erro: selecione o cadastro que deseja excluir'
            self.labelDadosError.setText(msg)
            self.labelDadosError.setStyleSheet(self.cor_erro)
            self.frameDadosError.show()

    def limpar_form_emissao(self):
        componentes = [
            self.lineEditCadastrosLocal,
            self.lineEditCadastrosLatitude,
            self.lineEditCadastrosLongitude,
            self.lineEditCadastrosTipoDeGas,
            self.lineEditCadastrosValor,
            self.lineEditCadastrosUnidade,
            self.lineEditCadastrosLimite
        ]
        self.__limpar_componentes(componentes)

    # METODOS DE USUARIO

    def cadastrar_usuario(self):
        usuario = Usuario()
        usuario.nome = self.lineEditCadUsuariosNome.text()
        usuario.sobrenome = self.lineEditCadUsuariosNome.text()
        usuario.usuario = self.lineEditCadUsuariosUser.text()
        usuario.email = self.lineEditCadUsuariosEmail.text()
        usuario.senha_1 = self.lineEditCadUsuariosSenha01.text()
        usuario.senha_2 = self.lineEditCadUsuariosSenha02.text()
        if len(usuario.error) != 0:
            self.labelCadUsuarioError.setText(usuario.error)
            self.labelCadUsuarioError.setStyleSheet(self.cor_erro)
            self.frameCadUsuarioError.show()
        else:
            if self.controle_usuarios.verificar_user(usuario.nome):
                msg = 'Erro: nome de usuário já registrado'
                self.labelCadUsuarioError.setText(msg)
                self.labelCadUsuarioError.setStyleSheet(self.cor_erro)
                self.frameCadUsuarioError.show()
            else:
                msg = self.controle_usuarios.add_usuario(usuario)
                self.labelCadUsuarioError.setText(msg)
                self.labelCadUsuarioError.setStyleSheet(self.cor_sucesso)
                self.frameCadUsuarioError.show()
                self.limpar_form_cadastro()

    def recuperacao_senha(self):
        pass

    def limpar_form_cadastro(self):
        componentes = [
            self.lineEditCadUsuariosNome,
            self.lineEditCadUsuariosNome,
            self.lineEditCadUsuariosUser,
            self.lineEditCadUsuariosEmail,
            self.lineEditCadUsuariosSenha01,
            self.lineEditCadUsuariosSenha02
        ]
        self.__limpar_componentes(componentes)

    # METODOS DIVERSOS

    # NAVEGACAO
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

    def sair(self):
        self.limpar_form_emissao()
        self.limpar_form_cadastro()
        self.tableWidget.clearContents()
        self.frameLoginError.hide()
        self.frameCadastrosError.hide()
        self.frameDadosError.hide()
        self.frameCadUsuarioError.hide()
        self.frameRecuperacaoError.hide()
        self.acessar_login()

    # LIMPEZA
    def __limpar_componentes(self, componentes:list) -> None:
        for componente in componentes:
            if isinstance(componente, QLineEdit):
                componente.clear()

    # ENCAPSULAMENTO

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self, user):
        if len(user) != 0:
            self.__usuario_logado = user
        else:
            print('O campo usuário não pode ser vazio')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
