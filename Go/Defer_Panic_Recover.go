package main

func main(){
  Defer()
  defer Recover()
  Panic()
}

func Panic() {
  // panic()함수는 현재 함수를 즉시 멈추고 현재 함수에 defer함수들을 모두 실행한후 리턴
  println("Inside Panic()")
  panic("stop this!")
  // 마지막에 프로그램이 에러를 내고 종료하게 된다.
}

func Recover() {
  println("Inside Recover")
  if r:=recover(); r!=nil {
    println("recoverd:", r)
  }
  // panic 함수에 의한 패닉상태를 다시 정상상태로 되돌리는 함수이다.
}

func Defer() {
  // 지연실행 defer
  // defer 키워드는 특정 문장 혹은 함수를 나중에 실행하게 한다.
  println("1")
  defer println("2")
  println("3")
}
