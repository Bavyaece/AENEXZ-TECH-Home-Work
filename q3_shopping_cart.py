# ---------------------------------------------------------------
# PART A - Spot the Bug
# ---------------------------------------------------------------
# def add_item(item, cart=[]):
#     cart.append(item)
#     return cart
#
# Predicted output:
# print(add_item("apple"))                  -> ["apple"]
# print(add_item("banana"))                  -> ["apple", "banana"]
# print(add_item("milk", cart=["bread"]))     -> ["bread", "milk"]
# print(add_item("eggs"))                     -> ["apple", "banana", "eggs"]
#
# WHY: Default arguments in Python are evaluated ONLY ONCE, when the
# function is defined - not every time it is called. So cart=[] creates
# a single list object that is reused (and mutated) across every call
# that doesn't explicitly pass its own cart. That's why "apple" and
# "banana" both end up in the SAME list, while the call with
# cart=["bread"] uses a separate, freshly passed list.


# ---------------------------------------------------------------
# PART B - Fix It
# ---------------------------------------------------------------
def add_item(item, cart=None):
    if cart is None:
        cart = []          # fresh empty list every call
    cart.append(item)
    return cart


# ---------------------------------------------------------------
# PART C - Build the Cart
# ---------------------------------------------------------------
def create_cart(owner, discount=0):
    # discount=0 is an int (immutable) -> safe as a default argument
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"Cannot modify tuple: {e}")
    # WHY: Tuples are immutable - once created, their internal items
    # cannot be reassigned. Python tuples don't implement item
    # assignment (__setitem__), so attempting price_tuple[0] = ...
    # raises a TypeError. This immutability is what makes tuples safe
    # to use as fixed records (like book details in Q2).


def calculate_total(cart):
    subtotal = 0
    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]
    discount_amount = subtotal * (cart["discount"] / 100)
    total = subtotal - discount_amount
    return round(total, 2)


def main():
    # ---- Demonstrate Part B fix ----
    print(add_item("apple"))                 # ["apple"]
    print(add_item("banana"))                # ["banana"]  <- independent now
    print(add_item("milk", cart=["bread"]))   # ["bread", "milk"]
    print(add_item("eggs"))                   # ["eggs"]    <- still independent

    print("-" * 40)

    # ---- Two independent customer carts ----
    cart1 = create_cart("Aarav", discount=10)
    cart2 = create_cart("Diya", discount=5)

    add_to_cart(cart1, "Notebook", 50, qty=3)
    add_to_cart(cart1, "Pen", 10, qty=5)

    add_to_cart(cart2, "Bag", 800, qty=1)

    print(f"{cart1['owner']}'s cart:", cart1["items"])
    print(f"{cart2['owner']}'s cart:", cart2["items"])

    print(f"{cart1['owner']}'s total: {calculate_total(cart1)}")
    print(f"{cart2['owner']}'s total: {calculate_total(cart2)}")

    # Proof carts are independent - cart2 unaffected by cart1's items
    assert cart1["items"] is not cart2["items"]
    print("Carts are independent: confirmed")

    print("-" * 40)

    # ---- Tuple immutability demo ----
    price_tuple = (100,)
    update_price(price_tuple, 150)


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------
# DISCUSSION POINTS
# ---------------------------------------------------------------
# 1. Why is discount=0 safe but cart=[] dangerous?
#    discount=0 is an int, which is immutable. Even if reassigned
#    inside the function, it just rebinds the local name - the
#    default object itself is never changed. cart=[] is a mutable
#    list; the SAME list object is shared across all calls, so any
#    .append() mutation persists and leaks into future calls.
#
# 2. Difference between rebinding and mutating?
#    Rebinding means pointing a variable name to a new object
#    (e.g., x = x + 1 for ints, or cart = [] inside a function).
#    The original object is left untouched. Mutating means changing
#    an object's contents in place (e.g., cart.append(item),
#    my_list[0] = 5) without creating a new object - other references
#    to that same object see the change too.
#
# 3. Which of these are mutable? list, tuple, dict, set, str, int
#    Mutable:   list, dict, set
#    Immutable: tuple, str, int
#
# 4. When you pass a list into a function and modify it, do changes
#    reflect outside? Why?
#    Yes. Python passes object references, not copies. A list
#    parameter inside the function refers to the exact same list
#    object as the caller's variable. So methods like .append(),
#    .remove(), or item assignment change the one shared object,
#    and the caller sees the update too. (Reassigning the parameter
#    to a brand-new list, however, would NOT affect the caller.)
