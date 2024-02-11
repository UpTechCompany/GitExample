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
        man = settings_maneger()
        file_name = "settings.json"
        man.opener(file_name)
        man.convert()
        print(man.data)

