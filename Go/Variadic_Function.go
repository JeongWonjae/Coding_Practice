package main

func main(){
  say("this", "wonaje")
  say("onething print")
}

func say(msg ...string){
  for _,s:=range msg{ //_는 왜 이렇게 쓰는지?
    println(s)
  }
}

/* 함수를 호출 할 때 ...3개의 마침표를 이용해서 n개의 파라미터를 전달 할 수있다. */
