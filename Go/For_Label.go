package main

func main() {
  i :=0

L1:
  for {
      if i==0{
        break L1
      }
  }
  println("ok")
}

/* break로 지정한 레이블로 이동할 수 있다.
보기에는 무한루프를 동작할 거 같지만 실제로 ok를 출력한다.
L1레이블로 간 다음 현재 for루프를 건너뛰고 다음 문장을 실행하기 때문이다. */
