import logging

from dao.FacesDao import FacesDao
from utils.model import Model


class FaceService:
    def __init__(self):
        self.faces_dao = FacesDao()
        self.model = Model()

    def get_known_names(self, js):
        self.model.set_data(js['frame'])

        try:
            face_encodings = self.model.get_face_encodings_yet()
        except Exception:
            face_encodings = None

        if face_encodings is None or face_encodings == []:
            logging.info("No faces at frame")
            # print("No faces at frame")
            return face_encodings
        else:
            # Берем данные из бдшки
            codes = self.faces_dao.get_codes()
            names = self.faces_dao.get_names()
            known_encodings_from_db, known_face_names_from_db = [], []

            l = len(names)
            for i, code in enumerate(codes):
                known_encodings_from_db.append(code['face_vector'])
                if i < l:
                    known_face_names_from_db.append(names[i]['name'])

            face_names, unknown_encoding = self.model.get_faces_and_unknown_encoding(face_encodings,
                                                                                     known_encodings_from_db,
                                                                                     known_face_names_from_db)

            if face_names == ['']:
                logging.info("Found unknown persons")
                for i in unknown_encoding:
                    new_id = self.faces_dao.insert_code(i)
                    logging.info("New encode saved by id %id" % new_id)

            return face_names
