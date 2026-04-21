package solution

// Solution calculates the count of non-divisors for each element in the input array.
// For each element A[i], it counts how many elements in the array do not divide A[i].
func Solution(numbers []int) []int {
	numberOfElements := len(numbers)

	if numberOfElements == 0 {
		return []int{}
	}

	// Find the maximum value to size our frequency arrays
	maximumValue := 0
	for _, number := range numbers {
		if number > maximumValue {
			maximumValue = number
		}
	}

	// Count how many times each value appears in the input array
	elementFrequency := make([]int, maximumValue+1)
	for _, number := range numbers {
		elementFrequency[number]++
	}

	// For each possible divisor d (from 1 to maxVal), add its frequency
	// to every multiple of d. This tells us how many array elements divide each value.
	numberOfDivisors := make([]int, maximumValue+1)
	for divisor := 1; divisor <= maximumValue; divisor++ {
		if elementFrequency[divisor] > 0 {
			for multiple := divisor; multiple <= maximumValue; multiple += divisor {
				numberOfDivisors[multiple] += elementFrequency[divisor]
			}
		}
	}

	// Build the result: for each element, non-divisor count = total elements - divisor count
	nonDivisorCounts := make([]int, numberOfElements)
	for index, number := range numbers {
		nonDivisorCounts[index] = numberOfElements - numberOfDivisors[number]
	}

	return nonDivisorCounts
}
