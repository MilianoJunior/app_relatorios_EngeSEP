from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    _data: list = []
    _name_db: str = ''
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """
    def get_observers(self):
        [print(name) for name in self._observers]

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self, data, name_db) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

#        print("\nSubject: I'm doing something important.")
        self._data = data
        self._name_db = name_db

#        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

#
#class Observer(ABC):
#    """
#    The Observer interface declares the update method, used by subjects.
#    """
#
#    @abstractmethod
#    def update(self, subject: Subject) -> None:
#        """
#        Receive update from subject.
#        """
#        pass


#"""
#Concrete Observers react to the updates issued by the Subject they had been
#attached to.
#"""


#class ConcreteObserverA(Observer):
#    def update(self, subject: Subject) -> None:
#        if subject._state < 3:
#            print("ConcreteObserverA: Reacted to the event")
#
#
#class ConcreteObserverB(Observer):
#    def update(self, subject: Subject) -> None:
#        if subject._state == 0 or subject._state >= 2:
#            print("ConcreteObserverB: Reacted to the event")


#if __name__ == "__main__":
#    # primeiro passo: criar a class Subject, que registra os objetos observados
#    subject = ConcreteSubject()
#    #
#    observer_a = ConcreteObserverA()
#    subject.attach(observer_a)
#
#    observer_b = ConcreteObserverB()
#    subject.attach(observer_b)
#
#    subject.some_business_logic()
#    subject.some_business_logic()
#
#    subject.detach(observer_a)
#
#    subject.some_business_logic()