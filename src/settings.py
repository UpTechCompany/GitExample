from errors import error_proxy
class settings:
    def __init__(self):
        self.__name = ""
        self.__inn = ""
        self.__check = ""
        self.__corr_check = ""
        self.__bik = ""
        self.__type_of_company = ""
        self.__first_start = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value.strip(), str):
            error_proxy.set_error(Exception("Некорректное наименование!"))

        self.__name = value.strip()

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 12:
            error_proxy.set_error(Exception("Некорректный ИНН!"))

        self.__inn = value.strip()

    @property
    def account(self):
        return self.__check

    @account.setter
    def account(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 11:
            error_proxy.set_error(Exception("Некорректный счет!"))

        self.__check = value.strip()

    @property
    def correspondent_account(self):
        return self.__corr_check

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 11:
            error_proxy.set_error(Exception("Некорректный корреспондентский счет!"))

        self.__corr_check = value.strip()

    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 9:
            error_proxy.set_error(Exception("Некорректный БИК!"))

        self.__bik = value.strip()

    @property
    def ownership_type(self):
        return self.__type_of_company

    @ownership_type.setter
    def ownership_type(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 5:
            error_proxy.set_error(Exception("Некорректный вид собственности!"))

        self.__type_of_company = value.strip()

    @property
    def is_first_start(self):
        """
           Флаг Первый старт
        """
        return self._first_start

    @is_first_start.setter
    def is_first_start(self, value: bool):
        self._first_start = value