package main

func main(){
  a :=1
  for a<15{
    if a==5{
      a+=a
      continue
    }
    a++
    if a>10{
      break
    }
  }
  if a==11{
    goto END
  }
  println(a)

END:
  println("END")
}

/* 기타 임의의 문장으로 이동하기 위해 goto문을 사용할 수 있다. goto문은
for 루프와 관련없이 사용될 수 있다. */
