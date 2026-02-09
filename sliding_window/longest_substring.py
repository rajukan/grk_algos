'''

Input [1,1] => Output 1
Input [1,2,3,1,5,2] => Output 4, rem we are taking about substrings not subsequences

'''



def longest_substr(numlist):
    n=len(numlist)
    left=0
    max_len=0
    bucket=set()

    for right in range(n):
        while numlist[right] in bucket:
            #you do not reset, you repair it
            bucket.remove(numlist[left])
            left+=1
        bucket.add(numlist[right])
        max_len=max(max_len,len(bucket))
    print(max_len)



if __name__ == "__main__":
    arr=[1,1]
    longest_substr(arr)