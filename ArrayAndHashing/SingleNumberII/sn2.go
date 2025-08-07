package main

import (
	"fmt"
	"sort"
)

// NOTE: My soltion passes all test cases but violates constraint time = O(n) because of sort.
// TODO: Need to study and have better understanding of bitwise operations.

func singleNumber(nums []int) int {
	if len(nums) == 0 {
		return nums[0]
	}

	sort.Ints(nums)
	l := len(nums)
	var a int
	for i := 0; i < l; {
		if i == l-1 {
			a = nums[i]
			break
		}
		if nums[i] != nums[i+2] {
			a = nums[i]
			break
		}

		i += 3
	}
	return a
}

func main() {
	s1 := []int{2, 2, 3, 2}
	fmt.Printf("T1: %d\n", singleNumber(s1))

	s2 := []int{0, 1, 0, 1, 0, 1, 99}
	fmt.Printf("T2: %d\n", singleNumber(s2))

	s3 := []int{0, 2, 0, 2, 0, 2, 1}
	fmt.Printf("T3: %d\n", singleNumber(s3))
}
