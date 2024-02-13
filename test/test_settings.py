import unittest
from src.settings import settings
from src.settings_manager import settings_manager

class TestSettings(unittest.TestCase):

    def test_check_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()

        self.assertEqual(manager1.unique_number, manager2.unique_number)

    def test_check_json_invalid_path(self):
        # Создание экземпляра класса
        man = settings_manager()

        # Неправильный путь к файлу и проба на считывание
        file_name = "lo/other_dir/settings.json"
        self.assertTrue(man.opener(file_name))
        self.assertEqual(man.data, {})

    def test_check_json_valid_path(self):
        # Создание экземпляра класса
        man = settings_manager()

        # Путь к файлу и проба на считывание
        file_name = "../res/settings.json"
        self.assertFalse(man.opener(file_name))
        self.assertNotEqual(man.data, {})

    def test_settings_properties_initial_values(self):
        # Создание экземпляра класса settings
        settings_obj = settings()

        # Проверка начальных значений полей
        self.assertEqual(settings_obj.BIK, "")
        self.assertEqual(settings_obj.check, "")
        self.assertEqual(settings_obj.korr_check, "")
        self.assertEqual(settings_obj.INN, "")
        self.assertEqual(settings_obj.name_of_product, "")
        self.assertEqual(settings_obj.name_of_company, "")

    def test_settings_properties_set_values(self):
        # Создание экземпляра класса settings
        settings_obj = settings()

        # Проверка сеттеров и геттеров
        settings_obj.BIK = "123456789"
        settings_obj.check = "12345678901"
        settings_obj.korr_check = "12345678901"
        settings_obj.INN = "123456789012"
        settings_obj.name_of_product = "Product A"
        settings_obj.name_of_company = "ABC Corp"

        self.assertEqual(settings_obj.BIK, "123456789")
        self.assertEqual(settings_obj.check, "12345678901")
        self.assertEqual(settings_obj.korr_check, "12345678901")
        self.assertEqual(settings_obj.INN, "123456789012")
        self.assertEqual(settings_obj.name_of_product, "Product A")
        self.assertEqual(settings_obj.name_of_company, "ABC Corp")

    def test_settings_exceptions_invalid_values(self):
        # Создание экземпляра класса settings
        settings_obj = settings()

        # Проверка исключений при некорректных данных
        with self.assertRaises(Exception):
            settings_obj.BIK = "12345678"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.check = "123456"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.korr_check = "123456"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.INN = "12345678901"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.name_of_company = "ABC"  # Некорректная длина

    def test_settings_manager_exceptions_nonexistent_file(self):
        # Попытка открыть несуществующий файл
        man = settings_manager()
        with self.assertRaises(Exception):
            man.opener("nonexistent_file.json")

    def test_settings_manager_exceptions_invalid_settings_file(self):
        # Попытка открыть файл с некорректным форматом данных
        man = settings_manager()
        with self.assertRaises(Exception):
            man.opener("invalid_settings.json")

    def test_unique_number_type(self):
        # Проверка типа уникального номера менеджера настроек
        manager = settings_manager()
        self.assertIsInstance(manager.unique_number, str)

    def test_settings_manager_opener_type(self):
        # Проверка типа возвращаемого значения метода opener
        man = settings_manager()
        self.assertIsInstance(man.opener("settings.json"), bool)

    def test_settings_manager_singleton(self):
        # Проверка, что менеджер настроек является синглтоном
        manager1 = settings_manager()
        manager2 = settings_manager()
        self.assertIs(manager1, manager2)

    def test_settings_opener_invalid_argument(self):
        # Проверка выброса исключения при передаче некорректного аргумента в метод opener
        man = settings_manager()
        with self.assertRaises(Exception):
            man.opener(123)

if __name__ == "__main__":
    unittest.main()
