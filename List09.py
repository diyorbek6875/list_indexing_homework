def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    a=len(list1)
    s=0
    i=0
    while i<a:
        if list1[0]==list1[i]:
            s+=1
        i+=1
    if a==s:
        s=True
    else:
        s=False
    return s
print(main([1,1,1,1]))