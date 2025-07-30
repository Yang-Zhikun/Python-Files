"""基于数组实现的哈希表"""
class Array_hash_map:
    """键值对"""
    class Pair:
        def __init__(self, key, val):
            self.key = key
            self.val = val

    def __init__(self, length: int = 101):
        """构造一个长度为length的数组"""
        self.length = length

        self.data: list[self.Pair | None] = [None] * length

    def put(self, key, val):
        """插入键值对"""
        pair = self.Pair(key, val)
        



if __name__ == "__main__":
    hash = Array_hash_map()
    print("哈希表长度：", hash.length)