import statistics
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
res = statistics.mean(data)
print("Mean: ", res)

res = statistics.median(data)
print("median: ", res)

res = statistics.median_grouped(data)
print("50% value: ", res)

res = statistics.median_high(data)
print("median high value: ", res)

res = statistics.median_low(data)
print("median low value: ", res)

res = statistics.stdev(data)
print("standard deviation", res)

res = statistics._sum(data)
print("sum: ", res)

res = statistics._counts(data)
print("count: ", res)



