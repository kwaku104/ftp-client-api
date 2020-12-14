import paramiko

class SFTPModel():

    # def __init__(self, server_ip, user, passwd):
    #     self.ftp = FTP(server_ip)
    #     self.ftp.login(user, passwd)

    def __init__(self, server_ip, user, passwd, port=22):
        self.server_ip = server_ip
        self.user = user
        self.passwd = passwd
        self.transport = paramiko.Transport((self.server_ip, port))
    
    # def __enter__(self):
    #     self.ftp = FTP(self.server_ip)
    #     self.ftp.login(self.user, self.passwd)

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.ftp.quit()
    
    def connect(self):
        self.transport.connect(None, self.user, self.passwd)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        return self.sftp
        

    def disconnect(self):
        if self.sftp:
            self.sftp.close()
        if self.transport:
            self.transport.close()

    def download_file(self, file_path, local_file_path="/default/download/path"):
        self.sftp.get(file_path, local_file_path)
    
    def upload_file(self, file_path, local_file_path="/default/upload/path"):
        self.sftp.put(local_file_path, file_path)