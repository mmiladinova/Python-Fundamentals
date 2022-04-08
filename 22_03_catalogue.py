class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = list()

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        filtered_products = list()
        # result = [x for x in self.products if x.startswith(first_letter)]
        for product in self.products:
            if product[0] == first_letter:
                filtered_products.append(product)
        return filtered_products

    def __repr__(self):
        self.products = sorted(self.products)
        result = '\n'.join(self.products)
        return f"Items in the {self.name} catalogue:\n{result}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
catalogue.add_product("Aappp")
print(catalogue.get_by_letter("M"))
print(catalogue)
