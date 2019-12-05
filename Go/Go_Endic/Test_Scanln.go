package main

import "fmt"

func main() {

	//한글이름받기
	var Kname string
	fmt.Print("Kname : ")
	fmt.Scanln(&Kname)
	//영어이름받기
	var Ename string
	fmt.Print("Ename : ")
	fmt.Scanln(&Ename)
	fmt.Print(Kname + ", " + Ename + "\n")

	//매핑하기
	saveName := make(map[string]string)
	saveName[Kname] = Ename
	for key, value := range saveName {
		fmt.Print(key + " = " + value + "\n")
	}
	//한번 더 받기
	fmt.Print("Kname : ")
	fmt.Scanln(&Kname)
	fmt.Print("Ename : ")
	fmt.Scanln(&Ename)
	saveName[Kname] = Ename
	for key, value := range saveName {
		fmt.Print(key + " = " + value + "\n")
	}

}
