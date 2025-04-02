from typing import List
from abc import ABC, abstractmethod

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
        self._state: str = ""

    def add_observer(self, observer:"Observer") -> None:
        """Adiciona um observador à lista"""
        self._observers.append(observer)

    def remove_observer(self, observer:"Observer") -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """Notifica todos os observadores quando o estado muda"""
        for observer in self._observers:
            observer.update(self._state)
            
    def set_state(self, state: str) -> None:
        """Define o estado do assunto"""
        self._state = state
        self.notify_observers()
        

class Observer(ABC):
    @abstractmethod
    def update(self, state: str) -> None:
        """Atualiza o estado do observador"""
        pass


class ConcreteObserver1(Observer):
    def update(self, state: str) -> None:
        print(f"Obeserve 1 recebeu a notificação: {state}")
        

class ConcreteObserver2(Observer):
    def update(self, state: str) -> None:
        print(f"Obeserver 2 recebeu a notificação: {state}")

if __name__ == "__main__":
    subject = Subject()

    observer1 = ConcreteObserver1()
    observer2 = ConcreteObserver2()

    subject.add_observer(observer1)
    subject.add_observer(observer2)

    print("🔹 Mudando estado para 'Estado 1'")
    subject.set_state("Estado 1")

    print("\n🔹 Mudando estado para 'Estado 2'")
    subject.set_state("Estado 2")

    print("\n🔹 Removendo Observer A e mudando estado para 'Estado 3'")
    subject.remove_observer(observer1)
    subject.set_state("Estado 3")