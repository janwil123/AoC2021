package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input01.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	nums := make([]int, 0)
	var n int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n, _ = strconv.Atoi(scanner.Text())
		nums = append(nums, n)
	}

	l := len(nums)
	c := 0

	for i := 0; i < l-1; i++ {
		if nums[i] < nums[i+1] {
			c += 1
		}
	}

	fmt.Println(c)

	c = 0
	d := nums[0] + nums[1] + nums[2]
	var e int
	for i := 0; i < l-3; i++ {
		e = d - nums[i] + nums[i+3]
		if d < e {
			c += 1
		}
	}

	fmt.Println(c)

}
