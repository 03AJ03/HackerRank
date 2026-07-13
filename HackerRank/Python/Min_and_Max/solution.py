import numpy
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


a = numpy.array(arr)
minimum=numpy.min(a,axis=1)
maximum=numpy.max(minimum)
print(maximum)
