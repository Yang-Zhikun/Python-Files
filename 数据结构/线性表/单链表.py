# -*- coding: utf-8 -*-
# 单链表LinkedList
# 结构说明：
# 1.每个链表都有一个头节点head，不存放数据，指向链表的第一个节点
class LinkedList:
    # 节点类
    class node:
        # 节点构造函数
        # :param value: 节点值
        # :param next: 指向下一个节点的指针，默认为None
        def __init__(self, value = None, next = None):
            self.value = value
            self.next = next
        
    def __init__(self):
        self.head = self.node()  # 创建一个头节点
        self.length = 0
    
    # 按位序插入
    # :param value: 要插入的值
    # :param index: 插入位置，1表示头节点之后，2表示第二个节点，依此类推
    def insert(self, value, index):
        if index < 1 or index > self.length + 1:
            raise IndexError("Linkedlist index out of range") # 索引越界
        # 找到插入位置的前一个节点
        p = self.head
        i = 0 # 从头节点开始计数
        while i < index - 1:
            p = p.next
            i = i + 1
        # 插入新节点
        newNode = self.node(value)
        newNode.next = p.next
        p.next = newNode
        self.length += 1

    # 头插法(插入到头节点之后)
    # :param value: 要插入的值

    def insert_head(self, value):
        insert(value, 1)  # 调用 insert 方法，将新节点插入到头节点之后
    
    # 尾插法
    # :param value: 要插入的值
    def insert_tail(self, value):
        insert(value, self.length + 1)  # 调用 insert 方法，将新节点插入到链表的尾部

    # 删除指定位置的节点
    # :param index: 要删除的节点位置，1表示头节点之后，2表示第二个节点，依此类推
    def remove(self, index):
        if index < 1 or index > self.length:
            raise IndexError("LinkedList index out of range") # 索引越界
        # 找到要删除节点的前一个节点
        p = self.head
        i = 0
        while i < index - 1:
            p = p.next
            i = i + 1
        val = p.next.value # 保存要删除节点的值
        p.next = p.next.next # 删除节点
        self.length -= 1
        return val
        # 注意：Python 的垃圾回收机制会自动处理对象的内存释放，所以不需要手动释放p.next所引用的节点。
    
    # 删除头节点之后的第一个节点
    def pop_head(self):
        remove(1)  # 调用 remove 方法，删除头节点之后的第一个节点

    # 删除尾节点
    def pop_tail(self):
        remove(self.length)  # 调用 remove 方法，删除链表的尾节点
        
    