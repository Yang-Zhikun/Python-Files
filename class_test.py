class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def get_info(self):
        return f"《{self.title}, 作者：{self.author}, 价格：{self.price}元》"

Book1 = Book("Python编程", "张三", 99.99)
Book2 = Book("数据结构与算法", "李四", 89.99)
print(Book1.get_info())
print(Book2.get_info())