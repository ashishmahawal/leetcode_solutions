# brute force solution
def maxArea(height):
    max_area = 0
    for i in range(0,len(height)):
        for j in range(i+1,len(height)):
            br = j - i
            ht = min(height[j],height[i])
            area = br * ht
            if area > max_area:
                max_area = area
    return max_area


# Optimal solution
def maxArea(height):
    max_area = 0
    l = 0
    r = len(height) - 1
    while l < r:
        br = r - l
        ht = min(height[l],height[r])
        area = br * ht
        if area > max_area:
            max_area = area
        if height[l] > height[r]:
            r-=1
        else:
            l+=1
    return max_area