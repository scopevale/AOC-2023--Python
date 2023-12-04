import re


def main():
	with (open('./input-04-01.txt', 'r')) as f:
	# with (open('./input-04-01__test.txt', 'r')) as f:
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
	print(total)


if __name__ == '__main__':
	main()
