
salads = [
    {"id": 1, "name": "Caesar", "price": 8.99},
    {"id": 2, "name": "Chicken Caesar", "price": 11.99},
    {"id": 3, "name": "Waldorf", "price": 10.99},
    {"id": 4, "name": "Cobb", "price": 9.99},
    {"id": 5, "name": "Caprese", "price": 9.99},
    {"id": 6, "name": "Nicoise", "price": 10.99},
]

if __name__ == "__main__":

    print("------------------")
    print("PROCESSING KITCHEN DATA...")
    print("------------------")
    print(salads)
    # breakpoint()

    #
    # QUESTION A
    #
    # Assuming the identifier, or "id" attribute, of each salad is and will always be unique,
    # ... and assuming the order of salads may vary,
    # ... "print" the name of the salad whose identifier is equal to 3 (i.e. "Waldorf"):

    print([n["name"] for n in salads if n["id"]==3][0])



    #
    # QUESTION B
    #
    # Assuming the "price" attribute represents a salad’s cost to the consumer,
    # ... "print" the number of salads which are more expensive than ten dollars (i.e. 3):

    # sticker = []
    # for p in salads:
    #     sticker.append(p["price"])

    # expensive = [e for e in sticker if e>10.0]
    # expensive_salads = len(expensive)
    # print(expensive_salads)

    print(len([s["price"] for s in salads if s["price"]>10.0]))

