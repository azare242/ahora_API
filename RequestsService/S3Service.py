import boto3

from botocore.exceptions import ClientError
#import logging
from ahora_API.settings import S3_ACCESS_KEY, S3_SECRET_KEY, S3_ENDPOINT

import boto3

class S3:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(S3, cls).__new__(cls)
            try:
                cls._instance.resource = boto3.resource(
                    's3',
                    endpoint_url=S3_ENDPOINT,
                    aws_access_key_id=S3_ACCESS_KEY,
                    aws_secret_access_key=S3_SECRET_KEY
                )
            except:
                raise Exception("Can not connect to S3")
        return cls._instance

    def insert_object(self, img_path):
        path = "./staticfiles/web/media/" + img_path
        print(img_path.split('/')[-1])
        try:
            bucket = self.resource.Bucket('cloudhw-ahora')
            with open(path, 'rb') as file:
                bucket.put_object(
                    ACL='private',
                    Body=file,
                    Key=img_path.split('/')[-1]
                )
        except Exception as exc:
            raise Exception("error")

        return "DONE"

    def get_object(self, key):
        path = './staticfiles/web/media/downloaded/' + key
        try:
            bucket = self.resource.Bucket('cloudhw-ahora')
            bucket.download_file(
                key,
                path
            )

            return open(path, 'rb')
        except Exception as exc:
            print(exc)
            raise Exception("error")
