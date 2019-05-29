
#!/usr/bin/python3
import argparse
import sys
from .FTP import FTPclient
from .TELNET import TelnetClient
"""
reconbrar configure y getconfiguration a upload y download 
y en sulgar implenetar un script que suba el archivo y que usando telnet lo ponga como running config
y vicevers usando telnet generar startup congif usando copy y descargarlo


"""

def interactTelnet(options):
    client=TelnetClient(options.addr,options.user,options.password)
    client.interact()
    
    
def listFiles(options):
    print('running listFiles', options)
    client = FTPclient(options.addr,options.user,options.password)
    client.listDirectory(options.path)
    

def upload(options):
    print('uploading file to server at ',options.addr)
    client = FTPclient(options.addr,options.user,options.password)
    client.sendFile(options.ipath,options.opath)
    

def download(options):
    print('Downloading file from server at ',options.addr)
    client = FTPclient(options.addr,options.user,options.password)
    client.getFile(options.ipath,options.opath)
    
def configure(options):
    pass

def getConfiguration(options):
    pass
    
def getInventory(options):
    pass

def run(args):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Create a upload subcommand    
    parser_upload = subparsers.add_parser('upload',aliases=["up"], help='upload a file to a FTP SERVER with address <addr>')
    parser_upload.add_argument('addr',help="ip address to connect with")
    parser_upload.add_argument('-ipath', '-i', help="Path of the file to be sent",default='startup-config')
    parser_upload.add_argument('-opath', '-o', help="Path to store the file",default='startup-config')
    parser_upload.add_argument('-user','-u',help="FTP user",default="rcp")
    parser_upload.add_argument('-password','-p',help="FTP password",default="rcp")
    parser_upload.set_defaults(func=upload)
    
    #create a downloa subcommand
    parser_download = subparsers.add_parser('download',aliases=["dw","down"],help='download  a file from a FTP SERVER with address <addr>')
    parser_download.add_argument('addr',help="ip address to connect with")
    parser_download.add_argument('-ipath', '-i', help="Path to store the file",default='startup-config')
    parser_download.add_argument('-opath', '-o', help="Path to the desired file",default='startup-config')
    parser_download.add_argument('-user','-u',help="FTP user",default="rcp")
    parser_download.add_argument('-password','-p',help="FTP password",default="rcp")
    parser_download.set_defaults(func=download)
    
    # Create a listapps subcommand       
    parser_listFiles = subparsers.add_parser('list',aliases=["l"], help='list all files in a directory <path> from a FTP SERVER <addr>')
    parser_listFiles.add_argument('addr',help="ip address to connect with")
    parser_listFiles.add_argument('-user','-u',help="FTP user",default="rcp")
    parser_listFiles.add_argument('-password','-p',help="FTP password",default="rcp")
    parser_listFiles.add_argument('-path',help="Path to be listed",default="")
    parser_listFiles.set_defaults(func=listFiles)
    
    # Create a interact subcommand       
    parser_interact = subparsers.add_parser('interact',aliases=["int"], help='connects to a remote terminal using telnet')
    parser_interact.add_argument('addr',help="ip address to connect with")
    parser_interact.add_argument('-user','-u',help="Telnet user",default="rcp")
    parser_interact.add_argument('-password','-p',help="Telnet password",default="rcp")
    parser_interact.set_defaults(func=interactTelnet)
    
    
    #TODO juanito 
    # Create a interact inventory       
    parser_getInventory = subparsers.add_parser('getInventory',aliases=["getInv"], help='get the system information of a SNMP agent')
    parser_getInventory.add_argument('addr',help="ip address to connect with")
    parser_getInventory.add_argument('com',help="snmp community of the agent",default="rcp")
    parser_getInventory.set_defaults(func=getInventory)
    
    
    
    if len(sys.argv) <= 1:
        sys.argv.append('--help')
    options = parser.parse_args()
    options.func(options)
