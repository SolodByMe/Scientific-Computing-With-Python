import random
import copy

class Hat:
    def __init__(self,**args):
        self.contents = []
        for key, value in args.items():
            for i in range(1,value):
                self.contents.append(key)

    def draw(self,number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents
        balls=[]
        for i in range(number_of_balls):
            drawen=random.randrange(len(self.contents))
            balls.append(self.contents.pop(drawen))
        return balls

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    expected_no_of_balls = []
    for key in expected_balls:
        expected_no_of_balls.append(expected_balls[key])
    successes = 0

    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        no_of_balls = []
        for key in expected_balls:
            no_of_balls.append(balls.count(key))

        if no_of_balls >= expected_no_of_balls:
            successes += 1
    return successes/num_experiments



