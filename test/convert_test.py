from logic.data_presentation import convert
from storage.storage import storage
from models.unit import unit_model
from models.nomenclature import nomenclature_model
from src.settings_manager import settings_manager
from logic.formats.data_csv import csv_convert
import unittest

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
