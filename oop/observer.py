"""
    Observer Design Pattern
"""


from abc import ABC, abstractmethod


class Subject:

    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def uregister_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class AbstractObserver(ABC):

    @abstractmethod
    def update(self, subject):
        pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Facebook(Subject):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def new_msg(self, msg):
        print("A new msg is being processed, DB, ...")
        self.notify()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Device(AbstractObserver):

    def __init__(self, name):
        self.name = name

    def update(self, subject):
        print('Showing message in {}'.format(self.name))


class LoggingServer(AbstractObserver):

    def update(self, subject):
        print("Message is saved on server")


sarah_fb = Facebook('Sarah')

logging_server = LoggingServer()
sarah_fb.register_observer(logging_server)
iphone = Device('iPhone')
sarah_fb.register_observer(iphone)
desktop = Device('Desktop')
sarah_fb.register_observer(desktop)
laptop = Device('laptop')
sarah_fb.register_observer(laptop)

sarah_fb.new_msg('This is a new message')