import os
import json
import uuid
from settings import settings

class settings_manager(object):
    __file_name = "settings.json"
    __unique_number = 1
    __data = {}
    __settings = settings()

    # Функция для создания экземляра класса и контроль, того, что у нас он будет только один
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance


    def __init__(self) -> None:
        self.__unique_number = uuid.uuid4()

    # Свойство для получения уникального номера (значения) в формате строки
    @property
    def unique_number(self) -> str:
        return str(self.__unique_number.hex)

    # Функция для открытия файла с настройками по указанному пути
    # Идет проверка на ошибки при подаче аргумента,
    # а потом все уходит в приватную функцию open
    def opener(self, file_name: str) -> bool:
        if not isinstance(file_name, str):
            raise Exception("ERROR: неправильный аргумент!")

        if file_name == "":
            raise Exception("ERROR: Неправильный аргумент!!")

        self.__file_name = file_name.strip()

        try:
            self.__open()
        except:
            return False

        return True

    # Функция для получения словаря с настройками считанными из файла с настройками
    @property
    def data(self) -> {}:
        return self.__data

    # Приватная функция для создания экземляра класса settings
    def __convert(self):

        #Если данных вообще нет
        if len(self.__data) == 0:
            raise Exception("Проблема с созданием экземпляра класса settings")

        fields = self.__settings.get_data_keys

        # если данные есть, но они неполные, то мы счтиатем то что есть, но выкинем Exception
        if len(self.__data) < len(fields):
            for field in fields:
                if field in self.__data:
                    value = self.__data[field]
                    setattr(self.__settings, field, value)
            raise Exception("Входных данных меньше ожидаемых, некоторые поля пустые")

        # Иначе мы просто заполняем все поля без лишних логических сравнений в if
        else:
            for field in fields:
                value = self.__data[field]
                setattr(self.__settings, field, value)

    # Приватное свойство для отрытия файла
    @property
    def __open(self):
        # Используем os.path для построения путей
        file_path = os.path.split(__file__)
        settings_file = "%s/%s" % (file_path[0], self.__file_name)
        if not os.path.exists(settings_file):
            raise Exception(
                "ERROR: Неправильный аргумент",
                settings_file)

        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)
            self.__convert()
            print(self.__data)

