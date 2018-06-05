package main

import "fmt"

/*
func add(a []int, b []int) []int {
	c := make([]int, 2)
	c[0] = a[0]*b[1] + a[1]*b[0]
	c[1] = a[1] * b[1]
	var rrr int
	if c[0] < c[1] {
		rrr = c[0]
	} else {
		rrr = c[1]
	}
	max := 1
	for i := 1; i < rrr; i++ {
		if c[0]%i == 0 && c[1]%i == 0 {
			max = i
		}
	}
	c[0] /= max
	c[1] /= max
	return c
}

//Game return as result an irreducible fraction written as an array of integers
func Game(n int) []int {
	al := make([]int, n*2)
	rst := []int{0, 1}
	for i := 0; i < n*2-1; i++ {
		if i < n {
			al[i] = (1 + (i + 1)) * (i + 1) / 2
		} else {
			// i==8 sum(2,8)
			// i==9 sum(3,8)
			al[i] = ((i - n + 2) + n) * (2*n - i - 1) / 2
		}
	}
	// sfmt.Println(al)
	for i := 0; i < n*2-1; i++ {
		b := []int{al[i], 2 + i}
		rst = add(b, rst)
		// fmt.Println(rst)
	}
	if rst[0]%rst[1] == 0 {
		return []int{rst[0] / rst[1]}
	}
	return rst
} */

//Game return as result an irreducible fraction written as an array of integers
func Game(n int) []int {
	if n == 0 {
		return []int{0}
	}
	if n == 1 {
		return []int{1, 2}
	}

	if n*n%2 == 0 {
		return []int{n * n / 2}
	}
	return []int{n * n, 2}

}

func main() {
	fmt.Println(Game(0))
	fmt.Println(Game(1))
	fmt.Println(Game(8))
	fmt.Println(Game(40))
	// fmt.Println(add([]int{1, 2}, []int{3, 3}))
}
