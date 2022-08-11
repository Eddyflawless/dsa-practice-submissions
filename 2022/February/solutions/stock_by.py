#ind local min and search for local max, sliding window;
def main(stocks):
    l,r = 0, 1 #left=buy, right=sell
    maxProfit = 0
    while r < len(stocks):
        #is it profitable ?
        if stocks[l] < stocks[r]:
            profit = stocks[r] - stocks[l]
            if profit > maxProfit:
                maxProfit = profit
        else:
            l = r
        r += 1

    return { 'buyOn': l, 'sellOn': r, 'maxProfit': maxProfit}        


if __name__ == '__main__':
    maxProfit = main([7,1,5,3,6,4])
    print(maxProfit)