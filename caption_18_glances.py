# glances -s

import xmlrpclib
s = xmlrpclib.ServerProxy('http://localhost:61209')
print s.getAllPlugins()
print s.getAll()
print s.getCpu()
print s.getLoad()
