package main

import "fmt"

func isValid(s string) bool {
	stack := []rune{}
	parenMap := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	for _, c := range s {
		if p, ok := parenMap[c]; ok {
			if len(stack) > 0 && stack[len(stack)-1] == p {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		} else {
			stack = append(stack, c)
		}
	}

	if len(stack) == 0 {
		return true
	}
	return false
}

func main() {
	// ANS: True
	s := "[]"
	fmt.Printf("T1: %t\n", isValid(s))

	// ANS: True
	s = "([{}])"
	fmt.Printf("T2: %t\n", isValid(s))

	// ANS: False
	s = "[(])"
	fmt.Printf("T2: %t\n", isValid(s))
}
