from src.bo.ProjectParticipation import ProjectParticipation
from src.db.Mapper import Mapper
from src.bo.Project import Project
from src.bo.Person import Person


class ProjectParticipationMapper (Mapper):

    def __init__(self):
        super().__init__()

    def find_all_person_by_project_id(self, key):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Project_Participation WHERE projectid={}".format(key))
        tuples = cursor.fetchall()

        for (personid) in tuples:
            result.append(personid[0])

        t = tuple(result)

        command = "SELECT * FROM Person WHERE id IN {}".format(t)
        cursor.execute(command)
        tuples = cursor.fetchall()

        result.clear()

        for (id, nickname, firstname, lastname, googleid, email) in tuples:
            person = Person()
            person.set_id(id)
            person.set_nickname(nickname)
            person.set_firstname(firstname)
            person.set_lastname(lastname)
            person.set_googleid(googleid)
            person.set_email(email)
            result.append(person)

        self._cnx.commit()
        cursor.close()
        return result

    def find_all_project_by_person_id(self, key):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT projectid FROM Project_participation WHERE personid={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (projectid) in tuples:
            result.append(projectid[0])

        t = tuple(result)

        command = "SELECT * FROM Project WHERE id IN {}".format(t)
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        result.clear()
        
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

    def insert(self, projectparticipation):
        cursor = self._cnx.cursor()

        command = "INSERT INTO Project_Participation (projectid, personid) VALUES (%s, %s)"
        data = (projectparticipation.get_projectid(), projectparticipation.get_personid())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return projectparticipation

    def update(self):
        pass

    def delete_projectparticipation(self, projectparticipation):

        cursor = self._cnx.cursor()

        command = "DELETE FROM Project_Participation WHERE projectid=%s AND personid=%s"
        data = (projectparticipation.get_projectid(), projectparticipation.get_personid())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return projectparticipation

    def delete(self):
        pass

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT projectid, personid from Project_Participation"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (projectid, personid) in tuples:
            obj = ProjectParticipation()
            obj.set_projectid(projectid)
            obj.set_personid(personid)
            result.append(obj)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        pass


if (__name__ == "__main__"):
    with ProjectParticipationMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)