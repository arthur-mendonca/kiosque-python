from menu import products

# TAREFA 1 ----------------------


def get_product_by_id1(product_id):
    select_product = {}
    for product in products:
        if product["_id"] == product_id:
            select_product = product
    return select_product


def get_products_by_type1(product_type):
    product_result = []
    for product in products:
        if product["type"] == product_type:
            product_result.append(product)
    return product_result


# def add_product(new_product):
#     biggest_id = findBiggestId(products)
#     new_product["_id"] = biggest_id + 1
#     products.append(new_product)
#     return products

# TAREFA 2 -----------------------

def findBiggestId(menu):
    maior_id = 0
    for product in menu:
        if product["_id"] > maior_id:
            maior_id = product["_id"]
    return maior_id


def add_product(menu, **new_product):
    product_id = findBiggestId(menu)
    new_product["_id"] = product_id + 1
    menu.append(new_product)
    return new_product


# TAREFA 3 ----------------------

def get_product_by_id(product_id):
    if type(product_id) != int:
        raise TypeError("product id must be an int")
    return get_product_by_id1(product_id)


def get_products_by_type(product_type):
    if type(product_type) != str:
        raise TypeError("product type must be a str")
    return get_products_by_type1(product_type)


def menu_report():
    products_count = len(products)
    average_price = sum([product["price"]
                        for product in products]) / products_count
    rounded_result = round(average_price, 2)
    types = [product["type"]for product in products]
    most_common_type = max(types, key=types.count)
    return f"Products Count: {products_count} - Average Price: ${rounded_result} - Most Common Type: {most_common_type}"


# def get_product_by_id(product_id):
#     if type(product_id) != int:
#         raise TypeError("product id must be an int")
#     for product in products:
#         if product["_id"] == product_id:
#             return product
#         return {}


# def get_products_by_type_refactor(product_type):
#     product_result = []
#     if type(product_type) != str:
#         raise TypeError("product type must be a str")
#     for product in products:
#         if product["type"] == type:
#             product_result.append(product)
#     return product_result
