
# input_file = 'test_input/day-03.txt'
input_file = 'input/day-03.txt'

def main():

	print("Day 03 - part 1:", part1())
	print("Day 03 - part 2:", part2())


def part1():

	with (open(input_file, 'r')) as f:
		lines = f.readlines()

	part_numbers = []

	for i, line in enumerate(lines):
		line = line.strip()
		tmp_numstr = ''
		adj_symbol_found = False

		for j, c in enumerate(line):
			if c.isdigit():
				tmp_numstr += c
				if not adj_symbol_found:
					adj_symbol_found = check_matrix_pt1(i, j, lines)
			else:
				if len(tmp_numstr) and adj_symbol_found:
					part_numbers.append(int(tmp_numstr))
				tmp_numstr = ''
				adj_symbol_found = False
				continue

		# catch the number at the end of the line edge case
		if tmp_numstr and adj_symbol_found:
			part_numbers.append(int(tmp_numstr))

	return sum(part_numbers)


def part2():

	with (open(input_file, 'r')) as f:
		lines = f.readlines()

	gears = {}
	sum_value = 0

	for i, line in enumerate(lines):
		line = line.strip()
		tmp_numstr = ''
		adj_asterisk_found = (False, None, None)

		for j, c in enumerate(line):
			if c.isdigit():
				tmp_numstr += c
				if not adj_asterisk_found[0]:
					adj_asterisk_found = check_matrix_pt2(i, j, lines)
			else:
				if tmp_numstr and adj_asterisk_found[0]:
					if (adj_asterisk_found[1], adj_asterisk_found[2]) in gears:
						gears[(adj_asterisk_found[1], adj_asterisk_found[2])] *= int(tmp_numstr)
						sum_value += gears[(adj_asterisk_found[1], adj_asterisk_found[2])]
					else:
						gears[(adj_asterisk_found[1], adj_asterisk_found[2])] = int(tmp_numstr)
				tmp_numstr = ''
				adj_asterisk_found = (False, None, None)
				continue

		# catch the number at the end of the line edge case
		if tmp_numstr and adj_asterisk_found[0]:
			if tmp_numstr and adj_asterisk_found[0]:
				if (adj_asterisk_found[1], adj_asterisk_found[2]) in gears:
					gears[(adj_asterisk_found[1], adj_asterisk_found[2])] *= int(tmp_numstr)
					sum_value += gears[(adj_asterisk_found[1], adj_asterisk_found[2])]
				else:
					gears[(adj_asterisk_found[1], adj_asterisk_found[2])] = int(tmp_numstr)

	return sum_value


# check if the symbol is surrounded by other symbols in the
# surrounding 8 cells, i,j is the centre of a 3x3 matrix
def check_matrix_pt1(i, j, lines):
	for k in range(i-1, i+2):
		if k < 0 or k >= len(lines):
			continue
		for l in range(j-1, j+2):
			if l < 0 or l >= len(lines[k]):
				continue
			c = lines[k][l]
			if not c.isdigit() and not c == '.' and not c == '\n':
				return True
	return False


# check if the symbol is surrounded by other symbols in the
# surrounding 8 cells, i,j is the centre of a 3x3 matrix
def check_matrix_pt2(i, j, lines):
	for k in range(i-1, i+2):
		if k < 0 or k >= len(lines):
			continue
		for l in range(j-1, j+2):
			if l < 0 or l >= len(lines[k]):
				continue
			c = lines[k][l]
			if c == '*':
				return (True, k, l)
	return (False, None, None)


if __name__ == '__main__':
	main()
