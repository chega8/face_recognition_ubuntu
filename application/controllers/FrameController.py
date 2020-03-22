from services.FaceService import FaceService


class FrameController:
    def __init__(self):
        self.face_service = FaceService()

    def post_frame(self, js):

        return self.face_service.get_known_names(js)
