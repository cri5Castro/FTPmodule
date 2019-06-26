# RouterConfigurator
___
Python tool to configure Routers and get their configurations 

### Usage:

```bash
python -m configurator <command> <options>*
``` 
- upload (up)         upload a file to a FTP SERVER with address <addr>
- download (dw, down) : download a file from a FTP SERVER with address <addr>
- list (l): list all files in a directory <path> from a FTP SERVER <addr>
- interact (int): connects to a remote terminal using telnet
- getInventory (getInv):
 get the system information of a SNMP agent

- configure (config, c): upload a startup config file to a FTP SERVER with address <addr>

- getConfiguration (gc, getconfig) download the startup-config file from a FTP SERVER with address <addr>

optional arguments:
  -h, --help            show this help message and exit

**Requeriments**
- ftplib
- telnetlib
- pysnmp
