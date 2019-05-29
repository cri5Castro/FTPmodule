
#!/usr/bin/python3
import argparse
import sys
from .FTP import FTPclient
from .TELNET import TelnetClient
from .SNMP import SNMPClient
"""
reconbrar configure y getconfiguration a upload y download 
y en sulgar implenetar un script que suba el archivo y que usando telnet lo ponga como running config
y vicevers usando telnet generar startup congif usando copy y descargarlo


"""
GENERATE_CONFIG=["enable","copy run start"]

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
    print(f'Configuring router at {options.addr}')
    upload(options)
    print("restart router to apply configuration")


def getConfiguration(options):#TODO
    print(f'get configuration of router at {options.addr}')
    clientTn = TelnetClient(options.addr,options.user,options.password)
    clientTn.sendCommands(GENERATE_CONFIG)
    download(options)
    
def getInventory(options):
    print(f'Generating Inventory for addr: {options.addr} community: {options.com}')
    client  = SNMPClient(options.addr,options.com)
    client.getInventory()

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

    # Create a configure subcommand    
    parser_configure = subparsers.add_parser('configure',aliases=["config","c"], help='upload a startup config file to a FTP SERVER with address <addr>')
    parser_configure.add_argument('addr',help="ip address to connect with")
    parser_configure.add_argument('-ipath', '-i', help="Path of the file to be sent",default='startup-config')
    parser_configure.add_argument('-opath', '-o', help="Path to store the file",default='startup-config')
    parser_configure.add_argument('-user','-u',help="FTP user",default="rcp")
    parser_configure.add_argument('-password','-p',help="FTP password",default="rcp")
    parser_configure.set_defaults(func=configure)
    
    #create getConfiguration subcommand
    parser_getConfiguration = subparsers.add_parser('getConfiguration',aliases=["gc","getconfig"],help='download  the startup-config file from a FTP SERVER with address <addr>')
    parser_getConfiguration.add_argument('addr',help="ip address to connect with")
    parser_getConfiguration.add_argument('-ipath', '-i', help="Path to store the file",default='startup-config')
    parser_getConfiguration.add_argument('-opath', '-o', help="Path to the desired file",default='startup-config')
    parser_getConfiguration.add_argument('-user','-u',help="FTP user",default="rcp")
    parser_getConfiguration.add_argument('-password','-p',help="FTP password",default="rcp")
    parser_getConfiguration.set_defaults(func=getConfiguration)
    
    
    
    if len(sys.argv) <= 1:
        sys.argv.append('--help')
    options = parser.parse_args()
    options.func(options)
