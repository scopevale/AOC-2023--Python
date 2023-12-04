import re

# input_file = 'test_input/day-04.txt'
input_file = 'input/day-04.txt'

def main():

	print("Day 04 - part 1:", part1())
	print("Day 04 - part 2:", part2())


def part1():

	with (open(input_file, 'r')) as f:
		lines = f.readlines()

	re_pattern = r"\d+"
	score = 0

	# Loop through the lines
	for line in enumerate(lines):
		numstrings = line[1].split('|')
		numbers = re.findall(re_pattern, numstrings[0].split(':')[1].strip())
		winning_numbers = sorted([int(x) for x in numbers])

		numbers = re.findall(re_pattern, numstrings[1].strip())
		my_numbers = sorted([int(x) for x in numbers])

		my_winning_numbers = sorted(list(set(winning_numbers) & set(my_numbers)))
		score += 0 if not len(my_winning_numbers) else pow(2, (len(my_winning_numbers) - 1))

	return score


def part2():

	with (open(input_file, 'r')) as f:
		lines = f.readlines()

	re_pattern = r"\d+"

	card_instances: dict = {i: 1 for i in range(1, len(lines) + 1)}

	# Loop through the lines
	for i, line in enumerate(lines):
		numstrings = line.split('|')
		numbers = re.findall(re_pattern, numstrings[0].split(':')[1].strip())
		winning_numbers = sorted([int(x) for x in numbers])

		numbers = re.findall(re_pattern, numstrings[1].strip())
		my_numbers = sorted([int(x) for x in numbers])
		duplicates = len(list(set(winning_numbers) & set(my_numbers)))
		for _ in range(1, card_instances[i + 1] + 1):
			for j in range(i + 2, i + duplicates + 2):
				card_instances[j] += 1

	total = sum(card_instances.values())
	return total


if __name__ == '__main__':
	main()
