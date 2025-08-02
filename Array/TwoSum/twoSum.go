package main

import "fmt"

func twoSum(nums []int, target int) []int {
	l := make(map[int]int)
	for i, v := range nums {
		if t, ok := l[target-v]; ok {
			return []int{i, t}
		}
		l[v] = i
	}
	return []int{}
}

func main() {
	s1 := []int{2, 7, 11, 15}
	t1 := 9
	fmt.Printf("Test 1: %v\n", twoSum(s1, t1))

	s2 := []int{3, 2, 4}
	t2 := 6
	fmt.Printf("Test 2: %v\n", twoSum(s2, t2))

	s3 := []int{3, 3}
	t3 := 6
	fmt.Printf("Test 3: %v\n", twoSum(s3, t3))
}
