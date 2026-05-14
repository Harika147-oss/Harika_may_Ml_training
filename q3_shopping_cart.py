#Part A — Spot the Bug
def add_item(item, cart=[]):
    cart.append(item)
    return cart
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))
#Part B — Fix It
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
#Part C — Build the Cart   
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }
def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })
def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price 
    except TypeError:
        print("TypeError: Tuples are immutable")
def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]
    discount_amount = total * cart["discount"] / 100
    return total - discount_amount
cart1 = create_cart("Alice", 10)
add_to_cart(cart1, "Laptop", 50000)
add_to_cart(cart1, "Mouse", 1000, 2)
cart2 = create_cart("Bob", 5)
add_to_cart(cart2, "Phone", 20000)
add_to_cart(cart2, "Charger", 500, 2)
print("Cart 1:")
print(cart1)
print("\nCart 2:")
print(cart2)
print("\nCart1 Total =", calculate_total(cart1))
print("Cart2 Total =", calculate_total(cart2))
price_data = (1000, "Laptop")
update_price(price_data, 1200)

# Discussion Points
# 1. discount=0 is safe because integers are immutable.
#    cart=[] is dangerous because lists are mutable.
# 2. Rebinding means assigning a new object.
#    Mutating means changing an existing object.
# 3. Mutable: list, dict, set
#    Immutable: tuple, str, int
# 4. Yes, changes reflect outside because lists are mutable
#    and functions receive references to objects.n 3 code in this online editor and run it.
