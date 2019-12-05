package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	var x [3]int
	x[0] = 1
	x[1] = 2
	x[2] = 3
	rand.Seed(time.Now().UnixNano())
	fmt.Println(rand.Intn(100))

}
