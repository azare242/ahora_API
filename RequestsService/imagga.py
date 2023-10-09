from ahora_API.settings import IMAGGA_API_KEY, IMAGGA_AUTH, IMAGGA_SECRET_KEY
import requests



class Imagga_Request:
    def __init__(self):
        self.__auth = (IMAGGA_API_KEY, IMAGGA_SECRET_KEY)
        self.__detection = 'https://api.imagga.com/v2/faces/detections?return_face_id=1'
        self.__similarity = 'https://api.imagga.com/v2/faces/similarity?face_id=%s&second_face_id=%s'
        
    def detect(self, image):
        # print(image)
        res = requests.post(
            self.__detection,
            auth=self.__auth,
            files={'image': image},
            
        ).json()
        confidence = res['result']['faces'][0]['confidence']
        face_id = res['result']['faces'][0]['face_id']
        # print((confidence, face_id))
        return (confidence, face_id)
        
        
    def similarity(self, face_id1, face_id2):
        res = requests.get(
            self.__similarity % (face_id1, face_id2),
            auth=self.__auth,
        ).json()
        
        return res['result']['score']