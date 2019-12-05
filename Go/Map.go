package main

func main(){
  var A map[int]string
  //키(KEY)값에 대응하는 VAULE(값)
  //map[KEY타입]VALUE타입으로 선언

  //map을 초기화하기 위해서 make()함수를 사용
  A=make(map[int]string)
  //값추가
  A[1]="JEONG"
  A[2]="WON"
  A[3]="JAE"

  str :=A[1]+A[2]+A[3]
  println(str)

  //값삭제
  delete(A, 1)
  str =A[1]+A[2]+A[3]
  println(str)

  //키체크
  var chValue string
  var exists bool
  chValue, exists =A[1]
  println(chValue)
  println(exists)

  //맵의 키와 값 열거
  for key, val := range A {
    println(key, val)
  }
}
