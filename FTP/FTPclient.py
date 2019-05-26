#!/usr/bin/python3
import ftplib
import os

STOR="STOR "
LS="LIST"
RETR="RETR "


class FTPclient():
    """
    FTP client
    """
    def __init__(self, address, user = 'rcp', passw = 'rcp'):
        """
        Arguments: 
            address {str} -- [address  of the FTP SERVER] 
        Keyword Arguments:
            user {str} -- [user to access FTP SERVER] (default: {'rcp'})
            passw {str} -- [passw to access FTP SERVER] (default: {'rcp'})
        """
        self.address = address
        self.user = user
        self.passw = passw
        

    def sendFile(self, ipath,opath=None):
        """
        Sends a file from our client to the FTP server.
        Arguments:
            ipath {str} -- [Path of the file to be sent]
        
        Keyword Arguments:
            opath {str} -- [Output Path in the FTP Server] (default: {ipath})
        """
        with ftplib.FTP(self.address) as ftp: 
            try:    
                ftp.login(self.user,self.passw)
                with open(ipath, 'rb') as fp: #open file to be uploaded
                    res = ftp.storlines(STOR + (opath if opath else ipath), fp)
                    if not res.startswith('226 Transfer complete'):
                        print('Upload failed')
            except ftplib.all_errors as e:
                print('FTP error:', e)
    
    def getFile(self, ipath,opath):
        """
        Retrieves a File from the FTP server to our computer.
        Arguments:
            ipath {str} -- [path of the origin file from the FTP SERVER]
            opath {str} -- [destination path]
        """
        with ftplib.FTP(self.address) as ftp:
            try:
                ftp.login(self.user,self.passw)
                with open(opath, 'w') as fp: #creating a file to store the desired file
                    res = ftp.retrlines( RETR + ipath, fp.write) #retriving file from FTP SERVER
                    if not res.startswith('226 Transfer complete'):
                        print('Download failed')
                        if os.path.isfile(opath):
                            os.remove(opath)
            except ftplib.all_errors as e:
                print('FTP error:', e) 


    def listDirectory(self,path=''):
        """[summary]
        
        Keyword Arguments:
            path {str} -- [description] (default: {''})
        """
        with ftplib.FTP(self.address) as ftp:
            try:
                ftp.login(self.user,self.passw)
                res = ftp.retrlines(LS)
                if not res.starswith('226 Directory send OK'):
                    print('Failed while trying to list files')
            except ftplib.all_errors as e:
                print('FTP error:', e)