package main

import "fmt"

func isPalindrome(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		if !isAlphaNum(s[l]) {
			l++
			continue
		}
		if !isAlphaNum(s[r]) {
			r--
			continue
		}
		if lower(s[l]) != lower(s[r]) {
			return false
		}
		l++
		r--
	}
	return true
}

func isAlphaNum(c byte) bool {
	b := 'A' <= c && c <= 'Z'
	b2 := 'a' <= c && c <= 'z'
	b3 := '0' <= c && c <= '9'
	return b || b2 || b3
}

func lower(c byte) byte {
	var bit int
	if 'A' <= c && c <= 'Z' {
		bit = 1
	}
	mask := byte(bit << 5)
	return c | mask
}

func main() {
	s := "Was it a car or a cat I saw?"
	fmt.Printf("T1: %t\n", isPalindrome(s))

	s = "tab a cat"
	fmt.Printf("T2: %t\n", isPalindrome(s))

	s = "race car"
	fmt.Printf("T3: %t\n", isPalindrome(s))
}
