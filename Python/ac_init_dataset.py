import os

os.system("pip3 install pymysql")

import pymysql as sql
from getpass import getpass

password = getpass("Enter mysql connect password: ")
connection = sql.connect(host="127.0.0.1", user="root", password=password, port=3306)
cursor = connection.cursor()


cursor.execute("CREATE SCHEMA AC;")
cursor.execute("USE AC;")
cursor.execute(
    """
    CREATE TABLE Book (
        bookid INT PRIMARY KEY, 
        bookname VARCHAR(50), 
        publisher VARCHAR(50), 
        price INT
    );
    """
)
cursor.execute(
    """
    CREATE TABLE Customer (
        custid INT PRIMARY KEY,
        name VARCHAR(3),
        address VARCHAR(50),
        phone VARCHAR(13)
    );
    """
)
cursor.execute(
    """
    CREATE TABLE Orders (
        orderid INT PRIMARY KEY, 
        custid INT, 
        bookid INT, 
        saleprice INT,
        orderdate DATE,
        FOREIGN KEY (bookid) REFERENCES Book(bookid),
        FOREIGN KEY (custid) REFERENCES Customer(custid)
    );
    """
)

book_data = [
    (1, "축구의 역사", "굿스포츠", 7000),
    (2, "축구 아는 여자", "나무수", 13000),
    (3, "축구의 이해", "대한미디어", 22000),
    (4, "골프 바이블", "대한미디어", 35000),
    (5, "피겨 교본", "굿스포츠", 8000),
    (6, "역도 단계별기술", "굿스포츠", 6000),
    (7, "야구의 추억", "이상미디어", 20000),
    (8, "야구를 부탁해", "이상미디어", 13000),
    (9, "올림픽 이야기", "삼성당", 7500),
    (10, "Olympic Champions", "Pearson", 13000)
]

orders_data = [
    (1, 1, 1, 6000, "2020-07-01"),
    (2, 1, 3, 21000, "2020-07-03"),
    (3, 2, 5, 8000, "2020-07-03"),
    (4, 3, 6, 6000, "2020-07-04"),
    (5, 4, 7, 20000, "2020-07-05"),
    (6, 1, 2, 12000, "2020-07-07"),
    (7, 4, 8, 13000, "2020-07-07"),
    (8, 3, 10, 12000, "2020-07-08"),
    (9, 2, 10, 7000, "2020-07-09"),
    (10, 3, 8, 13000, "2020-07-10")
]

customer_data = [
    (1, "박지성", "영국 맨체스터", "000-5000-0001"),
    (2, "김연아", "대한민국 서울", "000-6000-0001"),
    (3, "장미란", "대한민국 강원도", "000-7000-0001"),
    (4, "추신수", "미국 클리블랜드", "000-8000-0001"),
    (5, "박세리", "대한민국 대전", None)
]

cursor.executemany("INSERT INTO Book (bookid, bookname, publisher, price) VALUES (%s, %s, %s, %s);", book_data)
cursor.executemany("INSERT INTO Customer (custid, name, address, phone) VALUES (%s, %s, %s, %s);", customer_data)
cursor.executemany("INSERT INTO Orders (orderid, custid, bookid, saleprice, orderdate) VALUES (%s, %s, %s, %s, %s);", orders_data)

connection.commit()
cursor.close()
connection.close()

