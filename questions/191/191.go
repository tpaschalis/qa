func hammingWeight(num uint32) int {

	var sum int
	for num != 0 {
		if num&1 == 1 {
			sum++
		}
		num = num >> 1
	}

	return sum
}
