def main():

	with (open('./input-01-01.txt', 'r')) as f:
		lines = f.readlines()

	alldigits = []
	pseudonums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	rev_pseudonums = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']


	for line in lines:
		digits = ['0', '0']
		digit_pos = [99, 99]
		pseudonum_digits = ['0', '0']
		pseudonum_pos = [99, 99]
		line = line.strip()
		# look for the pseudonums first
		for i, p in enumerate(pseudonums):
			n = line.find(p)
			if n > -1:
				if n < pseudonum_pos[0]:
					pseudonum_digits[0] = str(i + 1)
					pseudonum_pos[0] = n

		for i, p in enumerate(rev_pseudonums):
			n = line[::-1].find(p)
			if n > -1:
				if n < pseudonum_pos[1]:
					pseudonum_digits[1] = str(i + 1)
					pseudonum_pos[1] = n

		for i, c in enumerate(line):
			if c.isdigit():
				digits[0] = c
				digit_pos[0] = i
				break
		for i, c in enumerate(line[::-1]):
			if c.isdigit():
				digits[1] = c
				digit_pos[1] = i
				break

		if pseudonum_pos[0] < digit_pos[0]:
			digits[0] = pseudonum_digits[0]
		if pseudonum_pos[1] < digit_pos[1]:
			digits[1] = pseudonum_digits[1]

		alldigits.append(int(digits[0] + digits[1]))

	print(alldigits)

	print(sum(alldigits))


if __name__ == '__main__':
	main()
