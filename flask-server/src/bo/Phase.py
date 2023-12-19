from src.bo.BusinessObject import BusinessObject as BusinessObject

class Phase(BusinessObject):

    def __init__(self):
        super().__init__()
        self._name = ""
        self._projectid = 0
        #nächste Zeile bitte löschen
        self._time_stamp = ""

    def get_name(self):
        return self._name
   
    def set_name(self, name):
        self._name = name

    # löschen 
    def get_time_stamp(self):
        return self._time_stamp   

    def set_time_stamp(self,time_stamp):
        self._time_stamp = time_stamp 
    ######    
    def get_projectid(self):
        return self._projectid

    def set_projectid (self, projectid):
        self._projectid = projectid

    def __str__(self):
        return self._name + "\n" + str(self._projectid)

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Phase()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["name"])
        obj.set_projectid(dictionary["projectid"])
        return obj

    @staticmethod
    def to_dict(phase):
        phase_dict = {'id': phase.get_id(),
                      'name': phase.get_name(),
                      'projectid': phase.get_projectid(),
                      'kanbancards': ''
                      }
        return phase_dict

