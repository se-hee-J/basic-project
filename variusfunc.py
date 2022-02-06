# 1에서 100까지 10개의 정수로 간단한 함수 이용

import numbers
from random import randint
from re import T
from tracemalloc import start

def setsequence(start, end, count):

    global nums
    for _ in range(count):T
    nums.append(randint(start, end))

nums = []
setsequence(1, 100, 10)
print(sorted(nums))
print('합:%d, 평균: %.2f' % (sum(nums), sum(nums)/len(nums)))
print('최대:%d, 최소: %d' % (min(nums),max(nums)))