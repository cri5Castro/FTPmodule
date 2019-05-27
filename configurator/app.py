
#!/usr/bin/python3
import argparse
import sys
from .FTP import FTPclient


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
    

def run(args):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Create a configure subcommand    
    parser_configure = subparsers.add_parser('configure',aliases=["c","config"], help='configure router with address <addr>')
    parser_configure.add_argument('addr',help="ip address to connect with")
    parser_configure.add_argument('-ipath', '-i', help="Path of the file to be sent",default='startup-config')
    parser_configure.add_argument('-opath', '-o', help="Path to store the file",default='startup-config')
    parser_configure.set_defaults(func=upload)
    
    #create a getConfiguration subcommand
    parser_getConfiguration = subparsers.add_parser('getConfiguration',
                                                    aliases=["gc","gconfig"],
                                                    help='get the coniguration file of the router with address <addr>')
    parser_getConfiguration.add_argument('addr',help="ip address to connect with")
    parser_getConfiguration.add_argument('-ipath', '-i', help="Path to store the file",default='startup-config')
    parser_getConfiguration.add_argument('-opath', '-o', help="Path to the desired file",default='startup-config')
    parser_getConfiguration.set_defaults(func=download)
    
    # Create a listapps subcommand       
    parser_listFiles = subparsers.add_parser('list',aliases=["l"], help='list all files in a directory')
    parser_listFiles.add_argument('addr',help="ip address to connect with")
    parser_listFiles.add_argument('-user','-u',help="FTP user",default="rcp")
    parser_listFiles.add_argument('-password','-p',help="FTP password",default="rcp")
    parser_listFiles.add_argument('-path',help="Path to be listed",default="")
    parser_listFiles.set_defaults(func=listFiles)
    
    if len(sys.argv) <= 1:
        sys.argv.append('--help')
    options = parser.parse_args()
    options.func(options)
