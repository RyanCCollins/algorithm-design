import pandas as pd
table = pd.read_csv('./data/integerArray.txt')

def merge_and_count_inversions(seq, start, middle, end):

    assert 0 <= start < middle < end <= len(seq)
    inversions = 0
    temp = []
    i = start
    j = middle
    while i < middle and j < end:
        if seq[i] <= seq[j]:
            temp.append(seq[i])
            i += 1
        else:
            temp.append(seq[j])
            j += 1
            inversions += middle - i
    if j == end:
        # Second subsequence is complete: process remainder of first.
        temp.extend(seq[i:middle])
    else:
        # First subsequence is complete: no need to process
        # remaininder of second, since it does not move.
        pass
    # Insert sorted results into original sequence.
    seq[start:start+len(temp)] = temp
    return inversions

def sort_and_count_inversions(seq):
    """Sort a sequence and count inversions.

    Argument: seq -- a sequence

    Result: number of inversions (cases where i < j, but seq[i] > seq[j]).

    Side effect: seq is sorted.

    """
    def sort_and_count(seq, start, end):
        if end - start < 2:
            return 0
        middle = (start + end) // 2
        return (sort_and_count(seq, start, middle)
                + sort_and_count(seq, middle, end)
                + merge_and_count_inversions(seq, start, middle, end))
    return sort_and_count(seq, 0, len(seq))

print(sort_and_count_inversions(table.values))
