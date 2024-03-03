from logic.convert import convert

class csv_convert(convert):

    def create(self, typeKey: str):
        super().create(typeKey)

        result = ""

        items = list(self.data[typeKey])

        # Создаем заголовок CSV
        class_attributes = self.get_class_attributes(items[0]) if items else []
        result += ",".join(attr.split('_')[-1] for attr in class_attributes) + "\n"

        # Заполняем CSV данными
        for item in items:
            values = [str(getattr(item, attr)) for attr in class_attributes]
            result += ",".join(values) + "\n"

        return result

    def get_class_attributes(self, obj):
        """
        Получает список имен атрибутов класса
        """
        return [attr for attr in vars(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
