from logic.data_presentation import convert
from datetime import datetime
from src.errors import error_proxy, exception_proxy
from src.reference import reference

class BasicConverter(convert):
    def convert(self, obj):
        """
        Реализация метода convert для простых типов данных.

        Args:
            obj: Любой объект.

        Returns:
            Словарь в формате ключ - наименование поля, значение - данные поля.
        """
        if isinstance(obj, int) or isinstance(obj, float):
            return {'numeric': obj}
        elif isinstance(obj, str):
            return {'str': obj}
        else:
            raise ValueError("Unsupported data type for basic conversion")

class DateTimeConverter(convert):
    def convert(self, obj):
        """
        Реализация метода convert для типа данных DateTime.

        Args:
            obj: Любой объект.

        Returns:
            Словарь в формате ключ - наименование поля, значение - данные поля.
        """
        if isinstance(obj, datetime):
            return {'datetime': obj.strftime('%Y-%m-%d %H:%M:%S')}
        else:
            raise ValueError("Unsupported data type for datetime conversion")

class ReferenceConverter(convert):
    def convert(self, obj):
        """
        Реализация метода convert для типа данных Reference.

        Args:
            obj: Любой объект.

        Returns:
            Словарь в формате ключ - наименование поля, значение - данные поля.
        """
        if isinstance(obj, reference):
            return {
                'id': obj.id,
                'name': obj.name,
                'description': obj.description,
                'is_error': obj.is_error
            }
        else:
            raise ValueError("Unsupported data type for reference conversion")
