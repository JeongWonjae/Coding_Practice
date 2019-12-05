package main

func main(){
  msg:="Hello"
  say(&msg)
  print(msg)
}

func say(msg *string){
  println(*msg)
  *msg="Changed"
}
/* msg 변수 앞에 &부호를 붙이면 msg변수의 주소를 표시하게 된다.
함수에 msg변수의 주소를 전달하게 된다.
피호출함수 say()에서는 *string과 같이 파라미터가 포인터이고,
이때 msg는 문자열을 갖는 메모리 영역의 주소
*msg로 값 변경 이를 Dereferencing이라함 */
