from src.bo.Phase import Phase
from src.db.Mapper import Mapper


class PhaseMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_by_key(self, id):
        cursor = self._cnx.cursor()
        command = "SELECT id, name, projectid FROM Phase WHERE id={}".format(id)
        cursor.execute(command)
        result = cursor.fetchone()

        if result:
            phase = Phase()
            phase.set_id(result[0])
            phase.set_name(result[1])
            phase.set_projectid(result[2])

        self._cnx.commit()
        cursor.close()

        return phase

    def find_all_by_projectid(self, id):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Phase WHERE projectid={}".format(id))
        tuples = cursor.fetchall()
#hier die set_time_stamp methode anschauen 
        for (id,name, projectid) in tuples:
            phase = Phase()
            phase.set_id(id)
            phase.set_name(name)
            phase.set_projectid(projectid)

            result.append(phase)
        

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, phase):
        cursor = self._cnx.cursor()

        command = "INSERT INTO Phase (name, projectid) VALUES (%s ,%s)"
        data = (phase.get_name(), phase.get_projectid())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return phase

    def update(self, phase):
        cursor = self._cnx.cursor()

        command = """UPDATE Phase SET name=%s, projectid=%s WHERE id=%s"""
        data = (phase.get_name(), phase.get_projectid(), phase.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return phase

    def delete(self, id):

        cursor = self._cnx.cursor()

        command = "DELETE FROM Phase WHERE id={}".format(id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_all(self):
        pass

if (__name__ == "__main__"):
    with PhaseMapper() as mapper:
        result = mapper.find_by_key(1)
        print(result)