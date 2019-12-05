package main

import (
  "log"
  "os"
)

func main() {
  a, err := os.Open("C:\\temp\\test.txt")
  if err !=nil {
    log.Fatal(err.Error())
  }
  b:=a
  println(b)
  println(b)
}
// os의 Open함수는 Open(name string)(file *File, err error)과 같은 원형을
// 가지는데 첫번째는 파일 포인터를 두번째는 에러 인터페이스를 리턴한다.
// 에러 인터페이스에 값이 있으면 에러를 반환한다.
