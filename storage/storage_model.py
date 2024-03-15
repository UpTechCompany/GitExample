from src.reference import reference
class StorageModel(reference):
    def __init__(self, location):
        self.location = location
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"{item} добавлен на склад в помещение {self.location}.")
        else:
            print("Склад полон, невозможно добавить товар.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} удален со склада из помещения {self.location}.")
        else:
            print(f"{item} отсутствует на складе в помещении {self.location}.")

