import psycopg2


class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class Db:
    def __init__(self):
        conn = psycopg2.connect(host='localhost', port='5432', dbname="pb", user="pb", password="")


if __name__ == '__main__':
    d = Db.Instance()
    d2 = Db.Instance()
