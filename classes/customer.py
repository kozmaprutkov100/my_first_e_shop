class Customer:
    '''
    Класс Customer
    Этим классом представлены клиенты в интернет магазине
    Метод __init__ :
    Конструктор инициализирует объект Product с двумя атрибутами: name (имя клиента) и orders (список заказов клиента).
    Пример: customer1 = Customer("Ivan", "smartfone", "laptop") создаст клиента с именем "Ivan" и списком заказов: "smartfone", "laptop" .
    Метод __str__:
    Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью команды print.
    Пример: print(сustomer1) выведет " Клиент Ivan, список заказов: smartphone, laptop).
    '''
    def __init__(self, name: str):
        self.name = name
        self._orders = []
        
    @property
    def orders(self):
        return self._orders
    
    @orders.setter
    def orders(self, orders):
        self._orders = orders
    
    def __str__(self):
         orders_list = ', '.join(str(order) for order in self.orders)
         return f"Клиент {self.name}, список заказов: {orders_list}"