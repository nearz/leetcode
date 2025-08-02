package main

import "fmt"

func maxArea(height []int) int {
	if len(height) <= 0 {
		return 0
	}
	m := 0
	l := 0
	r := len(height) - 1
	for l < r {
		w := r - l
		lh := height[l]
		rh := height[r]
		h := min(lh, rh)
		if m < w*h {
			m = w * h
		}
		if lh < rh {
			l++
		} else {
			r--
		}
	}
	return m
}

func main() {
	s1 := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	fmt.Printf("T1: %d\n", maxArea(s1))

	s2 := []int{1, 1}
	fmt.Printf("T1: %d\n", maxArea(s2))
}
