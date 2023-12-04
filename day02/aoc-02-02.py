
def main():
	games = []

	with (open('./input-02-01.txt', 'r')) as f:
		lines = f.readlines()

	for line in enumerate(lines, start=1):
		max_cubes = { 'red': 0, 'green': 0, 'blue': 0 }
		game = line[1].split(':')[1].strip()
		for _i, scores in enumerate(game.split(';')):
			for _j, score in enumerate(scores.strip().split(',')):
				cubes = score.strip().split(' ')
				if int(cubes[0]) > max_cubes[cubes[1]]:
					max_cubes[cubes[1]] = int(cubes[0])
		games.append(max_cubes['red'] * max_cubes['green'] * max_cubes['blue'])

	print(sum(games))

if __name__ == '__main__':
	main()
