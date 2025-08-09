"""基于数组实现的哈希表"""
"""键值对"""
class Pair:
    def __init__(self, key: int, val):
        self.key: int = key
        self.val = val

class Array_hash_map:
    def __init__(self, length: int = 101):
        """构造一个长度为length的数组"""
        self.length: int = length
        
        self.data: list[Pair | None] = [None] * length

    def hash_func(self, key: int) -> int:
        """哈希函数, 取余法"""
        return int(key) % self.length
    
    def put(self, key: int, val):
        """插入键值对"""
        pair: Pair = Pair(key, val)
        index: int = self.hash_func(key) # 通过哈希函数获取储存索引
        self.data[index] = pair
    
    def get(self, key: int):
        """通过key查询val"""
        index: int = self.hash_func(key) # 通过哈希函数获取索引
        if self.data[index] != None:
            return self.data[index].val
        else:
            return None
    
    def removeByKey(self, key: int):
        """通过键进行删除"""
        index: int = self.hash_func(key)
        self.data[index] = None

    def printList(self):
        """打印哈希表"""
        for data in self.data:
            if data != None:
                print("key:", data.key, "->val:", data.val)
    
    
        
        



if __name__ == "__main__":
    hash = Array_hash_map()
    print("哈希表长度：", hash.length)
    hash.put(123456, "name1")
    hash.put(123350, "name2")
    hash.put(23456, "name3")

    print("打印哈希表")
    hash.printList()
    print()

    print("查询：123456->", hash.get(123456))
    print("查询：123350->", hash.get(123350))
    print("查询：123213->", hash.get(123213))
    print("查询：23456 ->", hash.get(23456))

    print()
    hash.removeByKey(23456)
    print("删除key=23456后的哈希表: ")
    hash.printList()

    print()
    hash.removeByVal("name2")
    print("删除val=name2后的哈希表: ")
    hash.printList()
    