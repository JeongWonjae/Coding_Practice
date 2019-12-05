package main

func main(){
    count, total := sum(1,7,3,5,9)
    println(count, total)
}

func sum(nums ...int) (int,int) {
  s:=0
  count:=0
  for _, n:=range nums{
    s+=n
    count++
  }
  return count, s
}

/* go언어는 복수개의 값을 리턴할 수 있다.
sum() 옆의 괄호는 리턴 값의 데이터 타입을 지정해준다.
이 값들을 Named Return Parameter 이라고 한다.

리턴값을 비우고 NRP에 (count int, s int) 처럼 가독성을 높일 수 있다.*/
