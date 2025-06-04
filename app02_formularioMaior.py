import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class BeeWare1(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Campo Nome
        nome_label = toga.Label("Nome: ", style=Pack(padding=(0, 5)))
        self.nome_input = toga.TextInput(style=Pack(flex=1))
        nome_box = toga.Box(style=Pack(direction=ROW, padding=5))
        nome_box.add(nome_label)
        nome_box.add(self.nome_input)

        # Campo Data de Nascimento
        data_label = toga.Label("Data de nascimento:", style=Pack(padding=(0, 5)))
        self.data_input = toga.TextInput(placeholder="dd/mm/aaaa", style=Pack(flex=1))
        box_data = toga.Box(style=Pack(direction=ROW, padding=5))
        box_data.add(data_label)
        box_data.add(self.data_input)

        # Campo Endereço
        endereco_label = toga.Label("Endereço:", style=Pack(padding=(0, 5)))
        self.endereco_input = toga.TextInput(placeholder="", style=Pack(flex=1))
        box_endereco = toga.Box(style=Pack(direction=ROW, padding=5))
        box_endereco.add(endereco_label)
        box_endereco.add(self.endereco_input)

        # Campo Telefone
        telefone_label = toga.Label("Telefone:", style=Pack(padding=(0, 5)))
        self.telefone_input = toga.TextInput(placeholder="(xx) xxxx-xxxx", style=Pack(flex=1))
        box_telefone = toga.Box(style=Pack(direction=ROW, padding=5))
        box_telefone.add(telefone_label)
        box_telefone.add(self.telefone_input)

        # Botão
        button = toga.Button("Insira dados", on_press=self.enviarDados, style=Pack(padding=5))

        # Adicionando todos os campos ao layout principal
        main_box.add(nome_box)
        main_box.add(box_data)
        main_box.add(box_endereco)
        main_box.add(box_telefone)
        main_box.add(button)

        # Criando e exibindo a janela
        self.main_window = toga.MainWindow(title="Meu segundo App")
        self.main_window.content = main_box
        self.main_window.show()

    def enviarDados(self, widget):
        nome = self.nome_input.value
        data = self.data_input.value
        endereco = self.endereco_input.value
        telefone = self.telefone_input.value
        print(f"Nome: {nome}, Data: {data}, Endereço: {endereco}, Telefone: {telefone}")
        self.nome_input.value = ""
        self.data_input.value = ""
        self.endereco_input.value = ""
        self.telefone_input.value = ""


def main():
    return BeeWare1()
