def main():

	with (open('./input-01-01.txt', 'r')) as f:
		lines = f.readlines()

	# print(lines)


	alldigits = []

	for line in lines:
		digits = ['0', '0']
		line = line.strip()
		for i, c in enumerate(line):
			if c.isdigit():
				digits[0] = c
				break
		for i, c in enumerate(line[::-1]):
			if c.isdigit():
				digits[1] = c
				break

		alldigits.append(int(digits[0] + digits[1]))

	print(sum(alldigits))


if __name__ == '__main__':
	main()
