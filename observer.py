from abc import ABC, abstractmethod


class Observer(ABC):
    pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass
