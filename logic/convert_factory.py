from datetime import datetime
from src.errors import error_proxy, exception_proxy
from src.reference import reference
from logic.basic_converter import BasicConverter, DateTimeConverter, ReferenceConverter

class ConverterFactory:
    def __init__(self):
        self.basic_converter = BasicConverter()
        self.datetime_converter = DateTimeConverter()
        self.reference_converter = ReferenceConverter()

    def convert(self, obj):
        """
        Метод для конвертации объекта в набор словарей.

        Args:
            obj: Любой объект.

        Returns:
            Набор словарей, сформированных в соответствии с исходной структурой объекта.
        """
        if isinstance(obj, (int, float, str)):
            return self.basic_converter.convert(obj)
        elif isinstance(obj, datetime):
            return self.datetime_converter.convert(obj)
        elif isinstance(obj, reference):
            return self.reference_converter.convert(obj)
        else:
            raise ValueError("Unsupported data type for conversion")