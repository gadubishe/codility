# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
    # Compute and return final answer over here
    prices.sort()
    i = 0
    for x in prices:
        if x <= rupees:
            rupees -= x
            i += 1
        else:
            return i
    return i


if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)
