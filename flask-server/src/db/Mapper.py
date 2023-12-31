import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod


class Mapper (AbstractContextManager, ABC):

    def __init__(self):
        self._cnx = None

    def __enter__(self):

        if os.getenv('GAE_ENV', '').startswith('standard'):
            '''Cloud'''
            self._cnx = connector.connect(user='root', password='password',
                                          unix_socket='/cloudsql/winged-memory-407417:europe-west3:kanban-db',
                                          database='KanbanDB')
        else:
            '''Local'''
            self._cnx = connector.connect(user='root', password='Lollipopp2402',
                                  host='127.0.0.1',
                                  database='kanbandb')

        return self
    """the connection to the database gets closed after the data from the request gets fetched"""

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cnx.close()

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_key(self, key):
        pass

    @abstractmethod
    def insert(self, object):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, object):
        pass