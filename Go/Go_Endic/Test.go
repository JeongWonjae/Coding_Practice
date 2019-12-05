package main

import (
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

// 받을 단어 구조체
type Word struct {
	a string
	b string
	c map[string]string
}

func main() {

	//매핑DB초기화, 구조체 사용, 단일 명령
	w := Word{}
	w.c = make(map[string]string)

	fmt.Print("[질문] 등록할 단어의 개수를 입력하세요.\n->")
	var count int
	var num int
	fmt.Scan(&count)
	fmt.Print("\n[등록예시] store 가게")

	//처음 등록
	for num < count {
		//입력받기
		fmt.Print("\n[단어등록] 영어단어와 그 의미를 차례대로 입력해주세요.\n->")
		c, d := w.getWd()
		w.c[c] = d
		num++
	}

	//재등록
	for {
		fmt.Print("\n[질문] 단어등록을 추가로 하시겠습니까? (1.계속/2.중지)\n->")
		var yn int
		fmt.Scan(&yn)
		if yn == 1 {
			fmt.Print("\n[단어등록] 영어단어와 그 의미를 차례대로 입력해주세요.\n->")
			c, d := w.getWd()
			w.c[c] = d
		} else if yn == 2 {
			fmt.Print("등록을 마칩니다.\n")
			time.Sleep(2 * time.Second)
			break
		}
	}

	//여기서 보기 제작 1.모든 단어 조회 2.문제풀기
	fmt.Print("\n[질문] (1.조회) (2.문제풀기) (3.프로그램 종료) 번호를 입력해주세요\n->")
	var sel2 int
	fmt.Scan(&sel2)
	if sel2 == 1 {
		fmt.Print("\n[등록현황]", w.c, "\n")
	}
	if sel2 == 2 {
		count2 := len(w.c)
		var saveWord [10]string
		count3 := count2 - 1

		for key, value := range w.c {
			saveWord[count3] = key + ":" + value
			count3--
		}
		//랜덤으로 배열에서 데이터 가져옴
		//포문 돌려서 가져온다음에 값 받고 : 구분자를 기준으로 단어의 의미를 맞춤, 맞추면 맞췄다고 알려주고 틀리면 틀리다고 알려줌
		rand.Seed(time.Now().UnixNano())
		//fmt.Println(saveWord[rand.Intn(count2)])

		for {
			fmt.Println("\n문제풀기를 시작합니다.\n")
			sent := strings.Split(saveWord[rand.Intn(count2)], ":")

			var solve string

			fmt.Println("[알림] 1번 입력시 종료")
			fmt.Print("[문제] " + sent[0] + " 의 뜻은?\n->")
			fmt.Scan(&solve)
			TF := strings.Contains(sent[1], solve)
			//정답처리
			if solve == "1" {
				fmt.Println("프로그램을 종료합니다.")
				os.Exit(1)
			}
			if TF == true {
				fmt.Println("정답입니다.")
			}
			if TF == false {
				fmt.Println("오답입니다.")
				fmt.Println("정답은 " + sent[1])
			}
		}
		//for문

	}
	if sel2 == 3 {
		fmt.Print("프로그램을 종료합니다.")
		os.Exit(1)
	}

}

//단어 입력 받음
func (w Word) getWd() (a string, b string) {
	//여기서 입력받는다고 가정
	fmt.Scan(&w.a)
	fmt.Scan(&w.b)
	return w.a, w.b
}
