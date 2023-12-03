import random

def expected_run(n):
    k = 0
    baserunner = 0
    runs = 0
    total_run = []
    for i in range(41):
        if n[i] == "K":
            k += 1
            if k == 3:    
                total_run.append(runs)
                runs = 0
                k = 0
                baserunner = 0
        elif n[i] == "B":
            if baserunner == 3:
                runs += 1
                baserunner = 3
            else:
                baserunner += 1
        elif n[i] == "H":   
            runs = baserunner + 1
            baserunner = 0
    sum_run = sum(total_run)
    return sum_run
    
train = 10000
sum_of_run = 0
for i in range (train):
    game = ['B'] * 10 + ['K'] * 26 + ['H'] * 4
    random.shuffle(game)
    game.append("K")
    sum_of_run += expected_run(game)

print(sum_of_run/(train*9))
