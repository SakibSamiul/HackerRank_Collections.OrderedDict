from collections import OrderedDict

N = int(input())
order = OrderedDict()
for i in range(N):
    item_name, net_price = input().rsplit(maxsplit=1)
    item_name = ''.join(item_name)
    order[item_name] = order.get(item_name, 0) + int(net_price)

for item_name, net_price in order.items():
    print(item_name, net_price)