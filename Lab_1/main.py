from MergeSort import merge_sort
import time
start=time.time()
nums=[0,5,1,6,2,1,6,5,2,1,43,123,4265,12,1345,124,45]
merge_sort(nums)
time_job=(time.time() - start)
print(f"--- {time_job} seconds ---")
print(nums)