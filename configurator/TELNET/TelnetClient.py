import telnetlib
ASCII="ascii"
class Telnetclient():
    def __init__(self,address,user = 'rcp', passw = 'rcp'):
        self.address = address
        self.user = user
        self.passw = passw
    
    def test():
        with telnetlib.Telnet(self.address) as tnSess:
            tnSess.read_until(b"User: ")
            tnSess.write(user.encode(ASCII)+b"\n")
            tnSess.write(user.encode(ASCII)+b"\n")
            tnSess.write(b"show running-config\n")
            
    def sendCommands(commands):
        with telnetlib.Telnet(self.address) as tnSess:
            tnSess.read_until(b"User: ")
            tnSess.write(user.encode(ASCII)+b"\n")
            tnSess.write(user.encode(ASCII)+b"\n")
            for i in commands:
                tnSess.write(commands.encode(ASCII))
            tn.write(b"exit\n")
    
    ### interact
            
                
    
    