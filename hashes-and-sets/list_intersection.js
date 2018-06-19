const list_intersection = (nums1, nums2) => {
  return [...new Set([...nums1].filter(x => nums2.includes(x)))]
}
