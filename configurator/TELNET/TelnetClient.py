import telnetlib
ASCII="ascii"

class TelnetClient():
    """
        Telnet Client
    """
    def __init__(self,address,user = 'rcp', passw = 'rcp'):
        self.address = address
        self.user = user
        self.passw = passw
    
    def test(self):
        """Tests the telnet connection
        """
        with telnetlib.Telnet(self.address) as tnSess:
            tnSess.read_until(b"User: ")
            tnSess.write(self.user.encode(ASCII)+b"\n")
            tnSess.write(self.user.encode(ASCII)+b"\n")
            tnSess.write(b"show running-config\n")
            
    def sendCommands(self,commands):
        """ execute a list of commands in a given router
        
        Arguments:
            commands {[string]} -- an array of strings of the commands to be executed
        """
        with telnetlib.Telnet(self.address) as tnSess:
            tnSess.read_until(b"User: ")
            tnSess.write(self.user.encode(ASCII)+b"\n")
            tnSess.write(self.user.encode(ASCII)+b"\n")
            for command in commands:
                tnSess.write(command.encode(ASCII))
            tnSess.write(b"exit\n")
    
    
    def interact(self):
        """ 
        Open a telnet console of the router at <address>
        """
        with telnetlib.Telnet(self.address) as tnSess:
            tnSess.interact()
                
                
    
    