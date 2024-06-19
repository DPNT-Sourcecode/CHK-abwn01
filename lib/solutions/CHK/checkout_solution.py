from collections import Counter

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

offers = {
    "A": (3, 130),
    "B": (2, 45)
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1

    total = 0
    cart = Counter(skus)

    # apply discounts
    for item, count in cart.items():
        if item in offers:
            for required, price in offers[item]:
                if count >= required:
                    offer_count = count // required
                    total += offer_count * price
                    count -= offer_count * required
        total += count * prices[item]


