class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={} #key=number, value=frequency

        for i in nums:
            map[i]=map.get(i,0)+1
        
        l=sorted(map, key=lambda x: map[x], reverse=True) #turns the dict into a list with the sorting key
        return l[:k]
        