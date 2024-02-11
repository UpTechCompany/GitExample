

class settings:
    __INN = ""
    __check = ""
    __korr_check = ""
    __BIK = ""
    __name_of_product = ""
    __name_of_company = ""

    @property
    def get_data_keys(self):
        return ['INN', 'check', 'korr_check', 'BIK', 'name_of_product', 'name_of_company']

    @property
    def BIK(self):
        return self.__BIK

    @property
    def check(self):
        return self.__check

    @property
    def korr_check(self):
        return self.__korr_check

    @property
    def INN(self):
        return self.__INN

    @property
    def name_of_product(self):
        return self.__name_of_product

    @property
    def name_of_company(self):
        return self.__name_of_company


    @BIK.setter
    def BIK(self, value: str):
        if not isinstance(value, str) and len(value) == 9 and value.isnumeric():
            raise Exception("Некорректный аргумент!")

        self.__BIK = value.strip()

    @check.setter
    def check(self, value: str):
        if not isinstance(value, str) and len(value) == 11 and value.isnumeric():
            raise Exception("Некорректный аргумент!")

        self.__check = value.strip()

    @korr_check.setter
    def korr_check(self, value: str):
        if not isinstance(value, str) and len(value) == 11 and value.isnumeric():
            raise Exception("Некорректный аргумент!")

        self.__korr_check = value.strip()

    @INN.setter
    def INN(self, value: str):
        if not isinstance(value, str) and len(value) == 12 and value.isnumeric():
            raise Exception("Некорректный аргумент!")

        self.__INN = value.strip()

    @name_of_product.setter
    def name_of_product(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")

        self.__name_of_product = value.strip()

    @name_of_company.setter
    def name_of_company(self, value: str):
        if not isinstance(value, str) and len(value) == 5:
            raise Exception("Некорректный аргумент!")

        self.__name_of_company = value.strip()
        
        