def test_wecode(nums):
    my_list = []
    nums_list = list(nums)
    for i in nums_list:
        if i % 2 == 0:
            my_list.append(i)
    
    return my_list
