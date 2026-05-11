def square_root_bs(num):
    left = 0
    right = num 
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid * mid == num:
            return mid
        elif mid * mid < num:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

print(square_root_bs(20))