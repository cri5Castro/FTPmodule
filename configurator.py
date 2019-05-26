
#!/usr/bin/python3
import argparse
import sys
from FTP import FTPclient
def configure(options):
    print('configuring router at ',options.addr)

def getConfiguration(options):
    print("Retriving configuration File from ",options.addr)

def listFiles(options):
    
    client = FTPclient(options.addr,options.user,options.password)
    client.listDirectory(options.path)
    print('running listFiles', options)
    

def main(args):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Create a configure subcommand    
    parser_configure = subparsers.add_parser('configure',aliases=["c","config"], help='configure router with address <addr>')
    parser_configure.add_argument('addr',help="ip address to connect with")
    parser_configure.set_defaults(func=configure)
    
    #create a getConfiguration subcommand
    parser_getConfiguration = subparsers.add_parser('getConfiguration', help='configure router with address <addr>')
    parser_getConfiguration.add_argument('addr',help="ip address to connect with")
    parser_getConfiguration.set_defaults(func=getConfiguration)


    # Create a listapps subcommand       
    parser_listFiles = subparsers.add_parser('list', help='list all files in a directory')
    parser_listFiles.add_argument('addr',help="ip address to connect with")
    parser_listFiles.add_argument('-user','-u',help="FTP user",default="rcp")
    parser_listFiles.add_argument('-password','-p',help="FTP password",default="rcp")
    parser_listFiles.add_argument('-path',help="Path to be listed",default="")
    parser_listFiles.set_defaults(func=listFiles)
    
    if len(sys.argv) <= 1:
        sys.argv.append('--help')
    options = parser.parse_args()
    options.func(options)


if __name__ == "__main__":
    main(sys.argv[1:])
    