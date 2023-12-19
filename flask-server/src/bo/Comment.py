from src.bo.BusinessObject import BusinessObject as bo
from datetime import datetime

class Comment(bo):
    # Konstruktor der Klasse
    def __init__(self):
        super().__init__()
        self._creator = 0
        self._content = ""
        self._cardid = 0
        self._creation_date = datetime.now()

    def get_creator(self):
        return self._creator

    def set_creator(self, creator):
        self._creator = creator

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content

    def get_cardid(self):
        return self._cardid

    def set_cardid(self, cardid):
        self._cardid = cardid

    def get_creation_date(self):
        return self._creation_date

    def set_creation_date(self, creation_date):
        self._creation_date = creation_date

    def __str__(self):
        return str(self._creator) + "\n" + self._content + "\n" + str(self._cardid) + "\n"\
               + self._creation_date.strftime('%m/%d/%Y, %H:%M:%S')

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Comment()
        obj.set_id(dictionary["id"])
        obj.set_creator(dictionary["creator"])
        obj.set_content(dictionary["content"])
        obj.set_cardid(dictionary["cardid"])
        obj.set_creation_date(dictionary["creation_date"])
        return obj


    @staticmethod
    def to_dict(comment):
        comment_dict = {'id': comment.get_id(),
                        'creator': comment.get_creator(),
                        'content': comment.get_content(),
                        'cardid': comment.get_cardid(),
                        'creation_date': comment.get_creation_date().strftime("%m/%d/%Y, %H:%M:%S")
                        }
        return comment_dict
