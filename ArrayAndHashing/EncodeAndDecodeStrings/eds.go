package main

import (
	"fmt"
	"strconv"
	"strings"
)

func encode(strs []string) string {
	var sb strings.Builder
	for _, s := range strs {
		sb.WriteString(fmt.Sprintf("%d#%s", len(s), s))
	}
	return sb.String()
}

func decode(str string) []string {
	var res []string

	i := 0
	back := 0
	for i < len(str) {
		if str[i] == '#' {
			n, _ := strconv.Atoi(str[back:i])
			res = append(res, str[i+1:i+n+1])
			i = i + n + 1
			back = i
		}
		i++
	}

	return res
}

func main() {
	s1 := []string{"neet", "code", "love", "you"}
	e := encode(s1)
	fmt.Printf("E1: %s\n", e)
	fmt.Printf("D1: %v\n", decode(e))

	s2 := []string{"we", "say", ":", "yes"}
	e2 := encode(s2)
	fmt.Printf("E1: %s\n", e2)
	fmt.Printf("D1: %v\n", decode(e2))
}
