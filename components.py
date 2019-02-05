# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.products = []
    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for prd in products:
            print("Product Name: %s" %s(prd.name))
            print("Description: %s" %s(prd.description))
            print()


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!
        return "\tProduct name: %s\n\tdescription: %s\n\tprice: %s"\
        %(self.name, self.description, self.price)


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0

        for prd in self.products:
            total += prd.price 

        return total
    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print("your receipt: ")
        for prd in self.products:
            print("""
                Product name: {}
                Description: {}
                price: {:f} SAR

            Total price: {:f}
                """.format(prd.name, prd.description, prd.price, self.get_total_price()))
            

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        self.print_receipt()
        conf = input("Confirmed? (yes/no) ").lower()

        if conf == "yes":
            return "Your order has been placed."
        else:
            return "Your order has been cancelled."

