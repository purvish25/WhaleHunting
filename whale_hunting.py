import random
import math


def dist(x1, y1, x2, y2):
    return int(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))  # L_2


# This method is used to normalise the probability distribution in order to get total probability = 1
def normalize(prob):
    Z = float(sum(prob[outcome] for outcome in prob))
    for outcome in prob:
        prob[outcome] /= Z
    return prob


class Whale:
    whale_range = 10

    def __init__(self):
        self.x = random.randrange(self.whale_range)
        self.y = random.randrange(self.whale_range)

    def move(self):
        pass

        # basic whale does not move in core task

    def estimated_by(self, ship):
        ship.measure(dist(self.x, self.y, ship.x, ship.y))

    def found_by(self, ship):
        return dist(self.x, self.y, ship.x, ship.y) == 0

    def __repr__(self):
        return "Whale blows at %d,%d" % (self.x, self.y)


########################################################################
class Ship:
    def __init__(self, xwhale, ywhale):
        self.x_range = xwhale
        self.y_range = ywhale
        # this is the a priori probability
        p_w = {}
        for x in range(xwhale):
            for y in range(ywhale):
                p_w[x, y] = (1 / self.x_range * 1 / self.y_range)  # p[x,y] = p(x)*p(y)
        self.p_w = p_w
        self.x = random.randrange(self.x_range)
        self.y = random.randrange(self.y_range)

    # characteristics of distance measure: p(d|x,y) where x,y is a
    # possible position of the whale.
    # This method measures compares the distance measured by the sonar and the hypothesized distance for the
    # hypothesized location of the whale and returns 1 if it is same otherwise return 0.
    def p_d_cond_w(self, d, x, y):

        distance = dist(x, y, self.x, self.y)
        if d == distance:
            return 1
        else:
            return 0

    def measure(self, d):
        # for each possible position w=x,y of the whale
        # calculate p(w|d)
        p_w_cond_d = {}
        for x in range(whale.whale_range):
            for y in range(whale.whale_range):
                p_w_cond_d[x, y] = self.p_d_cond_w(d, x, y) * self.p_w[x, y]
                # new probabilities for whale position, if distance ’d’ has
                # been measured: p(w|d) = p(d|w) p(w)
        p_w_cond_d = normalize(p_w_cond_d)

        self.p_w = p_w_cond_d

    # This method is printing the current Bayesian model
    def show_model(self):

        for x in self.p_w:
            print(x, ' : ', self.p_w[x])
        # fill in a print routine printing the current Bayesian model
        # p(w|d) where w is the whale position (x,y)

    def move(self):
        # In the move, I am collecting all the members of the p_w who has probability grater than zero in the list
        # named lis1. Then I am choosing any random element from that list and assigning that element's coordinates to
        # the current ship position.
        lis1 = {}
        # print(lis1)

        for i in range(100):
            if list((self.p_w.values()))[i]:
                lis1.update({list(self.p_w)[i]: list((self.p_w.values()))[i]})

        temp = {}
        temp = random.choice(list(lis1))
        self.x = temp[0]
        self.y = temp[1]

    def __repr__(self):
        return "Ship at %d,%d" % (self.x, self.y)  # pretty print


def run(whale, ship):
    while not whale.found_by(ship):
        # input("Enter the distance: ")
        whale.move()
        whale.estimated_by(ship)  # ship gets distance
        ship.show_model()  # show current Bayesian model
        ship.move()  # to be  filled in
        print(whale)
        print(ship)
    print("Whale found")


whale = Whale()
ship = Ship(whale.whale_range, whale.whale_range)
run(whale, ship)
