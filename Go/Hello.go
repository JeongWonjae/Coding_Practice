package main

func main() {
  println("hello world")
/*
  var a int
  var f float32
  f=12.0
  // 변수는 var를 사용하여 선언한다. var키워드위에 변수명 그 다음에 변수타입을 적는다.
  var i,j,k int =1,2,3
*/
  const c int=10
  const s string="hi"
  // 상수는 const를 사용한다.

  const (
    Visa="Visa"
    Master="Mastrercard"
    Amex="American Express"
  )
  //위처럼 여러 개의 상수를 묶어서 지정할 수 있다.
  const (
    apple=iota //0
    grape //1
    orange //2
  )
  var back int=100
  var anony uint=uint(i)
  var anony2 float32=float32(i)
  println(anony, anony2)
}
