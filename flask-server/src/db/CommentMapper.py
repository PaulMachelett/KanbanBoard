from src.bo.Comment import Comment
from src.db.Mapper import Mapper


class CommentMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, comment):
        cursor = self._cnx.cursor()

        command = "INSERT INTO Comment (creator, content, cardid, creation_date) VALUES (%s, %s, %s, %s)"
        data = (comment.get_creator(), comment.get_content(), comment.get_cardid(), comment.get_creation_date())
        cursor.execute(command, data)
        self._cnx.commit()
        comment_id = cursor.lastrowid

        cursor.close()
        return comment_id

    def delete(self, commentid):
        cursor = self._cnx.cursor()

        command = "DELETE FROM Comment WHERE id = {}".format(commentid)
        cursor.execute(command)
        self._cnx.commit()

        cursor.close()
        return commentid

    def update(self, comment):
        cursor = self._cnx.cursor()

        command = "UPDATE comment SET creator = %s, content = %s, creation_date = %s, cardid = %s WHERE id = %s"
        data = (comment.get_creator(), comment.get_content(), comment.get_creation_date(),
                comment.get_cardid(), comment.get_id())
        cursor.execute(command, data)
        self._cnx.commit()

        cursor.close()
        return comment

    def find_by_key(self, id):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM Comment WHERE id = {}".format(id)
        cursor.execute(command)
        result = cursor.fetchone()
        if result:
            comment = Comment()
            comment.set_id(result[0])
            comment.set_creator(result[1])
            comment.set_content(result[2])
            comment.set_cardid(result[3])
            comment.set_creation_date(result[4])
        cursor.close()
        return comment

    def find_by_creator(self, id):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM Comment WHERE creator = {}".format(id)
        cursor.execute(command)
        result = cursor.fetchone()
        if result:
            comment = Comment()
            comment.set_id(result[0])
            comment.set_creator(result[1])
            comment.set_content(result[2])
            comment.set_cardid(result[3])
            comment.set_creation_date(result[4])
        cursor.close()
        return comment

    def find_all_by_cardid(self, id):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM Comment WHERE cardid = {}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creator, content, cardid, creation_date) in tuples:
            c = Comment()
            c.set_id(id)
            c.set_creator(creator)
            c.set_content(content)
            c.set_cardid(cardid)
            c.set_creation_date(creation_date)
            result.append(c)

        cursor.close()
        return result

    def find_all(self):
        pass


if (__name__ == "__main__"):
    with CommentMapper() as mapper:
        result = mapper.find_by_key(1)
        print(result)




