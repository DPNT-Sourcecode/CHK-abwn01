from collections import Counter

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

multi_offers = {
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

    # apply free item offers
    for item, offer in free_item_offers.items():
        if item in cart:
            required, free_item, quant = free_item_offers[item]
            count = cart[item]
            if count >= required:
                offer_count = count // required
                free_items_count = offer_count * quant
                if free_item in cart:
                    cart[free_item] = max(
                        0, cart[free_item] - free_items_count
                    )

    # apply multi offers
    for item, count in cart.items():
        if item in multi_offers:
            for required, price in multi_offers[item]:
                if count >= required:
                    offer_count = count // required
                    total += offer_count * price
                    count -= offer_count * required
        total += count * prices[item]

    return total





