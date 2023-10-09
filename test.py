import json
x = '{"result": {'aces': [{'attributes': [], 'confidence': 99.9994735717773, 'coordinates': {'height': 487, 'width': 487, 'xmax': 1010, 'xmin': 523, 'ymax': 612, 'ymin': 125}, 'face_id': '5ddd8f355dfd1c134272c432348e20775866314d7e7db972f30a3911efadc641', 'landmarks': []}]}, 'status': {'text': '', 'type': 'success'}}'

print(json.loads(x))