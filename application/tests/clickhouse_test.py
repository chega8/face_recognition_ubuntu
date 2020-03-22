import unittest

from clickhouse_driver import Client

from application.utils.model import Model


class ClickhouseTest(unittest.TestCase):
    def setUp(self):
        self.client = Client('localhost')

    def test_execute_data_return_date_and_version(self):
        result = self.client.execute('SELECT now(), version()')
        print("RESULT: {0}: {1}".format(type(result), result))
        for t in result:
            print(" ROW: {0}: {1}".format(type(t), t))
            for v in t:
                print("  COLUMN: {0}: {1}".format(type(v), v))

    def test_show_databases(self):
        client = Client(host='localhost')
        print(client.execute('SHOW DATABASES'))

    def test_create_new_table(self):
        self.client.execute(
            'CREATE TABLE face_recognition_test.faces (id Int32, name String, facevector Array(Float32)) ENGINE = Memory')

    def test_insert_data(self):
        _id = 1
        _name = "Me"
        _code = \
        Model.get_face_encodings_yet(Model.get_image_from_path("C:/Users/user/Desktop/fACE recognition/data/me.jpg"))[0]
        self.client.execute('INSERT INTO face_recognition_test.faces (id, name, facevector) VALUES',
                            [[_id, _name, _code]])

    def test_select(self):
        self.client.execute('SELECT * FROM face_recognition_test.faces')
