from src.bo.Person import Person
from src.db.Mapper import Mapper


class PersonMapper (Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from Person")
        tuples = cursor.fetchall()
        p = Person()

        for (id, nickname, firstname, lastname, googleid, email) in tuples:
            p.set_id(id)
            p.set_nickname(nickname)
            p.set_firstname(firstname)
            p.set_lastname(lastname)
            p.set_googleid(googleid)
            p.set_email(email)
            result.append(p)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        command = "SELECT id, nickname, firstname, lastname, googleid, email FROM Person WHERE id={}".format(key)
        cursor.execute(command)
        result = cursor.fetchone()
        p = Person()

        if result:

            p.set_id(result[0])
            p.set_nickname(result[1])
            p.set_firstname(result[2])
            p.set_lastname(result[3])
            p.set_googleid(result[4])
            p.set_email(result[5])

        self._cnx.commit()
        cursor.close()

        return p

    def insert(self, person):
        cursor = self._cnx.cursor()

        command = "INSERT INTO Person (nickname, firstname, lastname, googleid, email) VALUES (%s, %s, %s, %s, %s)"
        data = (person.get_nickname(), person.get_firstname(), person.get_lastname(), person.get_googleid()
                , person.get_email())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return person

    def update(self, person):
        cursor = self._cnx.cursor()

        command = """UPDATE Person SET nickname =%s, firstName=%s, lastName=%s, googleid=%s, email=%s WHERE id=%s"""
        data = (person.get_nickname(), person.get_firstname(), person.get_lastname(), person.get_googleid()
                , person.get_email(), person.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return person

    def delete(self, id):
        cursor = self._cnx.cursor()

        command = "DELETE FROM Person WHERE id={}".format(id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

        return id

    def find_by_email(self, email):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM Person WHERE email = '{}'".format(email)
        cursor.execute(command)
        result = cursor.fetchone()
        p = Person()

        if result:
            p.set_id(result[0])
            p.set_nickname(result[1])
            p.set_firstname(result[2])
            p.set_lastname(result[3])
            p.set_googleid(result[4])
            p.set_email(result[5])

        self._cnx.commit()
        cursor.close()

        return p

    def find_by_googleid(self, id):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM Person WHERE googleid = '{}'".format(id)
        cursor.execute(command)
        result = cursor.fetchone()
        p = Person()

        if result:
            p.set_id(result[0])
            p.set_nickname(result[1])
            p.set_firstname(result[2])
            p.set_lastname(result[3])
            p.set_googleid(result[4])
            p.set_email(result[5])

        self._cnx.commit()
        cursor.close()

        return p


if (__name__ == "__main__"):
    with PersonMapper() as mapper:
        result = mapper.find_by_googleid(23634061812457054952398)
        print(result)
