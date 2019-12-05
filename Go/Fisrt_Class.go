package main

func main() {
	add:=func(i int, j int) int {
		return i+j
	}
	//add는 i+j를 할당
	//변수 add에 익명함수를 할당

	r1:=calc(add, 10, 20)
	//첫번째 인자 함수는 두번째,세번째 인자값들을 계산한다.
	println(r1)


	r2:=calc(func(x int, y int) int {return x-y},10,20)
	println(r2)
}

func calc(f func(int, int) int, a int, b int) int{
	result:=f(a,b)
	return result
}
/* 결국 calc이 첫번째는 함수 두, 세 번째는 인자라는 것을 할당해준다. 알려준다. */

/* 일급함수
다른함수의 파라미터로 전달하거나 다른 함수의 리턴값으로도 사용될 수 있다.
함수의 입려파라미터나 리턴파라미터로서 함수 자체가 사용될 수 있다. */
/*
func nextValue() func() int {
	i:=0
	return func() int{
		i++
		return i
	}
}

func main() {
	next:=nextValue()

	println(next())
	println(next())
	println(next())

	anotherNext:=nextValue()
	println(anotherNext())
	println(anotherNext())
	println(next())
}
*/
/* 클로저(Closure)
클로저는 함수 바깥에 있는 변수를 참조하는 함수값을 일컫는데, 함수는 바깥의 변수를 마치 함수 안으로 끌어들인 듯이
변수를 읽거나 사용
익명함수가 바깥에 있는 변수 i를 참조하고 있다. 익명함수 자체가 로컬 변수를 갖는것이 아니기 때문에 외부 변수 i가
상태를 계속 유지함*/
