package main

import "fmt"

func Solution(numbers []int) []int {
	numberOfElements := len(numbers)

	if numberOfElements == 0 {
		return []int{}
	}

	maximumValue := 0
	for _, number := range numbers {
		if number > maximumValue {
			maximumValue = number
		}
	}

	elementFrequency := make([]int, maximumValue+1)
	for _, number := range numbers {
		elementFrequency[number]++
	}

	numberOfDivisors := make([]int, maximumValue+1)
	for divisor := 1; divisor <= maximumValue; divisor++ {
		if elementFrequency[divisor] > 0 {
			for multiple := divisor; multiple <= maximumValue; multiple += divisor {
				numberOfDivisors[multiple] += elementFrequency[divisor]
			}
		}
	}

	nonDivisorCounts := make([]int, numberOfElements)
	for index, number := range numbers {
		nonDivisorCounts[index] = numberOfElements - numberOfDivisors[number]
	}

	return nonDivisorCounts
}

func main() {
	testArray := []int{3, 1, 2, 3, 6}
	expectedOutput := []int{2, 4, 3, 2, 0}

	result := Solution(testArray)

	fmt.Printf("Input:    %v\n", testArray)
	fmt.Printf("Expected: %v\n", expectedOutput)
	fmt.Printf("Got:      %v\n", result)

	pass := true
	for i := range result {
		if result[i] != expectedOutput[i] {
			pass = false
		}
	}

	if pass {
		fmt.Println("✅ Test PASSED")
	} else {
		fmt.Println("❌ Test FAILED")
	}

	// Additional edge case: single element
	singleResult := Solution([]int{5})
	fmt.Printf("\nSingle element [5]: %v (expected [])\n", singleResult)

	// Edge case: all same elements
	sameResult := Solution([]int{2, 2, 2})
	fmt.Printf("All same [2,2,2]: %v (expected [0,0,0])\n", sameResult)
}
