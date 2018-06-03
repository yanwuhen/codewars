package main

import (
	"fmt"
)

//ToCamelCase return CamelCase string
func ToCamelCase(s string) string {
	sepList := []rune{'_', '-'}
	cList := []rune(s)
	rstList := make([]rune, 0)
	isSep := false
	preIsSep := false
	for _, c := range cList {
		isSep = false
		for _, sep := range sepList {
			if c == sep {
				isSep = true
				break
			}
		}
		if preIsSep && c <= 'z' && c >= 'a' {
			c = c + 'A' - 'a'
		}
		if !isSep {
			rstList = append(rstList, c)
		}
		preIsSep = isSep
	}
	return string(rstList)
}

func main() {
	fmt.Println(ToCamelCase("The_Stealth_Warrior"))
	fmt.Println(ToCamelCase("the-Stealth-Warrior"))
	fmt.Println(ToCamelCase("the-stealth-warrior"))
	fmt.Println(ToCamelCase("the_2tealth-warrior"))
}

// func ToCamelCase(s string) string {
// 	if s == "" {return ""}
// 	result := strings.Title(strings.Replace(strings.Replace(s, "-", " ", -1), "_", " ", -1))
// 	result = s[:1] + result[1:]
// 	result = strings.Replace(result, " ", "", -1)
// 	return result
//   }
