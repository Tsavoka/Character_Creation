from tkinter import *
from tkinter import messagebox
from character import Application
from observer import *
from new_character import NewCharacter


class MainWindow(Frame, Observer):
    warrior = NewCharacter()

    def __init__(self, master):
        super(MainWindow, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # описание
        Label(self,
              text='У тебя есть ' + str(MainWindow.warrior.get_points()) +
                   ' очков и 2 характеристики.\n' \
                   'Накидай своему персонажу.'
              ).grid(row=0, column=0, columnspan=2, sticky=W)
        # сколько очков
        Label(self,
              text='Осталось поинтов:'
              ).grid(row=1, column=0)
        self.points_label = Label(self,
                                  text=str(MainWindow.warrior.get_points())
                                  ).grid(row=1, column=2)
        # характеристика
        Label(self,
              text='Слабоумие'
              ).grid(row=2, column=0)
        # выбор
        self.first_app = Application(self, MainWindow.warrior)
        self.first_app.grid(row=3, column=0)
        self.first_app.attach(self)
        # еще
        Label(self,
              text='Отвага'
              ).grid(row=2, column=1)
        # выбор
        self.second_app = Application(self, MainWindow.warrior)
        self.second_app.grid(row=3, column=1)
        # подтверждение
        self.message_button = Button(text="Подтвердить",
                                     command=(lambda: self.confirm_changes()))
        self.message_button.grid(row=4, column=2)

    def confirm_changes(self):
        MainWindow.warrior.set_stupidity(self.first_app.get_points())
        MainWindow.warrior.set_bravery(self.second_app.get_points())
        messagebox.showinfo('Подтверждение',
                            'Слабоумие ' + MainWindow.warrior.get_stupidity() +
                            '\n' +
                            'Отвага ' + MainWindow.warrior.get_bravery())

    def update(self, subject: Subject) -> None:
        if subject._state == 0 and MainWindow.warrior.get_points() < 30:
            Label(self,
                  text=str(MainWindow.warrior.get_points())
                  ).grid(row=1, column=2)
        elif subject._state == 1 and MainWindow.warrior.get_points() > 0:
            Label(self,
                  text=str(MainWindow.warrior.get_points())
                  ).grid(row=1, column=2)
        else:
            Label(self,
                  text=str(MainWindow.warrior.get_points())
                  ).grid(row=1, column=2)


root = Tk()
root.title('Создание персонажа')
app = MainWindow(root)
root.mainloop()
