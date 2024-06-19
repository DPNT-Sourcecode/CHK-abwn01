from collections import Counter
from db import prices, multi_offers, free_item_offers, group_offers


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







