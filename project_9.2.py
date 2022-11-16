import threading
import time

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

THREAD_COUNT = len(ranges)


def runner(sums, i, start, end):

	sums[i] = 0
	# # end += 1
	# starter = (start+1)
	# ender = (2*(start)+(end-1)*1)
	# sums = starter/ (2*ender)

	for j in range(start, end + 1):
		sums[i] += j
	# print(starter)
	# print(ender)
	print(sums)


threads = []
sums = [0] * THREAD_COUNT

for i in range(THREAD_COUNT):
	start, end = ranges[i][0], ranges[i][1]

	t = threading.Thread(target=runner, args= (sums, i, start, end))
	t.start()
	threads.append(t)

for t in threads:
	t.join()

print(sums)
final_sum = sum(sums)
print(final_sum)
