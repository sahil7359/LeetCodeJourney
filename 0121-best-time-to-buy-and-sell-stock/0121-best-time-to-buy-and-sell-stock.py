class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pri = float('inf')
        pro = 0
        for price in prices:
            if price<pri:
                pri=price
            else:
                pro= max(pro,price-pri)
        return pro