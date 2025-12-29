import json


class Purchase:
    def __init__(self, path: str):
        self.path = path
        self.__data = []

        self.read_data()

    def read_data(self) -> bool:
        try:
            with open(self.path) as file:
                self.__data = json.load(file)
            return True
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return False

    def __get_items(self, key1: str, key2: str) -> dict:
        items = dict()
        for row in self.__data:
            if row[key1] not in items:
                items[row[key1]] = [row[key2]]
            else:
                items[row[key1]].append(row[key2])
        return items

    def total_revenue(self) -> float:
        total_rev = 0
        for row in self.__data:
            total_rev += row["price"] * row["quantity"]
        return total_rev

    def items_by_category(self) -> dict:
        return self.__get_items("category", "item")

    def expensive_purchases(self, min_price: float = 1.0) -> str:
        items = []
        for row in self.__data:
            if row["price"] > min_price:
                items.append(row)
        return f"Покупки дороже {min_price}: {items}"

    def average_price_by_category(self) -> dict:
        avg_price = dict()
        for key, val in self.__get_items("category", "price").items():
            avg_price[key] = sum(val) / len(val)
        return avg_price

    def most_frequent_category(self) -> str:
        category = ""
        mx = 0
        for row in self.__data:
            if mx < row["quantity"]:
                category = row["category"]
                mx = row["quantity"]
        return category

    def print_info(self):
        print(f"Общая выручка: {self.total_revenue()}")
        print(f"Товары по категориям: {self.items_by_category()}")
        print(self.expensive_purchases())
        print(f"Средняя цена по категориям: {self.average_price_by_category()}")
        print(
            f"Категория с наибольшим количеством проданных товаров: {self.most_frequent_category()}"
        )
