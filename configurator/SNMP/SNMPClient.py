from pysnmp.hlapi import *

class SNMPClient:
    def __init__(self,addr,community):
        self.addr = addr
        self.community = community

        self.oids = [("SISTEMA", "1.3.6.1.2.1.1.1.0"),
			("Total RAM in machine", "1.3.6.1.4.1.2021.4.5.0"), ("Total RAM used:", "1.3.6.1.4.1.2021.4.6.0"),
			("Total RAM Free:", "1.3.6.1.4.1.2021.4.11.0"),
        ("TIMEUP", "1.3.6.1.2.1.25.1.1.0")]
    def getInventory(self):
        #client= SNMP(self.addr,self.community)
        inventory = "SNMP Summary\n"
        for name, oid in self.oids:
        	inventory += name + " " + self.consultaSNMP(self.community, self.addr, oid) + "\n"
        name = self.addr.replace(".", "")
        file = open(name+".txt", "w")
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
