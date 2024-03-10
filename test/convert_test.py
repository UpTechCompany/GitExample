from unittest.mock import MagicMock
import datetime
from src.reference import reference
from logic.convert_factory import ConverterFactory
from logic.data_presentation import convert
from storage.storage import storage
from models.unit import unit_model
from models.nomenclature import nomenclature_model
from src.settings_manager import settings_manager
from logic.formats.data_csv import csv_convert
import unittest
from logic.formats.data_json import json_convert
class TestSettings(unittest.TestCase):

    """Проверить статический метод build класса convert"""
    def test_convert_build(self):
        #Подготовка
        data = {}
        data[storage.unit_key()] = [unit_model.create_unit_gramm()]

        #Действие
        result = convert.build(storage.unit_key(), data)

        assert result is not None
        assert len(result) > 0

    def test_check_csv_create(self):
        # Подготовка
        data = {}
        data[storage.unit_key()] = [unit_model.create_unit_gramm()]
        menager = settings_manager()
        # Действие
        csv = csv_convert(menager.settings, data)

        result = csv.create(storage.unit_key())
        print(result)

        assert result is not None
        assert len(result) > 0

    """Проверить статический метод build класса convert"""
    def test_convert_build_for_nomenclature(self):
        #Подготовка
        data = {}
        data[storage.nomenclature_key()] = [nomenclature_model]

        #Действие
        result = convert.build(storage.nomenclature_key(), data)

        assert result is not None
        assert len(result) > 0

    def test_check_csv_create_for_nomenclature(self):
        # Подготовка
        data = {}
        data[storage.nomenclature_key()] = [nomenclature_model]
        menager = settings_manager()
        # Действие
        csv = csv_convert(menager.settings, data)

        result = csv.create(storage.nomenclature_key())
        print(result)
        """Будут установлены значения по дефолту, поскольку данная модель не заполнена"""

        assert result is not None
        assert len(result) > 0


    def test_check_reporting_json_build(self):
        # Подготовка
        data = {}
        data[storage.unit_key()] = [unit_model.create_unit_gramm()]

        # Действие
        result = json_convert.build(storage.unit_key())

        assert result is not None
        assert len(result) > 0

    def test_converter_factory(self):
        converter_factory = ConverterFactory()

        # Проверяем преобразование числа
        result_numeric = converter_factory.convert(123)
        self.assertEqual(result_numeric, {'numeric': 123})

        # Проверяем преобразование строки
        result_string = converter_factory.convert("Hello")
        self.assertEqual(result_string, {'str': 'Hello'})

        # Проверяем преобразование объекта datetime
        now = datetime.datetime.now()
        result_datetime = converter_factory.convert(now)
        expected_datetime = {'datetime': now.strftime('%Y-%m-%d %H:%M:%S')}
        self.assertEqual(result_datetime, expected_datetime)

        # Проверяем преобразование объекта reference
        ref = reference("Test")
        ref.description = "Test reference"
        result_reference = converter_factory.convert(ref)
        expected_reference = {
            'id': ref.id,
            'name': ref.name,
            'description': ref.description,
            'is_error': ref.is_error
        }
        self.assertEqual(result_reference, expected_reference)

    def test_generate_report(self):
        # Создаем макет ConverterFactory
        mock_converter_factory = MagicMock(spec=ConverterFactory)

        # Устанавливаем, что возвращается при вызове метода convert
        mock_converter_factory.convert.return_value = {'key': 'value'}

        # Создаем экземпляр json_convert с макетом ConverterFactory и фиктивным _data
        _data = {}  # Замените на реальные данные, если необходимо
        json_reporting = json_convert(mock_converter_factory, _data)

        # Генерируем отчет
        report = json_reporting.create(storage.unit_key(), _data)

        # Проверяем, что метод convert был вызван с ожидаемым аргументом
        mock_converter_factory.convert.assert_called_once_with(None)

        # Проверяем, что результат преобразуется в JSON с использованием json.dumps
        self.assertEqual(report, '{"key": "value"}')

