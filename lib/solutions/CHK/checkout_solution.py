from collections import Counter

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

offers = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)]
}

free_item_offers = {
    "E": (2, "B", 1)
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1
    for x in skus:
        if x not in prices:
            return -1

    total = 0
    cart = Counter(skus)

    # apply discounts
    for item, count in cart.items():
        if item in offers:
            required, price = offers[item]
            if count >= required:
                offer_count = count // required
                total += offer_count * price
                count -= offer_count * required
        total += count * prices[item]

    return total

