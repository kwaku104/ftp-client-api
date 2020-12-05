from ftplib import FTP

class FTPModel():

    # def __init__(self, server_ip, user, passwd):
    #     self.ftp = FTP(server_ip)
    #     self.ftp.login(user, passwd)

    def __init__(self, server_ip, user, passwd):
        self.server_ip = server_ip
        self.user = user
        self.passwd = passwd
    
    # def __enter__(self):
    #     self.ftp = FTP(self.server_ip)
    #     self.ftp.login(self.user, self.passwd)

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.ftp.quit()
    
    def connect(self):
        self.ftp = FTP(self.server_ip)
        self.ftp.login(self.user, self.passwd)
        return self.ftp
        

    def disconnect(self):
        self.ftp.quit()


    def download_file(self, file_name):
        localfile = open(file_name, 'wb')
        self.ftp.retrbinary('RETR ' + file_name, localfile.write, 1024)

        localfile.close()
    
    def upload_file(self, file_name):
        self.ftp.storbinary('STOR '+file_name, open(file_name, 'rb'))