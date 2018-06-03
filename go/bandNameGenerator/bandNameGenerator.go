package main

import (
	"fmt"
	"strings"
)

func bandNameGenerator(word string) string {
	wb := []rune(word)
	first := strings.ToUpper(string(wb[0]))
	if wb[0] == wb[len(wb)-1] {
		return first + string(wb[1:]) + string(wb[1:])
	}
	i := strings.Index(word, "-")
	wb[i+1] -= ('a' - 'A')
	return "The " + first + string(wb[1:])
}

func main() {
	fmt.Println(bandNameGenerator(string("knife")))
	fmt.Println(bandNameGenerator(string("tart")))
	fmt.Println(bandNameGenerator(string("step-daughter")))
}

// func bandNameGenerator(word string) string {
// 	if word[0] == word[len(word)-1] {
// 		return strings.Title(word + word[1:])
// 	}
// 	return strings.Title("The " + word)
// }
