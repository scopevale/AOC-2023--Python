import re

def main():

	with (open('./input-04-01.txt', 'r')) as f:
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

	print(score)


if __name__ == '__main__':
	main()
