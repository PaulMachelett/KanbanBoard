from src.bo.BusinessObject import BusinessObject as bo


class ProjectParticipation(bo):
    def __init__(self):
        super().__init__()
        self._projectid = 0
        self._personid = 0

    def get_projectid(self):
        return self._projectid

    def set_projectid(self, projectid):
        self._projectid = projectid

    def get_personid(self):
        return self._personid

    def set_personid(self, personid):
        self._personid = personid

    def __str__(self):
        return str(self._projectid) + "\n" + str(self._personid)

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = ProjectParticipation()
        obj.set_projectid(dictionary["projectid"])
        obj.set_personid(dictionary["personid"])

        return obj
