export const binarySearch = (list, value) => {
  let start = 0;
  let stop = list.length - 1;
  const getMiddle = () => Math.floor((start + stop) / 2);
  let middle = getMiddle();

  while(list[middle] !== value && start < stop) {
    if (value < list[middle]) {
      stop = middle - 1;
    } else {
      start = middle + 1;
    }
    middle = getMiddle();
  }
  return list[middle] !== value ? -1 : middle;
}

export const binarySearchRecursive = (list, value, count = 0) => {
  const middle = Math.floor(list.length / 2);
  if (value < list[middle]) {
    const newList = list.slice(0, middle);
    return binarySearchRecursive(newList, value, count + 0);
  } else if (value > list[middle]) {
    const newList = list.slice(middle + 1, list.length);
    const nextCount = list.length - newList.length;
    return binarySearchRecursive(newList, value, count + nextCount);
  } else if (list[middle] === value) {
    return middle + count;
  } else {
    return -1;
  }
}