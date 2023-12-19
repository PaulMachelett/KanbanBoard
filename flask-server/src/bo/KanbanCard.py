from src.bo.BusinessObject import BusinessObject as bo
from datetime import datetime

class KanbanCard(bo):
    def __init__(self):
        super().__init__()
        self._title = ""
        self._content = ""
        self._phaseid = 0
        self._start_date = datetime.now()
        self._end_date = datetime.now()
        self._assigned_person = 0
        self._creator = 0

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content

    def get_start_date(self):
        return self._start_date

    def set_start_date(self, date):
        self._start_date = date

    def get_end_date(self):
        return self._end_date

    def set_end_date(self, date):
        self._end_date = date

    def get_phaseid(self):
        return self._phaseid

    def set_phaseid(self, phaseid):
        self._phaseid = phaseid

    def get_creator(self):
        return self._creator

    def set_creator(self, creator):
        self._creator = creator

    def get_assigned_person(self):
        return self._assigned_person

    def set_assigned_person(self, assigned_personid):
        self._assigned_person = assigned_personid

    def __str__(self):
        return self._title + "\n" + self._content + "\n"+ str(self._phaseid) + "\n"\
               + self._start_date.strftime('%m/%d/%Y, %H:%M:%S') + "\n"\
               + self._end_date.strftime('%m/%d/%Y, %H:%M:%S') + "\n" \
               + str(self._creator) + "\n" + str(self._assigned_person)


    @staticmethod
    def from_dict(dictionary=dict()):
        obj = KanbanCard()
        obj.set_id(dictionary["id"])
        obj.set_title(dictionary["title"])
        obj.set_content(dictionary["content"])
        obj.set_phaseid(dictionary["phaseid"])
        obj.set_start_date(dictionary["start_date"])
        obj.set_end_date(dictionary["end_date"])
        obj.set_creator(dictionary["creator"])
        obj.set_assigned_person(dictionary["assigned_person"])
        return obj

    @staticmethod
    def to_dict(kanbancard):
        card_dict = {'id': kanbancard.get_id(),
                     'title': kanbancard.get_title(),
                     'content': kanbancard.get_content(),
                     'phaseid': kanbancard.get_phaseid(),
                     'start_date': kanbancard.get_start_date().strftime("%m/%d/%Y, %H:%M:%S"),
                     'end_date': kanbancard.get_end_date().strftime("%m/%d/%Y, %H:%M:%S"),
                     'creator': kanbancard.get_creator(),
                     'assigned_person': kanbancard.get_assigned_person(),
                     'comments': ''
                     }
        return card_dict
