"""
Projeto da aula de Framework
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import mysql.connector


class Beeware1(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Nome: ",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Diga Olá!",
            on_press=self.enviarParaBancoDeDados,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def say_hello(self, widget):
        print(f"Hello, {self.name_input.value}")

    def say_hello2(self, widget):
        self.enviarParaBancoDeDados()
        self.main_window.info_dialog(
            f"Olá, {self.name_input.value}",
            "Tudo bem aí???"
        )


    ##INI BD
    def enviarParaBancoDeDados(self, widget):
        mydb = mysql.connector.connect(
            host="localhost",#"localhost:3306",
            user="root",
            # password="yourpassword",#só coloque senha se for diferente de vazio
            database="meubd"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO Pessoas (nome) VALUES (%s)"
        val = [(self.name_input.value)]
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "registro inserido.")

        queryDeTeste = "select * from PESSOAS"

        mycursor.execute(queryDeTeste)
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    ##FIM BD




def main():
    return Beeware1()