package main

import (
	"fmt"
	"strconv"
	"strings"
)

//FizzBuzzCuckooClock 报音钟
//如果被3整除,Fizz
//如果被5整除,Buzz
//如果可以被3,5整除，"Fizz Buzz"
//整点报时，"Cuckoo"重复整点次(12小时进制)
//半点报时，"Cuckoo"一次
//其它情况，"tick"
func FizzBuzzCuckooClock(time string) string {
	t := strings.Split(time, ":")
	hour, _ := strconv.Atoi(t[0])
	minute, _ := strconv.Atoi(t[1])
	isDiv3 := (minute%3 == 0)
	isDiv5 := (minute%5 == 0)
	if minute == 0 {
		rst := "Cuckoo"
		cnt := hour % 12
		if cnt == 0 {
			cnt = 12
		}
		for i := 1; i < cnt; i++ {
			rst += " Cuckoo"
		}
		return rst
	}
	if minute == 30 {
		return "Cuckoo"
	}
	if isDiv3 && isDiv5 {
		return "Fizz Buzz"
	}
	if isDiv3 {
		return "Fizz"
	}
	if isDiv5 {
		return "Buzz"
	}
	return "tick"
}

func main() {
	fmt.Println(FizzBuzzCuckooClock("13:34"))
	fmt.Println(FizzBuzzCuckooClock("21:00"))
	fmt.Println(FizzBuzzCuckooClock("13:15"))
	fmt.Println(FizzBuzzCuckooClock("13:30"))
	fmt.Println(FizzBuzzCuckooClock("12:00"))
	fmt.Println(FizzBuzzCuckooClock("00:00"))
}

// func FizzBuzzCuckooClock(time string) string {
// 	h, _ := strconv.Atoi(time[0:2])
// 	m, _ := strconv.Atoi(time[3:5])
// 	switch {
// 	  case m==0:
// 		return strings.Repeat("Cuckoo ", (h+11)%12) + "Cuckoo"
// 	  case m==30:
// 		return "Cuckoo"
// 	  case m%15 == 0:
// 		return "Fizz Buzz"
// 	  case m%5 == 0:
// 		return "Buzz"
// 	  case m%3 == 0:
// 		return "Fizz"
// 	  default:
// 		return "tick"
// 	}
//   }
