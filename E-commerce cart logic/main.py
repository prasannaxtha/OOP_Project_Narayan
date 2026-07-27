from cart import ShoppingCart


def menu():
    cart = ShoppingCart()

    while True:
        print("\n" + "=" * 40)
        print("      E-COMMERCE CART")
        print("=" * 40)
        print("1. Add Product")
        print("2. View Products")
        print("3. Add To Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Product ID: ")
            name = input("Product Name: ")
            price = input("Price: ")

            cart.add_product(pid, name, price)

        elif choice == "2":
            cart.view_products()

        elif choice == "3":
            pid = input("Product ID: ")
            qty = input("Quantity: ")

            cart.add_to_cart(pid, qty)

        elif choice == "4":
            cart.view_cart()

        elif choice == "5":
            cart.checkout()

        elif choice == "6":
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()