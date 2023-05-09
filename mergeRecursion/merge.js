function mergeSort(arr) {
  // base case
  if (arr.length < 1) {
    return arr;
  }

  // split array into two halves
  const middle = Math.floor(arr.length / 2);
  const leftHalf = arr.slice(0, middle);
  const rightHalf = arr.slice(middle);

  // recursively sort each half
  const sortedLeft = mergeSort(leftHalf);
  const sortedRight = mergeSort(rightHalf);

  // merge the sorted halves
  const mergedArr = merge(sortedLeft, sortedRight);
  return mergedArr;
}

function merge(left, right) {
  const mergedArr = [];
  let leftIdx = 0;
  let rightIdx = 0;

  // merge two halves into one sorted array
  while (leftIdx < left.length && rightIdx < right.length) {
    if (left[leftIdx] < right[rightIdx]) {
      mergedArr.push(left[leftIdx]);
      leftIdx++;
    } else {
      mergedArr.push(right[rightIdx]);
      rightIdx++;
    }
  }

  // add remaining elements to merged array
  mergedArr.push(...left.slice(leftIdx));
  mergedArr.push(...right.slice(rightIdx));

  return mergedArr;
}
