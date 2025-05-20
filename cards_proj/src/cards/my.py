import my2
from unittest import mock

class MyClass:
    def __init__(self, my_attribute: str):
        self._my_attribute = my_attribute
        self._db = (self._my_attribute + ".my_db")

    def db_path(self):
        return "C:/" + self._db


a = MyClass("fake/path")
# Mock instance of class
with mock.patch.object(a, "_db", "mock/path"):
    print(a.db_path())

# Mock variable in imported file
with mock.patch.object(my2, "hello", "Kirill"):
    print(my2.hello)

# Mock class method return value
with mock.patch.object(MyClass, "db_path") as mock_only_method:
    mock_only_method.return_value = "E:/mock/path/fake"
    b = MyClass("some/path")
    print(b.db_path())

# Mock class and its methods
with mock.patch.object(my2, "MyClass2") as FullClassMock:
    FullClassMock.return_value.connection_ports.return_value = "8000:80"
    c = my2.MyClass2(999)
    print(c.connection_ports())
    print(my2.MyClass2(123).connection_ports())

    FullClassMock.return_value.connection_ports.assert_called()

