package main

import (
	"fmt"
	"strings"
)

// TODO: Could be better.

func longestCommonPrefix(strs []string) string {
	l := 0
	h := minLen(strs)
	for l <= h {
		m := (l + h) / 2
		isPrefix := commonPrefix(strs[0][0:m], strs)
		if isPrefix {
			l = m + 1
		} else {
			h = m - 1
		}
	}
	return strs[0][0 : (l+h)/2]
}

func commonPrefix(pre string, strs []string) bool {
	for _, s := range strs {
		if !strings.HasPrefix(s, pre) {
			return false
		}
	}
	return true
}

func minLen(strs []string) int {
	m := len(strs[0])
	for i := 1; i < len(strs); i++ {
		if len(strs[i]) < m {
			m = len(strs[i])
		}
	}
	return m
}

func main() {
	s1 := []string{"flower", "flow", "flight"}
	fmt.Printf("T1: %s\n", longestCommonPrefix(s1))

	s2 := []string{"dog", "racecar", "car"}
	fmt.Printf("T2: %s\n", longestCommonPrefix(s2))

	s3 := []string{""}
	fmt.Printf("T3: %s\n", longestCommonPrefix(s3))

	s4 := []string{"", "a"}
	fmt.Printf("T4: %s\n", longestCommonPrefix(s4))

	s5 := []string{"a"}
	fmt.Printf("T5: %s\n", longestCommonPrefix(s5))

	s6 := []string{"ab", "a"}
	fmt.Printf("T6: %s\n", longestCommonPrefix(s6))
}

// func longestCommonPrefix(strs []string) string {
// 	pos := 1
// 	var prev string
// outter:
// 	for {
// 		set := make(map[string]struct{})
// 		for _, s := range strs {
// 			if pos > len(s) {
// 				break outter
// 			}
// 			c := string(s[0:pos])
// 			set[c] = struct{}{}
// 		}
// 		if len(set) != 1 {
// 			break
// 		}
// 		for k := range set {
// 			prev = k
// 			break
// 		}
// 		pos++
// 	}
// 	return prev
// }
