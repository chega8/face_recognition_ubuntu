import face_recognition
import numpy as np


# Модель распознавания лиц
class Model:
    def __init__(self):
        self.frame = None

    def set_data(self, data):
        # нейросеть может работать только с uint8, потратил два дня чтобы узнать это
        self.frame = np.array(data).astype('uint8')

    @staticmethod
    def get_face_encodings(image):
        return face_recognition.face_encodings(image)

    @staticmethod
    def get_image_from_path(path):
        return face_recognition.load_image_file(path)

    # Возвращает кодировки всех лиц на фрейме
    def get_face_encodings_yet(self):
        self.frame = self.frame
        face_locations = face_recognition.face_locations(self.frame)
        return face_recognition.face_encodings(self.frame, face_locations, num_jitters=1)

    def get_faces_and_unknown_encoding(self, face_encodings, known_encodings_from_db, known_face_names_from_db):

        face_names = []
        unknown_encoding = []

        for face_encoding in face_encodings:
            # Массив флагов, есть ли лица в бд
            matches = face_recognition.compare_faces(known_encodings_from_db, face_encoding)
            name = ''

            # known_inexes = []
            # unknown_indexes = []
            # for i, m in enumerate(matches):
            #     if m:
            #         known_inexes.append(i)
            #     else:
            #         unknown_indexes.append(i)

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_encodings_from_db, face_encoding)

            try:
                # Индекс минимальной дистанции из всех сравнений
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names_from_db[best_match_index]
                else:
                    unknown_encoding.append(face_encoding)
            except IndexError:
                pass

            face_names.append(name)

        return face_names, unknown_encoding
