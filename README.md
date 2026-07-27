# 🛒 E-Commerce Shopping Cart System

A simple console-based E-Commerce Shopping Cart System developed in Python using Object-Oriented Programming (OOP). This project allows users to manage products, add items to a shopping cart, calculate discounts and VAT, and complete checkout through a menu-driven interface. The program demonstrates the use of encapsulation, classes, objects, and modular programming. :contentReference[oaicite:0]{index=0}

---

## 📌 Features

- Add new products
- View available products
- Add products to the shopping cart
- View shopping cart with:
  - Subtotal
  - 10% Discount (for purchases above Rs. 5000)
  - 13% VAT
  - Grand Total
- Checkout and clear cart
- Menu-driven console interface :contentReference[oaicite:1]{index=1}

---

## 📂 Project Structure

```
E-Commerce-Cart/
│
├── main.py        # Main menu and program execution
├── cart.py        # ShoppingCart class and cart operations
├── product.py     # Product class
└── README.md
```

---

## 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## 💻 OOP Concepts Implemented

### Encapsulation
- Product attributes are private.
- Shopping cart and product list are stored as private attributes.

### Classes
- `Product`
- `ShoppingCart`

### Objects
Objects of the Product class are created whenever a new product is added to the system. :contentReference[oaicite:2]{index=2}

---

## ▶️ How to Run

1. Download or clone the project.
2. Open the project folder in VS Code or any Python IDE.
3. Run the following command:

```bash
python main.py
```

---

## 📋 Menu Options

```
1. Add Product
2. View Products
3. Add To Cart
4. View Cart
5. Checkout
6. Exit
```
:contentReference[oaicite:3]{index=3}

---

## 🧮 Billing Rules

- Discount: **10%** for purchases of **Rs. 5000 or more**
- VAT: **13%**
- Total = Subtotal − Discount + VAT :contentReference[oaicite:4]{index=4}

---

## 📖 Example

```
===== PRODUCTS =====
P001 | Laptop | Rs. 70000

===== SHOPPING CART =====
Laptop x1 = Rs. 70000

Subtotal : Rs. 70000
Discount : Rs. 7000
VAT      : Rs. 8190
Total    : Rs. 71190
```


## 🚀 Future Improvements

- Save products and orders using JSON/CSV
- Product search feature
- Remove items from cart
- Update product details
- User login and authentication
- Graphical User Interface (GUI)
- Database integration

---

## 👨‍💻 Author

**Prasanna Xtha**

Bachelor's in Cyber Security

Texas International College

---

## 📄 License

This project is developed for educational purposes only.
