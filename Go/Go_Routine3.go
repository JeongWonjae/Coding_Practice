package main

import (
  "runtime"
)

func main() {
  //5개의 cpu 사용
  runtime.GOMAXPROCS(5)
}
