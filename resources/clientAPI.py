from flask_restful import Resource, reqparse
from models.clientAPI import SFTPModel

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

class SFTPConnect(Resource):
    def post(self):
        data = _user_parser.parse_args()
        self.sftp_client = SFTPModel(data['serverip'], data['user'], data['password'])
        self.sftp_client = self.sftp_client.connect()
        return {'message':'Connection successful'}, 200

    def pass_connection(self):
        return self.sftp_client

class SFTPResource(Resource):
    @classmethod
    def get(cls, file_path):
        sftp_client = SFTPConnect.pass_connection()
        
        if sftp_client.download_file(file_path):
            return {'message': '{} downloaded successfully'.format(file_path)}, 200
        return {'message': 'Error occurred'}, 500

    @classmethod
    def post(cls, file_path):
        sftp_client = SFTPConnect.pass_connection()
        
        data = _upload_parser.parse_args()

        if sftp_client.upload_file(data['file_path']):
            return {'message':'{} uploaded successfully'.format(data['file_path'])}, 201
        return {'message': 'Error occurred'}, 500


    @classmethod
    def delete(cls,):
        pass

