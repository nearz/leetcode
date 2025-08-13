package main

import "fmt"

func hasDuplicate(nums []int) bool {
	set := make(map[int]struct{})

	for _, n := range nums {
		set[n] = struct{}{}
	}

	return len(set) < len(nums)
}

func main() {
	n := []int{1, 2, 3, 3}
	fmt.Printf("T1: %t\n", hasDuplicate(n))

	n2 := []int{1, 2, 3, 4}
	fmt.Printf("T2: %t\n", hasDuplicate(n2))

	n3 := []int{}
	fmt.Printf("T3: %t\n", hasDuplicate(n3))
}
