from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            arr=self.timeMap[key]
            low, high = 0, len(arr)-1
            prev_value=""
            while low<=high:
                mid=(low+high)//2
                if arr[mid][0]==timestamp:
                    return arr[mid][1]
                elif arr[mid][0]<timestamp:
                    prev_value = arr[mid][1]
                    low=mid+1
                elif arr[mid][0]>timestamp:
                    high=mid-1
            return prev_value
            
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)