import json
import unittest
import logging
import face_recognition

from application.dao.FacesDao import FacesDao
from application.utils.model import Model


class FaceComparerTest(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        self.known_encodings_from_db = []
        self.known_face_names_from_db = ["Sasha", "Sasha", "Pasha", "Pasha"]

        with open('C:\\Users\\user\\Desktop\\face_recognition\\simulations\\known_encodings_bd.json', "r") as f:
            self.known_encodings_from_db.append(json.loads(f.readline()))
            self.known_encodings_from_db.append(json.loads(f.readline()))
            self.known_encodings_from_db.append(json.loads(f.readline()))
            self.known_encodings_from_db.append(json.loads(f.readline()))
        # known_encodings_from_db shape [4x128]

        image_frame = face_recognition.load_image_file(
            "C:\\Users\\user\\Desktop\\fACE recognition\\data\\" + "pasha4.jpg")
        # self.monitor.consume(image_frame)
        # self.monitor.controller_init()
        self.model.set_data(image_frame)

    def test_put_Angelina_Pasha_Sasha_return_Pasha_Sasha(self):
        face_names, unknown_encodings = self.model.get_faces_and_unknown_encoding(self.known_encodings_from_db,
                                                                                  self.known_face_names_from_db)
        expected = "Sasha" in face_names and "Pasha" in face_names
        print(unknown_encodings)
        self.assertTrue(expected)

    def test_put_Angelina_Pasha_Sasha_return_1_unknown_encode(self):
        face_names, unknown_encodings = self.model.get_faces_and_unknown_encoding(self.known_encodings_from_db,
                                                                                  self.known_face_names_from_db)
        actual = len(unknown_encodings) == 1
        self.assertTrue(actual)

    def test_log(self):
        # logging.basicConfig(filename="sample.log", level=logging.INFO)

        logging.debug("This is a debug message")
        logging.info("Informational message")
        logging.error("An error has happened!")

    # def test_insert_in_bd(self):
    #     dao = FacesDao()
    #
    #     dao.insert_face(self.known_encodings_from_db[0], "Sasha")
    #     dao.insert_face(self.known_encodings_from_db[1], "Sasha")
    #     dao.insert_face(self.known_encodings_from_db[2], "Pasha")
    #     dao.insert_face(self.known_encodings_from_db[3], "Pasha")

