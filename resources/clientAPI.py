from flask_restful import Resource, reqparse
from models.clientAPI import FTPModel

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('user',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
_user_parser.add_argument('serverip',
                        type=str,
                        required=True,
                        help="This field cannot be blank." 
                            )
_user_parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank." 
                            )

_upload_parser = reqparse.RequestParser()
_upload_parser.add_argument('file_name',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

class FTPConnect(Resource):
    def post(self):
        data = _user_parser.parse_args()
        self.ftp_client = FTPModel(data['serverip'], data['user'], data['password'])
        self.ftp_client = self.ftp_client.connect()
        return {'message':'Connection successful'}, 200

    def pass_connection(self):
        return self.ftp_client

class FTPResource(Resource):
    @classmethod
    def get(cls, file_name):
        ftp_client = FTPConnect.pass_connection()
        
        if ftp_client.download_file(file_name):
            return {'message': '{} downloaded successfully'.format(file_name)}, 200
        return {'message': 'Error occurred'}, 500

    @classmethod
    def post(cls, file_name):
        ftp_client = FTPConnect.pass_connection()
        
        data = _upload_parser.parse_args()

        if ftp_client.upload_file(data['file_name']):
            return {'message':'{} uploaded successfully'.format(data['file_name'])}, 201
        return {'message': 'Error occurred'}, 500


    @classmethod
    def delete(cls,):
        pass

