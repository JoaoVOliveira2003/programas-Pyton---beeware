# CREATE TABLE pessoas (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nome VARCHAR(100) NOT NULL,
#     data_nascimento VARCHAR(100),
#     endereco VARCHAR(255),
#     telefone VARCHAR(20)
# );
# select * from pessoas;

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import mysql.connector


class BeeWare1(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Campo ID (para update/delete)
        id_label = toga.Label("ID (caso queira apagar ou atualizar): ", style=Pack(margin=(0, 5)))
        self.id_input = toga.TextInput(style=Pack(flex=1))
        id_box = toga.Box(style=Pack(direction=ROW, margin=5))
        id_box.add(id_label)
        id_box.add(self.id_input)

        linha = toga.Box(style=Pack(height=1, background_color='gray', margin_top=10, margin_bottom=10))

        # Campo Nome
        nome_label = toga.Label("Nome: ", style=Pack(margin=(0, 5)))
        self.nome_input = toga.TextInput(style=Pack(flex=1))
        nome_box = toga.Box(style=Pack(direction=ROW, margin=5))
        nome_box.add(nome_label)
        nome_box.add(self.nome_input)

        # Campo Data de Nascimento
        data_label = toga.Label("Data de nascimento:", style=Pack(margin=(0, 5)))
        self.data_input = toga.TextInput(placeholder="dd/mm/aaaa", style=Pack(flex=1))
        box_data = toga.Box(style=Pack(direction=ROW, margin=5))
        box_data.add(data_label)
        box_data.add(self.data_input)

        # Campo Endereço
        endereco_label = toga.Label("Endereço:", style=Pack(margin=(0, 5)))
        self.endereco_input = toga.TextInput(placeholder="", style=Pack(flex=1))
        box_endereco = toga.Box(style=Pack(direction=ROW, margin=5))
        box_endereco.add(endereco_label)
        box_endereco.add(self.endereco_input)

        # Campo Telefone
        telefone_label = toga.Label("Telefone:", style=Pack(margin=(0, 5)))
        self.telefone_input = toga.TextInput(placeholder="(xx) xxxx-xxxx", style=Pack(flex=1))
        box_telefone = toga.Box(style=Pack(direction=ROW, margin=5))
        box_telefone.add(telefone_label)
        box_telefone.add(self.telefone_input)

        linha = toga.Box(style=Pack(height=1, background_color='gray', margin_top=10, margin_bottom=10))

        button_inserir = toga.Button("Inserir", on_press=self.inserir_dados, style=Pack(margin=5))
        button_atualizar = toga.Button("Atualizar", on_press=self.atualizar_dados, style=Pack(margin=5))
        button_deletar = toga.Button("Deletar", on_press=self.deletar_dados, style=Pack(margin=5))

        botoes_box = toga.Box(style=Pack(direction=ROW, margin=5))
        botoes_box.add(button_inserir)
        botoes_box.add(button_atualizar)
        botoes_box.add(button_deletar)

        # Layout principal
        main_box.add(id_box)
        main_box.add(nome_box)
        main_box.add(box_data)
        main_box.add(box_endereco)
        main_box.add(box_telefone)
        main_box.add(linha)
        main_box.add(botoes_box)

        self.main_window = toga.MainWindow(title="App com Insert, Update e Delete")
        self.main_window.content = main_box
        self.main_window.show()

    def conectar_banco(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tcc"
        )

    def limpar_campos(self):
        self.id_input.value = ""
        self.nome_input.value = ""
        self.data_input.value = ""
        self.endereco_input.value = ""
        self.telefone_input.value = ""

    def inserir_dados(self, widget):
        try:
            conn = self.conectar_banco()
            cursor = conn.cursor()
            sql = "INSERT INTO pessoas (nome, data_nascimento, endereco, telefone) VALUES (%s, %s, %s, %s)"
            valores = (
                self.nome_input.value,
                self.data_input.value,
                self.endereco_input.value,
                self.telefone_input.value
            )
            cursor.execute(sql, valores)
            conn.commit()
            print(" Registro inserido com sucesso.")
            self.limpar_campos()
        except mysql.connector.Error as e:
            print("Erro ao inserir:", e)

    def atualizar_dados(self, widget):
        try:
            conn = self.conectar_banco()
            cursor = conn.cursor()
            sql = "UPDATE pessoas SET nome=%s, data_nascimento=%s, endereco=%s, telefone=%s WHERE id=%s"
            valores = (
                self.nome_input.value,
                self.data_input.value,
                self.endereco_input.value,
                self.telefone_input.value,
                self.id_input.value
            )
            cursor.execute(sql, valores)
            conn.commit()
            print("Registro atualizado com sucesso.")
            self.limpar_campos()
        except mysql.connector.Error as e:
            print("Erro ao atualizar:", e)

    def deletar_dados(self, widget):
        try:
            conn = self.conectar_banco()
            cursor = conn.cursor()
            sql = "DELETE FROM pessoas WHERE id=%s"
            cursor.execute(sql, (self.id_input.value,))
            conn.commit()
            print("Registro deletado com sucesso.")
            self.limpar_campos()
        except mysql.connector.Error as e:
            print("Erro ao deletar:", e)


def main():
    return BeeWare1()
