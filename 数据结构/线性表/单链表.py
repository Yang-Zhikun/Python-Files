# -*- coding: utf-8 -*-
# 单链表LinkedList

class node:
    """单链表节点"""
    def __init__(self, data = None, next: 'node' = None) -> None:
        self.data = data
        self.next: 'node' = next
        # next:'node'表示next指向的是一个node类型(node用引号包裹，表示class未定义完，要向前引用)


class LinkedList:
    """
    单链表
    结构说明：
    1.每个链表都有一个头节点head，不存放数据，指向链表的第一个节点
    """
    def __init__(self) -> None:
        self.head = node()
        self.length = 0 # 链表长度
    
    def getLength(self) -> int:
        """获取链表长度"""
        return self.length
    
    def push_back(self, data) -> None:
        """在链表尾部添加节点"""
        self.insert(self.length + 1, data)
    
    def push_head(self, data) -> None:
        """在链表头部添加节点"""
        self.insert(1, data)
    
    def insert(self, index: int, data) -> None:
        """
        在链表指定位序 index (从1开始) 处插入节点。
        self.head 视为 index=0，不存数据
        """
        if index < 1 or index > self.length + 1:
            raise IndexError("Index out of range")
        # 先定位到index-1
        cur = self.head # 此时cur的i=0
        i = 0
        while i < index - 1:
            cur = cur.next
            i += 1
        # 插入节点
        newnode = node(data, cur.next)
        cur.next = newnode
        self.length += 1
    
    def printList(self) -> None:
        """打印链表"""
        cur = self.head.next
        while cur != None:
            print(cur.data)
            cur = cur.next
        print()
        




if __name__ == "__main__":
    ll = LinkedList()
    ll.push_back("hey")
    ll.push_back(1)
    ll.push_back(66.66)
    ll.push_back("world")
    ll.push_back("你好")
    ll.push_head("头部插入")
    print("链表长度：", ll.getLength())
    print("链表内容：")
    ll.printList()