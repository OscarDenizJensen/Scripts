from jnpr.junos import Device
dev = Device(host="192.168.56.2", user='root', passwd='Juniper1')
dev.open()

config = dev.rpc.get_config()

from lxml import etree

f = open('config.xml', 'w')
f.write(etree.tostring(config))
f.close()

dev.close()