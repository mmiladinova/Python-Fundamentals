class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = list()

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage


# storage_capacity = int(input())
# products_list = input().split(', ')
# storage_obj = Storage(storage_capacity)
#
# for products in products_list:
#     a = len(storage_obj.storage)
#     if a < storage_capacity:
#         storage_obj.add_product(products)
#     else:
#         break
#
# print(storage_obj.get_products())
storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
