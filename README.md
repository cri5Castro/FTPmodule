# FTPmodule
___
Python FTPclient to configure Routers and get their configurations 

### Usage:

```bash
python -m configurator <command> <options>*
```
### configure:
 Configure a router (uploads a file to a FTP server)
```bash
python configurator configure <ipaddress> [-h] [-ipath IPATH] [-opath OPATH]
```

```
positional arguments:
  addr                  ip address to connect with

optional arguments:
    -h, --help          show this help message and exit
  -ipath IPATH, -i IPATH
                        Path of the file to be sent
  -opath OPATH, -o OPATH
                        Path to store the file
```

### getConfigure:
get the configuration file of a router. (downloads a file from a FTP server)

```bash
python -m configurator getConfiguration <ipaddress> [-h] [-ipath IPATH] [-opath OPATH]
```

```
positional arguments:
  addr                  ip address to connect with

optional arguments:
  -h, --help            show this help message and exit
  -ipath IPATH, -i IPATH
                        Path to store the file
  -opath OPATH, -o OPATH
                        Path of the desired file
```
### list:
list the files of a directory in a FTP server

```
python -m configurator list <ipaddress> [-h] [-user USER] [-password PASSWORD] [-path PATH]

```
```
positional arguments:
  addr                  ip address to connect with

optional arguments:
  -h, --help            show this help message and exit
  -user USER, -u USER   FTP user
  -password PASSWORD, -p PASSWORD
                        FTP password
  -path PATH            Path to be listed
```