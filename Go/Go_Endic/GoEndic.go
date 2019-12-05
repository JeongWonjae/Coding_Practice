package main

import (
	"fmt"
	"os"
	"time"
)

// 문제점은 struct 구조체가 함수간에 사용에따라 초기화를 하는 문제

type endic struct {
	saveWord map[string]string
}

func main() {
	var sel int

	fmt.Print("1: 영어단어 등록\n")
	fmt.Print("2: 영어단어 조회\n")
	fmt.Print("3: 문제 풀기\n")
	fmt.Print("4: 프로그램 종료\n\n")
	fmt.Print("번호를 입력해주세요 : ")
	fmt.Scanln(&sel)

	switch sel {
	case 1:
		fmt.Println("1.등록을 선택하셨습니다.")
		time.Sleep(2 * time.Second)
		regist()
	case 2:
		fmt.Println("2.조회를 선택하셨습니다.")
		time.Sleep(2 * time.Second)
		lookUp()
		main()
	case 3:
		fmt.Println("3.문제를 선택하셨습니다.")
		time.Sleep(2 * time.Second)
	case 4:
		fmt.Println("3초 뒤 프로그램을 종료합니다.")
		time.Sleep(2 * time.Second)
		os.Exit(3)
		fmt.Print("\n")
	}
}

func regist() {
	var eWord string
	var kWord string
	useThis := endic{}
	useThis.saveWord = make(map[string]string)
L2:
	for i := 0; i < 100; i++ {
		fmt.Print("영단어를 적어주세요 : ")
		fmt.Scanln(&eWord)
		fmt.Print("뜻을 적어주세요 : ")
		fmt.Scanln(&kWord)
		fmt.Print("\n")
		useThis.saveWord[eWord] = kWord
		var YN int

	L1:
		for {
			fmt.Print("1.메인으로 / 2.추가")
			fmt.Print("\n")
			fmt.Print("번호를 입력해주세요 : ")
			fmt.Scanln(&YN)
			if YN == 1 {
				main()
				break
			} else if YN == 2 {
				break L2
			} else {
				fmt.Print("\n")
				fmt.Print("번호를 잘못입력했습니다. 다시 입력해주세요")
				break L1
			}
		}
	}
}

func translate(key string, value string) {
	var saveWord2 map[string]string
	saveWord2 = make(map[string]string)
	saveWord2[key] = value
	fmt.Print(key, " / ", value)
}

func lookUp() {

	useThis := endic{}
	for key, value := range useThis.saveWord {
		fmt.Print(key + " = " + value + "\n")
	}
}
