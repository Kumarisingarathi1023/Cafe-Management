menu = {
    'pizza': 200,
    'burger': 150,
    'pasta': 250,
    'coffee': 100,
    'tea': 50
}

print("Welcome to our cafe")

print("Menu\npizza: 200\nburger: 150\npasta: 250\ncoffee: 100\ntea: 50")

order_total = 0

while True:

    order_item = input("Enter your item: ").lower()

    if order_item in menu:
        order_total += menu[order_item]

        order = input("Do you want anything else? (yes/no): ").lower()

        if order == "yes":
            continue

        else:
            break

    else:
        print("You entered a wrong item")

print(f"Your order value is: {order_total}")