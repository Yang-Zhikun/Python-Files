"""
基于数组实现的哈希表
使用链式地址法解决冲突
"""
"""键值对"""
class Pair:
    def __init__(self, key: int, val):
        self.key: int = key
        self.val = val

class Array_hash_map:
    def __init__(self, capability: int = 2, resizeFactor: float = 0.75, resizeRatio: int = 2):
        """构造一个长度为capability的数组, resizeFactor为负载因子, 大于它时进行扩容; resizeRatio为扩容倍数"""
        self.capability: int = capability # 哈希表的容量


        # 简化类型注解：桶数组是“列表的列表”，每个桶存储 Pair 对象
        self.buckets: list[list[Pair]] = [[] for _ in range(capability)]
        self.size: int = 0 # 哈希表当前键值对的数量
        self.resizeFactor: float = resizeFactor # 负载因子，超过该值时需要扩容
        self.resizeRatio: int = resizeRatio # 扩容倍数
        

    def hash_func(self, key: int) -> int:
        """哈希函数, 取余法"""
        return int(key) % self.capability
    
    def loadFactor(self) -> float:
        """计算负载因子"""
        return self.size / self.capability
    
    def resize(self) -> None:
        """扩容：直接迁移键值对，避免冗余的 put 调用"""
        old_buckets = self.buckets
        self.capability *= self.resizeRatio
        self.buckets = [[] for _ in range(self.capability)]  # 新桶数组
        self.size = 0  # 重置 size，后续直接累加  
        for bucket in old_buckets:
            for pair in bucket:
                # 直接计算新索引并插入，跳过 put 的负载因子检查
                new_index = self.hash_func(pair.key)
                self.buckets[new_index].append(pair)
                self.size += 1  # 手动累加 size



    def put(self, key: int, val) -> None:
        """插入键值对"""
        # 检查是否需要扩容
        if self.loadFactor() > self.resizeFactor:
            self.resize()
        index = self.hash_func(key) # 通过哈希函数获取储存索引
        cur_bucket = self.buckets[index] # 找到index所在桶
        # 遍历桶，若遇到指定 key ，则更新对应 val 并返回
        for pair in cur_bucket:
            if pair.key == key:
                pair.val = val
                return
        # 若无该 key ，则将键值对添加至桶中
        pair = Pair(key, val)
        cur_bucket.append(pair)
        self.size += 1
    
    def get(self, key: int):
        """通过key查询val"""
        index = self.hash_func(key) # 通过哈希函数获取索引
        cur_bucket = self.buckets[index] # 找到index所在桶
        # 遍历桶，若找到 key ，则返回对应 val
        for pair in cur_bucket:
            if pair.key == key:
                return pair.val
        # 若未找到 key ，则返回 None
        return None
    
    def remove(self, key: int) -> None:
        """通过key删除键值对"""
        index = self.hash_func(key)
        cur_bucket = self.buckets[index] # 找到index所在桶
        # 遍历桶，从中删除键值对
        for pair in cur_bucket:
            if pair.key == key:
                cur_bucket.remove(pair)
                self.size -= 1
                return

    def printHashMap(self):
        """打印哈希表"""
        for bucket in self.buckets:
            for pair in bucket:
                # 直接打印，无需判断 pair 是否为 None（桶中仅含 Pair 对象）
                print(f"key: {pair.key}, val: {pair.val}")        
        print("current size:", self.size)
    
    
        
        



if __name__ == "__main__":
    hash = Array_hash_map()
    print("哈希表容量：", hash.capability)
    hash.put(123456, "name1")
    hash.put(123350, "name2")
    hash.put(23456, "name3")
    hash.put(4, "name4")
    hash.put(5, "name5")
    hash.put(6, "name6")
    print("哈希表容量：", hash.capability)


    print("打印哈希表")
    hash.printHashMap()
    print()

    print("查询：123456->", hash.get(123456))
    print("查询：123350->", hash.get(123350))
    print("查询：123213->", hash.get(123213))
    print("查询：23456 ->", hash.get(23456))

    print()
    hash.remove(23456)
    print("删除key=23456后的哈希表: ")
    hash.printHashMap()
    