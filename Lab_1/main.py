from MergeSort import merge_sort

import time
file=open('Input.txt','r')
nums= [int(i) for i in file.readline().split(',')]
start=time.time()
merge_sort(nums)
time_job=(time.time() - start)
print(f"--- {time_job} seconds ---")
print(nums)