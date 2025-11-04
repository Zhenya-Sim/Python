from sqlalchemy import create_engine, text


class SubjectTable:
    __scripts = {
        "select": text("SELECT * FROM subject"),
        "select_by_id": text("SELECT * FROM subject WHERE subject_id = :id"),
        "insert_new": text(
            "INSERT INTO subject (\"subject_title\", \"subject_id\") "
            "values (:new_name, :new_id)"),
        "update": text(
            "update subject set subject_title = :new_title "
            "where subject_id = :id"),
        "delete": text("DELETE FROM subject WHERE \"subject_id\" = :id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        conn.close()
        return result.mappings().all()

    def get_subject_by_id(self, id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_by_id"], {"id": id})
        conn.close()
        return result.mappings().first()

    def add_subject(self, name, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts[
            "insert_new"], {"new_name": name, "new_id": id})
        conn.commit()
        conn.close()

    def delete_subject(self, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete"], {"id": id})
        conn.commit()
        conn.close()

    def update_subject(self, new_title, id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts[
            "update"], {"new_title": new_title, "id": id})
        rows = result.mappings().all
        conn.commit()
        conn.close()
        return rows
