

def main():
    games = []
    # allgames = list(range(1,101))
    allgames = list(range(1,101))
    max_cubes = { 'red': 12, 'green': 13, 'blue': 14 }

    with (open('./input-02-01.txt', 'r')) as f:
        lines = f.readlines()

    for line in enumerate(lines, start=1):
        game = line[1].split(':')[1].strip()
        for _i, scores in enumerate(game.split(';')):
            for score in enumerate(scores.strip().split(',')):
                cubes = score[1].strip().split(' ')
                if int(cubes[0]) > max_cubes[cubes[1]]: 
                    games.append(line[0])
                    break

    print([x for x in allgames if x not in games])
    print(sum([x for x in allgames if x not in games]))





if __name__ == '__main__':
        main()
