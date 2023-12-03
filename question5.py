import random

game = ['B'] * 10 + ['K'] * 26 + ['H'] * 4

random.shuffle(game)
game.append("K")

game1 = ['B', 'K', 'K', 'K', 'K', 'B', 'K', 'B', 'K', 'K', 'K', 'K', 'K', 'B', 'K', 'K', 'K', 'K', 'H', 'K', 'K', 'K', 'H', 'B', 'K', 'K', 'B', 'H', 'B', 'K', 'K', 'K', 'K', 'B', 'K', 'K', 'B', 'K', 'B', 'H', 'K']

def expected_run(n):
    k = 0
    baserunner = 0
    runs = 0
    total_run = []
    for i in range(40):
        if k == 3:    
            total_run.append(runs)
            runs = 0
            k = 0
            baserunner = 0
            print(i, k, baserunner, runs, total_run)
        elif n[i] == "K":
            k += 1
            print(i, k, baserunner, runs, total_run)
        elif n[i] == "B":
            if baserunner == 3:
                runs += 1
                baserunner = 3
                print(i, k, baserunner, runs, total_run)
            else:
                baserunner += 1
                print(i, k, baserunner, runs, total_run)
        elif n[i] == "H":   
            runs = baserunner + 1
            baserunner = 0
            print(i, k, baserunner, runs, total_run)
    return total_run
    
#train = 10000
#runs = 0
#for i in range train:
    #expe
#print (game1)
print(expected_run(game1))
