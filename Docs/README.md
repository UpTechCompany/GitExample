# Кодовая база

В этом репозитории содержится несколько классов и модулей на Python, которые выполняют различные функции, связанные с управлением настройками и тестированием.

## settings.py

Этот модуль определяет класс `settings`, который представляет собой набор настроек для определенной системы или приложения. Каждый атрибут этого класса соответствует конкретной настройке:

- `INN`: ИНН (Идентификационный номер налогоплательщика) компании.
- `check`: счет.
- `korr_check`: корреспондентский счет.
- `BIK`: БИК (Банковский идентификационный код) банка.
- `name_of_product`: название продукта.
- `name_of_company`: наименование компании.

Каждый атрибут имеет методы получения (`getter`) и установки (`setter`) значений, которые также выполняют проверку корректности переданных значений. Например, для ИНН проверяется его длина (12 символов) и то, что он содержит только цифры.

## settings_maneger.py

Этот модуль определяет класс `settings_maneger`, который представляет менеджера настроек. Этот класс отвечает за загрузку настроек из файла JSON, их конвертацию в объекты класса `settings` и управление этими настройками.

Ключевые методы класса `settings_maneger`:

- `opener(file_name)`: открывает файл настроек из JSON-файла. Если файл не найден или возникает ошибка при его открытии, метод возвращает `False`.
- `convert()`: конвертирует данные из JSON в объекты класса `settings`. Перед этим методом нужно убедиться, что файл настроек успешно открыт методом `opener`.
- `data`: возвращает словарь с данными настроек после их конвертации.

## test_settings.py

Этот модуль содержит набор тестов для проверки функциональности классов `settings` и `settings_maneger`. В тестах проверяется создание экземпляров менеджера настроек, открытие файла настроек и корректность конвертации данных из JSON в объекты `settings`.

## settings.json

Этот файл содержит пример JSON-данных настроек, которые используются в тестах для проверки функциональности. Пример содержит значения для всех атрибутов класса `settings`, чтобы полностью протестировать функциональность.
