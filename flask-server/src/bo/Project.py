import datetime

from src.bo.BusinessObject import BusinessObject as bo


class Project(bo):
    def __init__(self):
        super().__init__()
        self._start_date = datetime.datetime.now()
        self._end_date = datetime.datetime.now()
        self._name = ""

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_start_date(self):
        return self._start_date

    def set_start_date(self, timestamp):
        self._start_date = timestamp

    def get_end_date(self):
        return self._end_date

    def set_end_date(self, timestamp):
        self._end_date = timestamp

    def __str__(self):
        return self._start_date.strftime('%m/%d/%Y, %H:%M:%S') + "\n" \
               + self._end_date.strftime('%m/%d/%Y, %H:%M:%S') + "\n" \
               + self._name
    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Project()
        obj.set_id(dictionary["id"])
        obj.set_start_date(dictionary["start_date"])
        obj.set_end_date(dictionary["end_date"])
        obj.set_name(dictionary["name"])
        return obj

    @staticmethod
    def to_dict(project):
        project_dict = {'id': project.get_id(),
                        'start_date': project.get_start_date().strftime("%m/%d/%Y, %H:%M:%S"),
                        'end_date': project.get_end_date().strftime("%m/%d/%Y, %H:%M:%S"),
                        'name': project.get_name(),
                        'phases': ''}
        return project_dict

