
# input_file = 'test_input/day-02.txt'
input_file = 'input/day-02.txt'

def main():

	print("Day 02 - part 1:", part1())
	print("Day 02 - part 2:", part2())


def part1():

	with (open(input_file, 'r')) as f:
		lines = f.readlines()

	games = []
	allgames = list(range(1,101))

	max_cubes = { 'red': 12, 'green': 13, 'blue': 14 }

	for line in enumerate(lines, start=1):
		game = line[1].split(':')[1].strip()
		for _i, scores in enumerate(game.split(';')):
			for score in enumerate(scores.strip().split(',')):
				cubes = score[1].strip().split(' ')
				if int(cubes[0]) > max_cubes[cubes[1]]:
					games.append(line[0])
					break

	return sum([x for x in allgames if x not in games])


def part2():

	with (open(input_file, 'r')) as f:
		lines = f.readlines()

	games = []

	for line in enumerate(lines, start=1):
		max_cubes = { 'red': 0, 'green': 0, 'blue': 0 }
		game = line[1].split(':')[1].strip()
		for _i, scores in enumerate(game.split(';')):
			for _j, score in enumerate(scores.strip().split(',')):
				cubes = score.strip().split(' ')
				if int(cubes[0]) > max_cubes[cubes[1]]:
					max_cubes[cubes[1]] = int(cubes[0])
		games.append(max_cubes['red'] * max_cubes['green'] * max_cubes['blue'])

	return sum(games)


if __name__ == '__main__':
	main()
