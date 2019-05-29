

class SNMPClient():
    def __init__(self,addr,community):
        self.addr=addr
        self.community=community
        
    def getInventory(self):
        #client= SNMP(self.addr,self.community)
        pass