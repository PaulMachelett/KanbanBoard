from src.db.Mapper import Mapper
from src.bo.KanbanCard import KanbanCard


class KanbanCardMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, kanbancard):
        try:
            cursor = self._cnx.cursor()
            command = """INSERT INTO Kanbancard (title, content, phaseid, start_date, end_date, creator, 
            assigned_person) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            data = (kanbancard.get_title(), kanbancard.get_content(), kanbancard.get_phaseid(),
                    kanbancard.get_start_date(), kanbancard.get_end_date(), kanbancard.get_creator(),
                    kanbancard.get_assigned_person())
            cursor.execute(command, data)
            self._cnx.commit()
            canbancard_id = cursor.lastrowid
        except Exception as e:
            print("Fehler beim Erstellen der KanbanCard:", str(e))
            canbancard_id = None
        finally:
            cursor.close()
            return canbancard_id

    def delete(self, id):
        try:
            cursor = self._cnx.cursor()
            command = "DELETE FROM Kanbancard WHERE id = {}".format(id)
            cursor.execute(command)
            self._cnx.commit()
            success = True

        except Exception as e:
            print("Fehler beim Löschen der Kanbancard:", str(e))
            success = False
        finally:
            cursor.close()
            return success

    def update(self, kanbancard):
        try:
            cursor = self._cnx.cursor()
            command = """UPDATE Kanbancard SET title = %s, content = %s, phaseid = %s, start_date = %s, end_date = %s, 
            creator = %s, assigned_person = %s WHERE id = %s"""
            data = (kanbancard.get_title(), kanbancard.get_content(), kanbancard.get_phaseid(),
                    kanbancard.get_start_date(), kanbancard.get_end_date(), kanbancard.get_creator(),
                    kanbancard.get_assigned_person(), kanbancard.get_id())
            cursor.execute(command, data)
            self._cnx.commit()
            success = cursor.rowcount > 0
        except Exception as e:
            print("Fehler beim Aktualisieren der Kanban Karte:", str(e))
            success = False
        finally:
            cursor.close()
            return success

    def find_by_key(self, key):
        kanbancard = KanbanCard()
        try:
            cursor = self._cnx.cursor()
            command = "SELECT * FROM Kanbancard WHERE id = {}".format(key)
            cursor.execute(command)
            result = cursor.fetchone()
            if result:
                kanbancard.set_id(result[0])
                kanbancard.set_title(result[1])
                kanbancard.set_content(result[2])
                kanbancard.set_phaseid(result[3])
                kanbancard.set_start_date(result[4])
                kanbancard.set_end_date(result[5])
                kanbancard.set_creator(result[6])
                kanbancard.set_assigned_person(result[7])
        except Exception as e:
            print("Fehler beim Suchen der Kanbancard:", str(e))
            kanbancard = None
        finally:
            cursor.close()
            return kanbancard

    def find_all_by_assigned_person(self, id):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from Kanbancard WHERE id={}".format(id))
        tuples = cursor.fetchall()

        for (id, title, content, phase_id, start_date, end_date, creator,
             assigned_person) in tuples:
            card = KanbanCard()
            card.set_id(id)
            card.set_title(title)
            card.set_content(content)
            card.set_phaseid(phase_id)
            card.set_start_date(start_date)
            card.set_end_date(end_date)
            card.set_creator(creator)
            card.set_assigned_person(assigned_person)
            result.append(card)

        self._cnx.commit()
        cursor.close()
        return result

    def find_all_by_creator(self, id):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from Kanbancard WHERE creator={}".format(id))
        tuples = cursor.fetchall()

        for (id, title, content, phase_id, start_date, end_date, creator,
             assigned_person) in tuples:
            card = KanbanCard()
            card.set_id(id)
            card.set_title(title)
            card.set_content(content)
            card.set_phaseid(phase_id)
            card.set_start_date(start_date)
            card.set_end_date(end_date)
            card.set_creator(creator)
            card.set_assigned_person(assigned_person)
            result.append(card)

        self._cnx.commit()
        cursor.close()
        return result

    def find_all_by_phaseid(self, id):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from Kanbancard WHERE phaseid={}".format(id))
        tuples = cursor.fetchall()

        for (id, title, content, phase_id, start_date, end_date, creator,
             assigned_person) in tuples:
            card = KanbanCard()
            card.set_id(id)
            card.set_title(title)
            card.set_content(content)
            card.set_phaseid(phase_id)
            card.set_start_date(start_date)
            card.set_end_date(end_date)
            card.set_creator(creator)
            card.set_assigned_person(assigned_person)
            result.append(card)

        self._cnx.commit()
        cursor.close()
        return result


    def find_all(self):
        pass


if (__name__ == "__main__"):
    card = KanbanCard()
    card.set_id(1)
    with KanbanCardMapper() as mapper:
        result = mapper.delete(card)
        print(result)