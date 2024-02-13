

class settings:
    __INN = ""
    __check = ""
    __korr_check = ""
    __BIK = ""
    __name_of_product = ""
    __name_of_company = ""

    # Свойство для получения имен полей класса
    @property
    def get_data_keys(self):
        return ['INN', 'check', 'korr_check', 'BIK', 'name_of_product', 'name_of_company']

    #Свойство для получения поля BIK
    @property
    def BIK(self):
        return self.__BIK

    # Свойство для получения поля check
    @property
    def check(self):
        return self.__check

    # Свойство для получения поля korr_check
    @property
    def korr_check(self):
        return self.__korr_check

    # Свойство для получения поля INN
    @property
    def INN(self):
        return self.__INN

    # Свойство для получения поля name_of_product
    @property
    def name_of_product(self):
        return self.__name_of_product

    # Свойство для получения поля name_of_company
    @property
    def name_of_company(self):
        return self.__name_of_company

    # Сеттер для изменения значения поля BIK
    @BIK.setter
    def BIK(self, value: str):
        if not isinstance(value, str) and len(value) == 9 and value.isnumeric():
            raise Exception("Некорректный аргумент!")

        self.__BIK = value.strip()

    # Сеттер для изменения значения поля check
    @check.setter
    def check(self, value: str):
        if not isinstance(value, str) and len(value) == 11 and value.isnumeric():
            raise Exception("Некорректный аргумент!")

        self.__check = value.strip()

    # Сеттер для изменения значения поля corr_check
    @korr_check.setter
    def korr_check(self, value: str):
        if not isinstance(value, str) and len(value) == 11 and value.isnumeric():
            raise Exception("Некорректный аргумент!")

        self.__korr_check = value.strip()

    # Сеттер для изменения значения поля INN
    @INN.setter
    def INN(self, value: str):
        if not isinstance(value, str) and len(value) == 12 and value.isnumeric():
            raise Exception("Некорректный аргумент!")

        self.__INN = value.strip()

    # Сеттер для изменения значения поля name_of_product
    @name_of_product.setter
    def name_of_product(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")

        self.__name_of_product = value.strip()

    # Сеттер для изменения значения поля name_of_company
    @name_of_company.setter
    def name_of_company(self, value: str):
        if not isinstance(value, str) and len(value) == 5:
            raise Exception("Некорректный аргумент!")

        self.__name_of_company = value.strip()
        
        