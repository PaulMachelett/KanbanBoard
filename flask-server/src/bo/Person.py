from src.bo.BusinessObject import BusinessObject as bo


class Person(bo):
    def __init__(self):
        super().__init__()
        self._nickname = ""
        self._firstname = ""
        self._lastname = ""
        self._googleid = 0
        self._email = ""

    def get_nickname(self):
        return self._nickname

    def set_nickname(self, nickname):
        self._nickname = nickname

    def get_firstname(self):
        return self._firstname

    def set_firstname(self, firstname):
        self._firstname = firstname

    def get_lastname(self):
        return self._lastname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def get_googleid(self):
        return self._googleid

    def set_googleid(self, googleid):
        self._googleid = googleid

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def __str__(self):
        return self._nickname + "\n" + self._firstname + "\n"+ self._lastname + "\n"\
               + str(self._googleid) + "\n" + self._email

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Person()
        obj.set_id(dictionary["id"])
        obj.set_nickname(dictionary["nickname"])
        obj.set_firstname(dictionary["firstname"])
        obj.set_lastname(dictionary["lastname"])
        obj.set_googleid(dictionary["googleid"])
        obj.set_email(dictionary["email"])
        return obj
