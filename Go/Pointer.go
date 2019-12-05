package main

func main() {
  var k int = 11
  var p = &k //k의 주소 할당
  println(*p) //p가 가리키는 주소에 있는 실제 내용을 출력
  println(p)
}
