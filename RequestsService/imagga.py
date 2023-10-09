from ahora_API.settings import IMAGGA_API_KEY, IMAGGA_AUTH, IMAGGA_SECRET_KEY
import requests


import requests

class Imagga_Request:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Imagga_Request, cls).__new__(cls)
            cls._instance.__auth = (IMAGGA_API_KEY, IMAGGA_SECRET_KEY)
            cls._instance.__detection = 'https://api.imagga.com/v2/faces/detections?return_face_id=1'
            cls._instance.__similarity = 'https://api.imagga.com/v2/faces/similarity?face_id=%s&second_face_id=%s'
        return cls._instance

    def detect(self, image):
        res = requests.post(
            self.__detection,
            auth=self.__auth,
            files={'image': image},
        ).json()
        confidence = res['result']['faces'][0]['confidence']
        face_id = res['result']['faces'][0]['face_id']
        return (confidence, face_id)

    def similarity(self, face_id1, face_id2):
        res = requests.get(
            self.__similarity % (face_id1, face_id2),
            auth=self.__auth,
        ).json()

        return res['result']['score']
