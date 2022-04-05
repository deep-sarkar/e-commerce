

def get_max_sum_subarray(arr):
    max_sum = arr[0]
    sub_arr_sum = 0
    for ele in arr:
        sub_arr_sum += ele
        if max_sum < sub_arr_sum:
            max_sum = sub_arr_sum
        if sub_arr_sum < 0:
            sub_arr_sum = 0

    return max_sum




a = [1, 2, -4, 1, 2, 3, -9]
res = get_max_sum_subarray(a)
print(res)