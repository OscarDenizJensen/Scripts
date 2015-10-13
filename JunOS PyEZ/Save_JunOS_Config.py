from jnpr.junos import Device

dev = Device(host='192.168.56.2', user='root', password='Juniper1')
#192.168.56.2
dev.open()

class Create_Config():
    def __init__(self):
        config=str(self.get_conf())

        file_name=raw_input("Enter File Name: ")

        with open(file_name, "w") as text_file:
                text_file.write(config)
                text_file.close()

    def get_conf(self):
        return dev.cli("show configuration")


run=Create_Config()