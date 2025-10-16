-- Active: 1756495168690@@127.0.0.1@3306@multi_vendor_ecommerce

create DATABASE multi_vendor_ecommerce

USE multi_vendor_ecommerce

show DATABASES

-- Tables

CREATE TABLE SubscriptionPlan (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) not NULL,
    duration INT NOT NULL,
    features TEXT
)

-- DROP TABLE SubscriptionPlan

-- Part B : 4
CREATE Table Vendor (
    vendor_id INT AUTO_INCREMENT PRIMARY KEY,
    business_name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address VARCHAR(255),
    subscription_id INT,
    FOREIGN KEY (subscription_id) REFERENCES SubscriptionPlan (plan_id)
)

-- DROP TABLE Vendor

CREATE Table Product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    status ENUM('active', 'inactive') DEFAULT 'active',
    vendor_id INT,
    FOREIGN KEY (vendor_id) REFERENCES Vendor (vendor_id)
)

-- DROP TABLE Product

CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
)

-- DROP TABLE Category

-- Part B : 5
CREATE Table ProductCategory (
    product_id INT,
    category_id INT,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES Product (product_id),
    FOREIGN KEY (category_id) REFERENCES Category (category_id)
)

-- DROP TABLE ProductCategory

CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address VARCHAR(255)
)

-- DROP TABLE Customer

CREATE TABLE Orders (
    order_id int AUTO_INCREMENT PRIMARY key,
    customer_id int,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2),
    status VARCHAR(100),
    FOREIGN key (customer_id) REFERENCES Customer (customer_id)
)

-- DROP TABLE Orders

CREATE TABLE OrderItem (
    orderItem_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders (order_id),
    FOREIGN KEY (product_id) REFERENCES Product (product_id)
);

-- DROP TABLE OrderItem

CREATE TABLE Payment (
    payment_id int AUTO_INCREMENT PRIMARY KEY,
    order_id INT UNIQUE,
    method VARCHAR(100),
    amount DECIMAL(10, 2),
    payment_date DATE,
    status VARCHAR(50),
    FOREIGN key (order_id) REFERENCES Orders (order_id)
)

-- DROP TABLE Payment

-- show TABLES

SHOW TABLEs

-- 7: insert product
INSERT INTO
    SubscriptionPlan (
        plan_name,
        price,
        duration,
        features
    )
VALUES (
        'Basic_Plan',
        1000,
        30,
        'Basic features'
    );

-- SELECT * from SubscriptionPlan

INSERT INTO Category (name) VALUES ('Electronics');

INSERT INTO
    Vendor (
        business_name,
        contact_person,
        email,
        phone,
        address,
        subscription_id
    )
VALUES (
        'SmartTech Ltd',
        'Rahim Khan',
        'rahim@smarttech.com',
        '017XXXXXXXX',
        'Dhaka, Bangladesh',
        (
            SELECT plan_id
            FROM SubscriptionPlan
            WHERE
                plan_name = 'Basic_Plan'
        )
    );

-- SELECT * FROM Vendor

INSERT INTO
    Product (
        vendor_id,
        name,
        price,
        stock_quantity,
        status
    )
VALUES (
        (
            SELECT vendor_id
            FROM Vendor
            WHERE
                business_name = 'SmartTech Ltd'
        ),
        'Laptop',
        75000,
        10,
        'active'
    );

-- SELECT * FROM Product

INSERT INTO
    ProductCategory (product_id, category_id)
VALUES (
        (
            SELECT product_id
            FROM Product
            WHERE
                name = 'Laptop'
        ),
        (
            SELECT category_id
            FROM Category
            WHERE
                name = 'Electronics'
        )
    );

UPDATE Product SET stock_quantity = 15 WHERE name = 'Laptop';

DELETE FROM Customer WHERE email = 'oldcustomer@gmail.com';

-- 15

SELECT Vendor.business_name, SUM(OrderItem.subtotal) AS total_sales
FROM
    Vendor
    JOIN Product ON Vendor.vendor_id = Product.vendor_id
    JOIN OrderItem ON Product.product_id = OrderItem.product_id
GROUP BY
    Vendor.vendor_id,
    Vendor.business_name;

-- 16

SELECT Customer.name, Customer.email
FROM Customer
    LEFT JOIN Orders ON Customer.customer_id = Orders.customer_id
WHERE
    Orders.order_id IS NULL;

-- 17
SELECT COUNT(*) AS Total_Active_Products
FROM Product
WHERE
    status = 'active';

-- 18

SELECT Vendor.business_name, Vendor.contact_person, Vendor.email
FROM Vendor
    JOIN SubscriptionPlan ON Vendor.subscription_id = SubscriptionPlan.plan_id
WHERE
    SubscriptionPlan.plan_name = 'Enterprise';

-- 19

SELECT Customer.name, AVG(Orders.total_amount) AS Avg_Order_Amount
FROM Customer
    JOIN Orders ON Customer.customer_id = Orders.customer_id
GROUP BY
    Customer.customer_id,
    Customer.name;

-- 20

SELECT Customer.name, COUNT(DISTINCT Product.vendor_id) AS Vendor_Count
FROM
    Customer
    JOIN Orders ON Customer.customer_id = Orders.customer_id
    JOIN OrderItem ON Orders.order_id = OrderItem.order_id
    JOIN Product ON OrderItem.product_id = Product.product_id
GROUP BY
    Customer.customer_id,
    Customer.name
HAVING
    Vendor_Count > 1;