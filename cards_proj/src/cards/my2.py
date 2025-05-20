
hello = "World"

class MyClass2:
    def __init__(self, my_attribute: int):
        self._port = my_attribute

    def connection_ports(self):
        return "8000:"+str(self._port)