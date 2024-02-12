from settings import settings
from settings_maneger import settings_maneger
import unittest


class test_settings(unittest.TestCase):

    def test_check_create_manager(self):
        manager1 = settings_maneger()
        manager2 = settings_maneger()

        print(str(manager1.unique_number))
        print(str(manager2.unique_number))

        assert manager1.unique_number == manager2.unique_number

    def test_check_json(self):
        # Создание экземпляра класса
        man = settings_maneger()

        # Неправильный путь к файлу и проба на считывание
        file_name = "lo/other_dir/settings.json"
        man.opener(file_name)
        print(man.data)

        # Путь к файлу и проба на считывание
        file_name = "settings.json"
        man.opener(file_name)
        print(man.data)

