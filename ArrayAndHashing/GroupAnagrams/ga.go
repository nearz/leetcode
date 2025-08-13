package main

import (
	"fmt"
)

func groupAnagrams(strs []string) [][]string {
	set := make(map[[26]int][]string)

	for _, str := range strs {
		hash := [26]int{}
		for _, s := range str {
			hash[s-'a']++
		}
		set[hash] = append(set[hash], str)
	}

	res := [][]string{}
	for _, v := range set {
		res = append(res, v)
	}
	return res
}

func main() {
	s1 := []string{"act", "pots", "tops", "cat", "stop", "hat"}
	fmt.Printf("T1: %v\n", groupAnagrams(s1))

	s2 := []string{"x"}
	fmt.Printf("T2: %v\n", groupAnagrams(s2))

	s3 := []string{""}
	fmt.Printf("T3: %v\n", groupAnagrams(s3))
}
