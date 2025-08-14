package main

import "fmt"

func twoSum(numbers []int, target int) [2]int {
	if len(numbers) == 2 {
		return [2]int{1, 2}
	}

	l, r := 0, len(numbers)-1

	for l < r {
		n := numbers[l] + numbers[r]
		if n == target {
			return [2]int{l + 1, r + 1}
		} else if n > target {
			r--
		} else {
			l++
		}
	}
	return [2]int{-1, -1}
}

func main() {
	fmt.Println("MAIN:")

	// ANS: [1, 2]
	n := []int{1, 2, 3, 4}
	fmt.Printf("T1: %v\n", twoSum(n, 3))

	// ANS: [1, 3]
	n = []int{1, 2, 3, 4}
	fmt.Printf("T2: %v\n", twoSum(n, 4))

	// ANS: [1, 2]
	n = []int{-1, 0}
	fmt.Printf("T3: %v\n", twoSum(n, -1))

	// ANS: [1, 3]
	n = []int{-5, -3, 0, 1, 2}
	fmt.Printf("T4: %v\n", twoSum(n, -5))

	// ANS: [3, 6]
	n = []int{-5, -3, -2, 0, 1, 2}
	fmt.Printf("T5: %v\n", twoSum(n, 0))
}
