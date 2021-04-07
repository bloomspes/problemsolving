class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], []
        answer = 0

        for price, amount, ordertype in orders:
            if ordertype == 0:
                if not sell:
                    heapq.heappush(buy, (-price, amount))

                else:
                    while sell and sell[0][0] <= price and amount > 0:
                        prce, amnt = heapq.heappop(sell)

                        if amount < amnt:
                            heapq.heappush(sell, (prce, amnt-amount))

                        amount -= amnt

                    if amount > 0:
                        heapq.heappush(buy, (-price, amount))

            else:
                if not buy:
                    heapq.heappush(sell, (price, amount))

                else:
                    while buy and -buy[0][0] >= price and amount > 0:
                        prce, amnt = heapq.heappop(buy)
                        prce *= -1

                        if amount < amnt:
                            heapq.heappush(buy, (-prce, amnt-amount))

                        amount -= amnt

                    if amount > 0:
                        heapq.heappush(sell, (price, amount))

        total = buy + sell
        answer = sum([i[1] for i in total]) % (10**9 + 7)

        return answer
