package main

import (
	"fmt"
	"sort"
)

func singleNumber(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	// return xor(nums)
	sort.Ints(nums)
	l := len(nums)
	var a int
	for i := 0; i < l; {
		if i == l-1 {
			a = nums[i]
			break
		}
		if nums[i] != nums[i+1] {
			a = nums[i]
			break
		}
		i += 2
	}
	return a
}

func xor(nums []int) int {
	res := 0
	for _, n := range nums {
		res ^= n
	}
	return res
}

func main() {
	n1 := []int{2, 2, 1}
	fmt.Printf("T1: %d\n", singleNumber(n1))

	n2 := []int{4, 1, 2, 1, 2}
	fmt.Printf("T2: %d\n", singleNumber(n2))

	n3 := []int{1}
	fmt.Printf("T3: %d\n", singleNumber(n3))
}

// NOTE: Does not use constant memory
// func singleNumber(nums []int) int {
// 	if len(nums) == 1 {
// 		return nums[0]
// 	}
// 	track := make(map[int]int)
// 	for _, n := range nums {
// 		if _, ok := track[n]; !ok {
// 			track[n] = 1
// 		} else {
// 			track[n] += 1
// 		}
// 	}
//
// 	for k, v := range track {
// 		if v == 1 {
// 			return k
// 		}
// 	}
//
// 	return 0
// }
