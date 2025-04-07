from sqlalchemy import create_engine
from sqlalchemy.sql import text

class Table_DB:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)


# Метод для получения списка предметов.
    def get_subjects(self):
        with self.db.connect() as connection:
            result = connection.execute(text("SELECT * FROM subject"))
            return result.mappings().all()


# Метод для добавления нового предмета.
    def create_new_subject(self, id, title):
        with self.db.connect() as connection:
            transaction = connection.begin()
            connection.execute(text("insert into subject(\"subject_id\","
            " \"subject_title\") values (:new_id, :new_title)"),
                               {'new_id': id, 'new_title': title})
            transaction.commit()

# Метод, который  запросит у БД значение самого большого ID — ID последней созданной компании (новой).
    def get_max_id(self, id):
        with self.db.connect() as connection:
            transaction = connection.begin()
            result = connection.execute(text("select  MAX(\"subject_id\") from subject"),
                                        {"max_id": id}).fetchall()[0][0]
            transaction.commit()
            return result


# Метод для удаления педмета.
    def delete_subject(self, id):
        with self.db.connect() as connection:
            transaction = connection.begin()
            sql_statement = text("delete from subject where subject_id =:id_to_delete")
            connection.execute(sql_statement, {"id_to_delete": id})
            transaction.commit()


# Метод для редактирования педмета.
    def edit_subject(self, title, id):
        with self.db.connect() as connection:
            transaction = connection.begin()
            sql_statement = (text("update subject set subject_title"
            "=:new_title where subject_id=:id_to_edit"))
            connection.execute(sql_statement, {"new_title":title ,
                                               "id_to_edit": id})
            transaction.commit()


# Метод, который вернет предмет по ID:
    def get_subject_by_id(self, id):
        with self.db.connect() as connection:
            transaction = connection.begin()
            result = connection.execute(text("select * from subject where subject_id =:by_id"),
                                        {"by_id": id}).fetchall()
            transaction.commit()
            return result
