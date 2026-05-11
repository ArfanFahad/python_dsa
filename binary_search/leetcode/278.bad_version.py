def isBadVersion(version):
    if version >= 4:
        return "true"
    else:
        return "false"

app_version = 5

def first_bad_version(app_version):
    left = 1
    right = app_version
    result = None
    
    while left <= right:
        mid = (left + right) // 2
        
        if isBadVersion(mid) == "true":
            right = mid - 1
            result = mid
        elif isBadVersion(mid) == "false":
            left = mid + 1
    return result
        
print(first_bad_version(app_version))   