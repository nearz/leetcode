package main

import (
	"fmt"
	"math"
)

type MinStack struct {
	min   int
	stack []int
}

func New() *MinStack {
	m := &MinStack{
		min:   0,
		stack: []int{},
	}
	return m
}

func (m *MinStack) Push(val int) {
	if len(m.stack) == 0 {
		m.stack = append(m.stack, 0)
		m.min = val
	} else {
		m.stack = append(m.stack, val-m.min)
		if val < m.min {
			m.min = val
		}
	}
}

func (m *MinStack) Pop() {
	if len(m.stack) == 0 {
		return
	}
	pop := m.stack[len(m.stack)-1]
	if pop < 0 {
		m.min = m.min - pop
	}
	m.stack = m.stack[:len(m.stack)-1]
}

func (m *MinStack) Top() int {
	// Probably would typically return an error
	if len(m.stack) == 0 {
		return math.MaxInt
	}
	top := m.stack[len(m.stack)-1]
	if top < 0 {
		return m.min
	}
	return top + m.min
}

func (m *MinStack) GetMin() int {
	// Probably would typically return an error
	if len(m.stack) == 0 {
		return math.MaxInt
	} else {
		return m.min
	}
}

func main() {
	ms := New()
	ms.Push(-1)
	ms.Push(5)
	ms.Push(0)
	ms.Push(-5)
	fmt.Println(ms.GetMin())
	ms.Pop()
	fmt.Println(ms.GetMin())
	ms.Pop()
	fmt.Println(ms.GetMin())
	ms.Pop()
	fmt.Println(ms.GetMin())
	ms.Pop()
	ms.Push(4)
	ms.Push(-4)
	ms.Push(2)
	fmt.Println(ms.GetMin())
	ms.Pop()
	fmt.Println(ms.GetMin())
	ms.Pop()
	fmt.Println(ms.GetMin())
}
