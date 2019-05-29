import telnetlib
ASCII="ascii"

class TelnetClient():
    def __init__(self,address,user = 'rcp', passw = 'rcp'):
        self.address = address
        self.user = user
        self.passw = passw
    
    def test(self):
        with telnetlib.Telnet(self.address) as tnSess:
            tnSess.read_until(b"User: ")
            tnSess.write(self.user.encode(ASCII)+b"\n")
            tnSess.write(self.user.encode(ASCII)+b"\n")
            tnSess.write(b"show running-config\n")
            
    def sendCommands(self,commands):
        with telnetlib.Telnet(self.address) as tnSess:
            tnSess.read_until(b"User: ")
            tnSess.write(self.user.encode(ASCII)+b"\n")
            tnSess.write(self.user.encode(ASCII)+b"\n")
            for command in commands:
                tnSess.write(command.encode(ASCII))
            tnSess.write(b"exit\n")
    
    ### interact
    def interact(self):
        with telnetlib.Telnet(self.address) as tnSess:
            tnSess.interact()
                
                
    
    