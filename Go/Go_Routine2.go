package main

import (
  "fmt"
  "sync"
)

func main(){
  // waitgroup 생성, 2개의 go루틴을 기다림
  var wait sync.WaitGroup
  wait.Add(2)

  //익명함수를 사용한 goroutine
  go func() {
    defer wait.Done() //끝이나면 done() 호출
    fmt.Println("Hello")
  }()

  //익명함수에 파라미터 전달
  go func(msg string){
    defer wait.Done() //끝이나면 done() 호출
    fmt.Println(msg)
  }("Hi")

  wait.Wait() //go루틴이 모두 끝날때 까지 기달
}
