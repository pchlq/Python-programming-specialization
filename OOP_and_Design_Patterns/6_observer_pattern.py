from abc import ABC, abstractmethod

# Опишем наблюдаемую систему
class ObservableEngine(Engine):
    def __init__(self):
        # Объявим пустое множество подписчиков
        self.__subscribers = set()
        
    def subscribe(self, subscriber):
        # Добавим пользователя во множество подписчиков
        self.__subscribers.add(subscriber)
        
    def unsubscribe(self, subscriber):
        # Если данный подписчик присутствует в списке подписчиков, его можно удалить
        self.__subscribers.remove(subscriber)
        
    def notify(self, achievement):
        # Отправка уведомления всем подписчикам
        for subscriber in self.__subscribers:
            subscriber.update(achievement)
            

# Определим абстрактного наблюдателя
class AbstractObserver(ABC):

    # Каждый конкретный наблюдатель должен будет реализовать метод update
    @abstractmethod
    def update(self, achievement):
        pass
    

# Определим конкретных наблюдателей
class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        # Объявим множество всех полученных достижений
        self.achievements = set()
    
    def update(self, achievement):
        # Добавим название достижения во множество достижений
        self.achievements.add(achievement['title'])
        
        
class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        # Объявим список всех полученных достижений
        self.achievements = list()
        
    def update(self, achievement):
        # Если подобного достижения не было в списке, добавим его
        if achievement not in self.achievements:
            self.achievements.append(achievement)