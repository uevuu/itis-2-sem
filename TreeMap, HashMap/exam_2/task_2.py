class NewsObservers:
    """Наблюдатели за новостями."""

    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        """Подключаем наблюдателя"""
        self.__observers.append(observer)

    def detach(self, observer):
        """Отключаем наблюдателя"""
        self.__observers.remove(observer)

    def notify_subscribe(self):
        """Отправка уведомледний"""
        for observer in self.__observers:
            observer.subscribe()

    def notify_post_feed(self):
        for observer in self.__observers:
            observer.post_feed()


class User:
    """Пользователи в ленте"""

    def __init__(self, user_id: int):
        self.user_id = user_id
        self.topic = None
        self.feed_id = None

    def create_topic(self, topic: str, feed_id: int):
        self.topic = topic
        self.feed_id = feed_id

    def subscribe(self):
        if self.check_topic():
            print(f'Пользователь {self.user_id} подписался на новость "{self.feed_id}"')
        else:
            print(f'Пользователь {self.user_id} не подписался ни на одну новость')

    def post_feed(self):
        if self.check_topic():
            print(f'Пользователь {self.user_id} получил новость "{self.feed_id}"')
        else:
            print(f'Пользователь {self.user_id} не получил ни одну новость')

    def check_topic(self):
        if self.topic == self.feed_id is None:
            return False
        else:
            return True


user_1 = User(1)
user_1.create_topic('IT', 1)
user_2 = User(2)
user_2.create_topic('Sport', 2)
user_3 = User(3)
user_3.create_topic('Sport', 2)
user_4 = User(4)

news_system = NewsObservers()

news_system.attach(user_1)
news_system.attach(user_2)
news_system.attach(user_3)
news_system.attach(user_4)

print('\n')

news_system.notify_subscribe()

print('\n')

news_system.notify_post_feed()

print('\n')

news_system.detach(user_4)
news_system.notify_subscribe()
