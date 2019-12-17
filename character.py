from tkinter import *
from observer import *
from typing import List


class Application(Frame, Subject):
    _state: int = None
    _observers: List[Observer] = []

    def __init__(self, master, warrior):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.warrior = warrior
        self.points = 0

    def create_widgets(self):

        # кнопка меньше
        self.less_bttn = Button(self, text='<', command=self.less_points)
        self.less_bttn.grid(row=0, column=0)
        # поле со значением
        self.ent_points = Entry(self, width=2, justify=CENTER)
        self.ent_points.insert(0, '0')
        self.ent_points.grid(row=0, column=1)
        # кнопка больше
        self.more_bttn = Button(self, text='>', command=self.more_points)
        self.more_bttn.grid(row=0, column=2)

    def less_points(self):
        if self.points > 0:
            self.points -= 1
            self.update_view()
            self.warrior.add_points(1)
            self._state = 0
            self.update_main()

    def more_points(self):
        if self.points < 30 and self.warrior.get_points() != 0:
            self.points += 1
            self.update_view()
            self.warrior.remove_points(1)
            self._state = 1
            self.update_main()

    def get_points(self):
        return self.ent_points.get()

    def update_view(self):
        self.ent_points.delete(0, END)
        self.ent_points.insert(0, self.points)

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def update_main(self):
        self.notify()

