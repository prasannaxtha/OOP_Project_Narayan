from product import Product


class ShoppingCart:
    def __init__(self):
        self.__products = []
        self.__cart = []

    def add_product(self, pid, name, price):
        self.__products.append(Product(pid, name, price))
        print("Product added successfully!")

    def view_products(self):
        if not self.__products:
            print("No products available.")
            return

        print("\n===== PRODUCTS =====")

        for product in self.__products:
            product.display()

    def add_to_cart(self, pid, qty):
        for product in self.__products:
            if product.get_id() == pid:
                self.__cart.append((product, int(qty)))
                print("Added to cart!")
                return

        print("Product not found!")

    def view_cart(self):
        if not self.__cart:
            print("Cart is empty.")
            return

        subtotal = 0

        print("\n===== SHOPPING CART =====")

        for product, qty in self.__cart:
            total = product.get_price() * qty
            subtotal += total
            print(f"{product.get_name()} x{qty} = Rs. {total}")

        discount = subtotal * 0.10 if subtotal >= 5000 else 0
        vat = (subtotal - discount) * 0.13
        grand_total = subtotal - discount + vat

        print("---------------------------")
        print(f"Subtotal : Rs. {subtotal}")
        print(f"Discount : Rs. {discount}")
        print(f"VAT      : Rs. {vat}")
        print(f"Total    : Rs. {grand_total}")

    def checkout(self):
        if not self.__cart:
            print("Cart is empty.")
            return

        self.view_cart()
        print("\nCheckout Successful!")
        self.__cart.clear()