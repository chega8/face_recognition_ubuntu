import unittest
from PIL import Image
from application.dao import FacesDao
import application.utils.model as model
import numpy as np


class MyTestCase(unittest.TestCase):

    def test_something(self):
        image = Image.open("/home/chega/Рабочий стол/face_recognition/indor-face_recognition/application/tests/simulations/data/me2.jpg")
        name = "Aleksandr"

        dao = FacesDao.FacesDao()
        vector = model.Model().get_face_encodings(np.array(image).astype('uint8'))

        print(dao.insert_code(vector[0]))
        dao.insert_name(name)

        # self.assertEqual(True, False)

    def test_get_data(self):
        dao = FacesDao.FacesDao()
        print(dao.get_codes())


if __name__ == '__main__':
    unittest.main()
