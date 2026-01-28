class Discount:
    '''
    Класс Discount
    Этот класс представляет скидку в интернет-магазине.
    Метод __init__:
        Конструктор инициализирует объект Discount с двумя атрибутами: description (описание скидки) и discount_percent (процент скидки)
        Пример: discount1 = Discount("leto", 10) создаст скидку с названием "лето" и процентом скидки 10%.
    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(discount1) выведет Discount(description: "лето", discount_percent: 10).
    '''
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent
    
    @staticmethod
    def calculate_discount_price(price, discount_percent):
       return price - (price * discount_percent / 100)

    def __str__(self):
        return f"Описание скидки: {self.description}, процент скидки: {self.discount_percent}"