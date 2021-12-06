package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input02.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	inp := make([][]string, 0)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		inp_arr := strings.Fields(scanner.Text())
		inp = append(inp, inp_arr)
	}

	// Task 1

	hor := 0
	ver := 0
	var n int

	for _, com := range inp {
		n, _ = strconv.Atoi(com[1])
		if com[0] == "forward" {
			hor += n
		}
		if com[0] == "down" {
			ver += n
		}
		if com[0] == "up" {
			ver -= n
		}
	}
	fmt.Println(hor * ver)

	// Task 1

	hor = 0
	ver = 0
	aim := 0

	for _, com := range inp {
		n, _ = strconv.Atoi(com[1])
		if com[0] == "forward" {
			hor += n
			ver += aim * n
		}
		if com[0] == "down" {
			aim += n
		}
		if com[0] == "up" {
			aim -= n
		}
	}
	fmt.Println(hor * ver)

}
