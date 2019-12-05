package main

import "fmt"

type myself struct {
	name string
	age  int
}

func main() {
	me := myself{}
	me.name = "정원재"
	me.age = 24
	fmt.Println("제 이름은 ", me.name, "입니다. 나이는 ", me.age, "세 입니다.")
	fmt.Print("\n")
	test()
}

func test() {
	a := myself{}
	a.name = "왓더"
	a.age = 5
	fmt.Println(a.name)
	fmt.Println("두 번째 나이는", a.age)
}
