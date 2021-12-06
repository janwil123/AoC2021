package main

import (
	"bufio"
	"fmt"
	"os"
)

func bin2dec(ds []int) int {
	res := 0
	for _, d := range ds {
		if d == 0 {
			res *= 2
		} else {
			res = 2*res + 1
		}
	}
	return res
}

func main() {
	file, err := os.Open("input03.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	inp := make([]string, 0)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		inp = append(inp, scanner.Text())
	}

	l := len(inp)
	m := len(inp[0])

	sums := make([]int, 0)

	for j := 0; j < m; j++ {
		cnt := 0
		for i := 0; i < l; i++ {
			if inp[i][j] == '1' {
				cnt += 1
			}
		}
		sums = append(sums, cnt)
	}

	gamma := make([]int, 0)
	epsilon := make([]int, 0)

	for j := 0; j < m; j++ {
		if sums[j] > l/2 {
			gamma = append(gamma, 1)
			epsilon = append(epsilon, 0)
		} else {
			gamma = append(gamma, 0)
			epsilon = append(epsilon, 1)
		}
	}

	fmt.Println(bin2dec(gamma) * bin2dec(epsilon))

}
