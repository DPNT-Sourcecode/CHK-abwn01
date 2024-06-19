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

