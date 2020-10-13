from typing import List
def coinChangeDP(coins, rem, count: List[int]):
	if rem < 0: return -1
	if rem == 0: return 0
	if count[rem-1] != 0: return count[rem-1]
	min = sys.maxsize
	for v in coins:
		res = coinChangeDP(coins, rem-v, count)
		if res >= 0 and res < min: min = res+1
	count[rem-1] = -1 if min == sys.maxsize else min
	return count[rem-1]
