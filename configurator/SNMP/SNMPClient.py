from pysnmp.hlapi import *

class SNMPClient:
    def __init__(self,addr,community):
        self.addr = addr
        self.community = community
        self.oids = [("RAM", "1.3.6.1.4.1.2021.4.5.0"), ("SISTEMA", "1.3.6.1.2.1.1.1.0")]
    def getInventory(self):
        #client= SNMP(self.addr,self.community)
        inventory = "SNMP Summary\n"
        for name, oid in self.oids:
        	inventory += name + " " + self.consultaSNMP(self.community, self.addr, oid) + "\n"
        file = open("inventory"+".txt", "w")
        file.write(inventory)
        file.close()
        print(inventory)
        return inventory

    def consultaSNMP(self, community, host, oid, port = 161):
	    errorIndication, errorStatus, errorIndex, varBinds = next(
	        getCmd(SnmpEngine(),
	               CommunityData(community),
	               UdpTransportTarget((host, port)),
	               ContextData(),
	               ObjectType(ObjectIdentity(oid))))
	    resultado = ""
	    if errorIndication:
	        print(errorIndication)
	    elif errorStatus:
	        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
	    else:
	        for varBind in varBinds:
	            varB=(' = '.join([x.prettyPrint() for x in varBind]))
	            resultado= varB.split()[2]
	    return resultado