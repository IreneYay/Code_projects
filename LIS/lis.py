def verify_subseq(seq, subseq):
    """
      Determines whether one sequence is a subsequence of another
    """
    if not subseq: #empty sequence is always a subsequence so we return True
        return True
    count = 0 #initialize a count
    for j in seq: #if element in seq is also in subseq
        if j == subseq[count]:
            count += 1
        if count == len(subseq):
            return True
    return False
def verify_increasing(seq):
    """
      Determines whether a sequence is in increasing order
    """
    for item in range(len(seq) - 1): #iterate through sequence
        if seq[item] >= seq[item + 1]: #if element is greater than the previous then it's not increasing
            return False
    return True
def find_lis(seq):
    """
    Finds the longest increasing subsequence of the given sequence
    """
    size = len(seq)
    pile = [[] for _ in range(size)]
    previous = [[] for _ in range(size)]
    length = 0
    for i in range(size):
        lower = 1
        upper = length
        while upper >= lower:
            #binary search
            #REFERENCE: implementation method used from https://leetcode.com/
            #code has been modified
            mid = (lower + upper + 1) // 2 # If element is present at the middle itself
            min_mid = pile[mid-1] #lower middle midpoint
            if seq[i] <= seq[min_mid]:#sequence at i is smaller than at lower middle point
                upper = mid - 1
            else:
                lower = mid + 1
        if length < lower: #lower point is greater than the longest point
            length = lower
        pile[lower-1] = i
        #Compute optimized LIS values in countdown manner
        previous[i] = pile[(lower-1) - 1] #the top of the previous pile
    index = pile[length - 1]
    sequence = [None] * length
    for i in reversed(range(len(sequence))): #traverse the sequence counting down
        sequence[i] = seq[index]
        index = previous[index] #follow pointers back to build the LIS in reverse order
    return sequence
    
