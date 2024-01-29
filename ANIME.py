
def count_rotations(rotated):
    low =0
    high = len(rotated)-1
    while low <= high:
        mid = (low +high)//2
    if rotated[mid] <= rotated[high]:
        high = mid -1
    elif rotated[mid] >= rotated[low]:
        low = mid + 1

