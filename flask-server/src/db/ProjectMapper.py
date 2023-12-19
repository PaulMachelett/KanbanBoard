from src.bo.Project import Project
from src.db.Mapper import Mapper



class ProjectMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("Select * from Project")
        tuples = cursor.fetchall()

        for (id, start_date, end_date, name) in tuples:
            project = Project()
            project.set_id(id)
            project.set_start_date(start_date)
            project.set_end_date(end_date)
            project.set_name(name)
            result.append(project)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM Project WHERE id={}".format(key)
        cursor.execute(command)
        result = cursor.fetchone()

        if result:
            project = Project()
            project.set_id(result[0])
            project.set_start_date(result[1])
            project.set_end_date(result[2])
            project.set_name(result[3])

        self._cnx.commit()
        cursor.close()
        return project

    def find_by_name(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM Project WHERE name = '{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, start_date, end_date, name) in tuples:
            project = Project()
            project.set_id(id)
            project.set_start_date(start_date)
            project.set_end_date(end_date)
            project.set_name(name)
            result.append(project)

            self._cnx.commit()
            cursor.close()

        return result


    def insert(self, project):
        cursor = self._cnx.cursor()
        command = "INSERT INTO Project (start_date, end_date, name) VALUES (%s, %s, %s)"
        data = (project.get_start_date(), project.get_end_date(), project.get_name())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, id):

        cursor = self._cnx.cursor()
        command = "DELETE FROM Project WHERE id={}".format(id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def update(self, project):
        cursor = self._cnx.cursor()

        command = """UPDATE Project SET start_date=%s, end_date=%s, name=%s WHERE id=%s"""
        data = (project.get_start_date(), project.get_end_date(), project.get_name(), project.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

if (__name__ == "__main__"):
    with ProjectMapper() as mapper:
        result = mapper.find_by_key(1)
        print(result)
