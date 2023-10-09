from MergeSort import merge_sort

import time
file=open('Input.txt','r')
nums= [int(i) for i in file.readline().split(',')]
file.close()

start=time.time()
merge_sort(nums)
time_job=(time.time() - start)

file =open('Result.txt','w')
file.write(str(nums))
print(f"{len(nums)} numbers per {time_job} seconds")
