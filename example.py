from classes.order import Order
from classes.product import Product
from classes.customer import Customer
from classes.discount import Discount

#Создаем продукты
product1 = Product("Smartphone", 15000)
product2 = Product("Headphones", 2000)
print('Продукты:')
print(product1)
print(product2)

#Создаем клиентов

customer1 = Customer("Ivan")
customer2 = Customer("Katya")
print('Клиенты:')
print(customer1)
print(customer2)

#Создаем заказы для каждого клиента
print("Создаем заказы")
order1 = Order([product1])
customer1.orders.append(order1)
print(order1)


order2 = Order([product1, product2])
customer2.orders.append(order2)
print(order2)



#Создаем разные виды скидок

discount_leto = Discount("лето", 10)
discount_promokod = Discount("промокод", 15)
print('Скидки:')
print(discount_leto)
print(discount_promokod)

#Рассчитываем цену с учетом скидки

discounted_price_product1 = Discount.calculate_discount_price(product1.price, discount_leto.discount_percent)
print(discounted_price_product1)

discounted_price_product2 = Discount.calculate_discount_price(product2.price, discount_promokod.discount_percent)
print(discounted_price_product2)

product1.price = discounted_price_product1
product2.price = discounted_price_product2

print("заказы с учетом примененных скидок")
print(order1)
print(order2)


print(f"всего заказов: {Order.total_orders()}")

orders = [order1, order2]
     
total_sum = sum(order.total_price() for order in orders)
print(f"Общая сумма всех заказов - {total_sum}")    

def print_customer_products(customer):
    print(f"Продукты для клиента {customer.name}:")
    for order in customer.orders:
        for product in order.products:
            print(f"- {product.name}")


print('Информация о клиентах:')
print('Клиент1:')
print(customer1)
print_customer_products(customer1)


print('Клиент2:')
print(customer2)
print_customer_products(customer2)



