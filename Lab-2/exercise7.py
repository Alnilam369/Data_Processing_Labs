products = [
    {"name": "Notebook",  "price": 120 , " quantity": 3},
    {"name": "Pen",  "price": 20, "quantity ": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse","price": 650, " quantity": 1}
]

total = 0

for product in products:
    cost = product["price"] * product["quantity"]
    total += cost

print("Total Cost:",  total)


def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    else:
        return total


final_price = apply_discount(total)

print("Final Price:", final_price)