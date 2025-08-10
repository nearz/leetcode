package main

import "fmt"

func isAnagram(s, t string) bool {
	if len(s) != len(t) {
		return false
	}

	freq := make([]int, 26)

	l := len(s)
	for i := range l {
		freq[s[i]-'a']++
		freq[t[i]-'a']--
	}

	for _, f := range freq {
		if f != 0 {
			return false
		}
	}
	return true
}

func main() {
	s := "racecar"
	t := "carrace"
	fmt.Printf("T1: %t\n", isAnagram(s, t))

	s = "jar"
	t = "jam"
	fmt.Printf("T2: %t\n", isAnagram(s, t))

	s = "xx"
	t = "x"
	fmt.Printf("T3: %t\n", isAnagram(s, t))

	s = "a"
	t = "ab"
	fmt.Printf("T4: %t\n", isAnagram(s, t))
}
