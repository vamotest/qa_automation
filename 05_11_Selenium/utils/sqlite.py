from sqlalchemy import create_engine


def _create_database():
    engine = create_engine('sqlite:///../tests/log.db')
    return engine


class Sqlite:

    def __init__(self):
        self.engine = _create_database()
        self._create_table()

    def _create_table(self):
        self.engine.execute('CREATE TABLE IF NOT EXISTS logs('
                            '"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                            '"message" varchar(255))')

    def write_log(self, text):
        self.engine.execute(r'INSERT INTO logs (message) VALUES ("{}")'.
                            format(text))
