class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)
        self.dictionary=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        value=self.dictionary[key]
        index=len(value)-1
        while index>-1 and value[index][0]>timestamp:
            index-=1
        if index==-1:
            return ""
        else:
            return value[index][1]
