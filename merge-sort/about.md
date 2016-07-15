### Merge Sort

Recursive

Input: array of n numbers, unsorted:
[1, 4, 2, 6, 3, 7, 9, 5, 8]

Output: Some Numbers sorted in increasing order.

Take input array, split in half, solve each side and then add together.

#### Pseudocode

1. Recursively sort 1st half of list
2. Recursively sort 2nd half of list
3. Merge the two lists together

list = [1, 5, 3, 6, 4, 7]
length = list.length

def merge_sort(list)

end

C = output array [length = n]
A = 1st sorted array [n / 2]
B = 2nd sorted array [n / 2]
i = 1, j = 1
```
for k = i to n
  if A[i] < B[j]
    C[k] = A[i]
  else (b[j] < A[i])
    C[k] = B[j]
    j++
```

Code in Ruby
```
def merge_sort(list)
  return list if list.size <= 1
  mid = list.size / 2
  left = list[0, mid]
  right = list[mid, list.size]
  merge(merge_sort(left), merge_sort(right))
end

def merge(left, right)
  sorted = []
  until left.empty? || right.empty?
    if left.first <= right.first
      sorted << left.shift
    else
      sorted << right.shift
    end
  end
  sorted.concat(left).concat(right)
end
```

### Merge sort running time
Running time is 4m + 2
6m (since m > 1)
