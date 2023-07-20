from menu import products


def calculate_tab(table):
    subtotal = 0
    for item in table:
        for product in products:
            if product["_id"] == item["_id"]:
                subtotal += (product["price"]*item["amount"])
    return {"subtotal":  f"${round(subtotal,2)}"}
