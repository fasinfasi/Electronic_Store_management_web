# Electronic Web Store 🛒

Electronic Web Store is a simple online platform designed to facilitate the storage, purchase, and pricing of electronic products. Users can browse a variety of electronic items, view instant prices, and place orders. The application manages order details, including customer IDs, product items, quantities, individual prices, and total prices, ensuring a seamless shopping experience for electronics enthusiasts, hobbyists, and professionals.

## Technologies Used
  - Frontend: HTML, CSS, JavaScript, Bootstrap(for the user interface)
  - Backend: Flask (Python web framework)
  - Database: MySQL (for storing product and order data)

### Project Overview 👁

The Electronic Web Store enables users to easily browse and purchase electronic products. The system is built using Flask and MySQL, allowing for efficient management of product information and order details. Users can view available products, their prices, and place orders that store customer details, product items, quantities, individual prices, and total prices in a MySQL database.

### Features ✨
 - Product Management: Store and display a variety of electronic products.
 - Instant Pricing: Get real-time prices for products available for purchase.
 - Order Processing: Store order details, including customer ID, product items, quantity, individual prices, and total price in MySQL.
 - User-Friendly Interface: Simplified navigation for browsing and purchasing products.

### Screenshots 📷

##### Dashboard
![image](https://github.com/fasinfasi/Electronic_Store_management_web/assets/141424321/663a7ff7-5e08-4fa7-9613-3d52e482dd40)

##### Adding products to cart
![image](https://github.com/fasinfasi/Electronic_Store_management_web/assets/141424321/b08d6007-5967-448a-8f46-4b82f50cfc34)

##### Added cart items
![image](https://github.com/fasinfasi/Electronic_Store_management_web/assets/141424321/94094d49-8f36-4674-a0df-fe876fd035b2)

##### Available products listed with it's ID and price
![image](https://github.com/fasinfasi/Electronic_Store_management_web/assets/141424321/8a24c167-67c7-428b-885d-62bbd41d0486)

##### Customers details registered into database table
![image](https://github.com/fasinfasi/Electronic_Store_management_web/assets/141424321/a995048c-4c18-4dce-9817-51796cb90aa5)

##### All ordered items are kept in MySQL database
![image](https://github.com/fasinfasi/Electronic_Store_management_web/assets/141424321/aa676b11-7af9-45f8-bddc-c4834c528c21)


## Installation
#### Prerequisites
 - Python (v3.6 or higher)
 - MySQL Server

**Steps**
1. Clone the Repository:
   ```
   https://github.com/fasinfasi/Electronic_Store_management_web.git
   cd electronic-web-store
   ```

2. Set Up a Virtual Environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install Dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set Up the Database:
   - Create a MySQL database and configure the connection settings in your Flask application.

5. Run the Application:
   ```
   flask run
   ```

6. Access the App:
   - Open your web browser and go to http://127.0.0.1:5000 (or the designated port).

## License
Distributed under the MIT License. See [LICENSE](license) for more information.

