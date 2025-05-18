def pair_sum(dict, arr, sum):
    # code here
    # Hint: You can use 'in' to find if any key is in dict
    for i in arr:
        complement=sum-i
        if complement in dict:
            return True
        dict[i]=1
    return False

l= [1, 2, 3, 3, 5], sum = 2
pair_sum(l,sum)