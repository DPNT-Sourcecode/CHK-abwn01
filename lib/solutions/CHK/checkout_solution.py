from collections import Counter

prices = {
    "A": 50, "B": 30, "C": 20, "D": 15, "E": 40,
    "F": 10, "G": 20, "H": 10, "I": 35, "J": 60,
    "K": 70, "L": 90, "M": 15, "N": 40, "O": 10,
    "P": 50, "Q": 30, "R": 50, "S": 20, "T": 20,
    "U": 40, "V": 50, "W": 20, "X": 17, "Y": 20,
    "Z": 21
}

multi_offers = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 120)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "V": [(3, 130), (2, 90)]
}

free_item_offers = {
    "E": (2, "B", 1),
    "F": (2, "F", 1),
    "N": (3, "M", 1),
    "R": (3, "Q", 1),
    "U": (3, "U", 1)
}

group_offers = {
    ("STXYZ", 3, 45)
}


def validated(x):
    if not isinstance(x, str):
        return False
    for _ in x:
        if _ not in prices:
            return False
    return True


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not validated(skus):
        return -1

    total = 0
    cart = Counter(skus)

    # apply free item offers
    for item, offer in free_item_offers.items():
        if item in cart:
            required, free_item, quant = offer
            if item == free_item:
                required += quant
            count = cart[item]
            if count >= required:
                offer_count = count // required
                free_items_count = offer_count * quant
                if free_item in cart:
                    cart[free_item] = max(
                        0, cart[free_item] - free_items_count
                    )

    # apply group offers
    for items, required, price in group_offers:
        items_sorted = list(items)
        items_sorted.sort(key=lambda x: prices[x], reverse=True)
        valid_item_count = sum(cart.get(k, 0) for k in items_sorted)

        if valid_item_count >= required:
            offer_count = valid_item_count // required
            total += offer_count * price
            items_in_offer = offer_count * required

            while items_in_offer > 0:
                for item in items_sorted:
                    if cart.get(item, 0) > 0:
                        cart[item] -= 1
                        items_in_offer -= 1
                        break

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








