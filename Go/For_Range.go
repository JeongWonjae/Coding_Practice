package main

func main() {
  names := []string{"정", "원", "재"}

  for index, name := range names{
    println(index, name)
  }
}

/* for range 문은 "for 인덱스, 요소값:=range 컬렉션"같이 루프를 구성하는데,
range 키워드 다음의 컬렉션으로부터 하나씩 요소를 리턴해서
그 요소의 위치인덱스와 값을 for키워드 다음의 2개의 변수에 각각 할당한다. */
