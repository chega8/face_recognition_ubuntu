import postgresql
import psycopg2
import numpy as np
# pq://user:password@host:port/database

class FacesDao:
    def __init__(self):
        pass

    def db_conn(self):
        # return postgresql.open('pq://postgres:chega445@localhost:5432/face_recognition')
        conn = psycopg2.connect(dbname="face_recognition", user="postgres", password="chega445", host="localhost", port="5432")
        cur = conn.cursor()
        return conn, cur

    def insert_code(self, face_vector):
        conn, cur = self.db_conn()
        with conn as con:
            with cur as db:
                db.execute("INSERT INTO codes (code) VALUES (%s) RETURNING id;", (face_vector.tolist(),))
                faces_id = db.fetchone()
                con.commit()
            return faces_id

    def get_codes(self):
        conn, cur = self.db_conn()
        with conn as con:
            with cur as db:
                db.execute("SELECT id, code FROM codes;")
                tuples = db.fetchall()
                faces_and_names = []
                for (id, face_vector) in tuples:
                    faces_and_names.append({"id": id, "face_vector": face_vector})
                con.commit()
                return faces_and_names

    def insert_name(self, name):
        conn, cur = self.db_conn()
        with conn as con:
            with cur as db:
                db.execute("INSERT INTO names (name) VALUES (%s) RETURNING id;", (name,))
                id = db.fetchone()
                con.commit()
            return id

    def get_names(self):
        conn, cur = self.db_conn()
        with conn as con:
            with cur as db:
                db.execute("SELECT id, name FROM names;")
                tuples = db.fetchall()
                faces_and_names = []
                for (id, name) in tuples:
                    faces_and_names.append({"id": id, "name": name})
                con.commit()
                return faces_and_names

    def create_new_table(self, name):
        conn, cur = self.db_conn()
        with conn as con:
            with cur as db:
                if name == "codes":
                    db.execute("CREATE TABLE codes (id serial PRIMARY KEY, code real[]);")
                    con.commit()
                    return True
                elif name == "names":
                    db.execute("CREATE TABLE names (id serial PRIMARY KEY, name varchar(50));")
                    con.commit()
                    return True
        return False

    def drop_table(self, name):
        conn, cur = self.db_conn()
        with conn as con:
            with cur as db:
                if name == "codes":
                    db.execute("DROP TABLE codes;")
                    con.commit()
                    return True
                elif name == "names":
                    db.execute("DROP TABLE names;")
                    con.commit()
                    return True
        return False


    # def insert_code(self, face_vector):
    #     with self.db_conn() as db:
    #         insert = db.prepare(
    #             "INSERT INTO codes (code) VALUES ($1) " +
    #             "RETURNING id")
    #         [(faces_id,)] = insert(face_vector)
    #         return faces_id
    #
    # def get_codes(self):
    #     with self.db_conn() as db:
    #         tuples = db.query("SELECT id, code FROM codes")
    #         faces_and_names = []
    #         for (id, face_vector) in tuples:
    #             faces_and_names.append({"id": id, "face_vector": face_vector})
    #         return faces_and_names
    #
    # def insert_name(self, name):
    #     with self.db_conn() as db:
    #         insert = db.prepare(
    #             "INSERT INTO names (name) VALUES ($1) " +
    #             "RETURNING id")
    #         [(faces_id,)] = insert(name)
    #         return faces_id
    #
    # def get_names(self):
    #     with self.db_conn() as db:
    #         tuples = db.query("SELECT id, name FROM names")
    #         faces_and_names = []
    #         for (id, name) in tuples:
    #             faces_and_names.append({"id": id, "name": name})
    #         return faces_and_names
