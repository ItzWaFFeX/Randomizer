import random

def pick_ball_experiment():
    balls = ["red", "green", "blue","orange" ]
    result = random.choice(balls)
    probability = balls.count('red')/len(balls)
    print("The odds of pick blue are:",probability)
    
    #result

    if result == 'blue':
        return "you got it right"
    else:
        return "You lost"
print(pick_ball_experiment())