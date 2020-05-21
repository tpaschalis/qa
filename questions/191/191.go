func hammingWeight(num uint32) int {

	var sum int
	for num != 0 {
		if num%2 == 1 {
			sum++
		}
		num = num >> 1
	}

	return sum
}
