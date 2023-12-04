
def main():

	with open('input-03-01.txt', 'r') as f:
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
					adj_symbol_found = check_matrix(i, j, lines)
			else:
				if len(tmp_numstr) and adj_symbol_found:
					part_numbers.append(int(tmp_numstr))
				tmp_numstr = ''
				adj_symbol_found = False
				continue

		# catch the number at the end of the line edge case
		if tmp_numstr and adj_symbol_found:
			part_numbers.append(int(tmp_numstr))

	print(sum(part_numbers))


# check if the symbol is surrounded by other symbols in the
# surrounding 8 cells, i,j is the centre of a 3x3 matrix
def check_matrix(i, j, lines):
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


if __name__ == '__main__':
	main()
