package main

import "fmt"

type TreeNode struct {
	val   int
	left  *TreeNode
	right *TreeNode
}

func DiameterOfBinaryTree(root *TreeNode) int {
	diam := 0
	dfs(root, &diam)
	return diam
}

func dfs(root *TreeNode, diam *int) int {
	if root == nil {
		return 0
	}
	lh := dfs(root.left, diam)
	rh := dfs(root.right, diam)
	*diam = max(*diam, lh+rh)
	return 1 + max(lh, rh)
}

func main() {
	fmt.Println("MAIN:")
	p := &TreeNode{val: 1}
	p2 := &TreeNode{val: 2}
	p3 := &TreeNode{val: 3}
	p4 := &TreeNode{val: 4}
	p5 := &TreeNode{val: 5}
	p.right = p2
	p2.left = p3
	p2.right = p4
	p3.left = p5
	fmt.Printf("T1: %d\n", DiameterOfBinaryTree(p))
}
