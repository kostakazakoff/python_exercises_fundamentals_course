def valid_price(part_price: float):
    if part_price < 0:
        return False
    return True


def valid_order(order_total_price: float):
    if order_total_price <= 0:
        return False
    return True


def order_with_tax(total_order_price: float):
    return total_order_price, total_price * 0.2, total_order_price * 1.2


def customer_discount(order: float, customer_status: str):
    if customer_status == 'special':
        return order * 0.9
    return order


command = input()
total_price = 0

while command != 'special' and command != 'regular':
    price = float(command)
    if not valid_price(price):
        print('Invalid price!')
        command = input()
        continue
    total_price += price
    command = input()

if not valid_order(total_price):
    print('Invalid order!')
else:
    total_price, tax, total_price_with_tax = order_with_tax(total_price)
    final_order = customer_discount(total_price_with_tax, command)
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {final_order:.2f}$")
