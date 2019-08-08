# -*- coding: utf-8 -*-

import math
import random

K = 5
FILE = open("data/iris.data", 'r')
TRAINING_BASE_SIZE = 75
TEST_BASE_SIZE = 150 - TRAINING_BASE_SIZE
HITS_COUNT = 0
ERRORS_COUNT = 0


class Iris(object):
    def __init__(self, iris_date):
        array_s = iris_date.split(',')
        self.sepal_length = float(array_s[0])
        self.sepal_width = float(array_s[1])
        self.petal_length = float(array_s[2])
        self.petal_width = float(array_s[3])

        name = array_s[4]
        self.class_name = name.replace('\n', '')


class IrisNeighbor(object):
    def __init__(self, iris, distance):
        self.iris = iris
        self.dist = distance


def do_calculate_distance(iris_training, iris_test):
    d_w = iris_training.sepal_length - iris_test.sepal_length
    d_x = iris_training.sepal_width - iris_test.sepal_width
    d_y = iris_training.petal_length - iris_test.petal_length
    d_z = iris_training.petal_width - iris_test.petal_width

    d_w_pow = math.pow(d_w, 2)
    d_x_pow = math.pow(d_x, 2)
    d_y_pow = math.pow(d_y, 2)
    d_z_pow = math.pow(d_z, 2)

    return math.sqrt(d_w_pow + d_x_pow + d_y_pow + d_z_pow)


def do_train(instance):
    neighbor_array = []

    for j in range(len(training_base_array)):
        i_train = training_base_array[j]
        d = do_calculate_distance(i_train, i_test)

        iris_viz = IrisNeighbor(i_train, d)
        neighbor_array.append(iris_viz)

    neighbor_array.sort(key=lambda a: a.dist)

    array_knn = []

    for j in range(K):
        i_v = neighbor_array[j]
        array_knn.append(i_v)

    iris_setosa_quantity = 0
    iris_versicolour_quantity = 0
    iris_virginica_quantity = 0

    for j in range(len(array_knn)):
        i_v = array_knn[j]

        if i_v.iris.class_name == "Iris-setosa":
            iris_setosa_quantity = iris_setosa_quantity + 1
        elif i_v.iris.class_name == "Iris-versicolor":
            iris_versicolour_quantity = iris_versicolour_quantity + 1
        if i_v.iris.class_name == "Iris-virginica":
            iris_virginica_quantity = iris_virginica_quantity + 1

    return do_decide(iris_setosa_quantity, iris_versicolour_quantity, iris_virginica_quantity)


def do_decide(iris_setosa_quantity, iris_versicolour_quantity, iris_virginica_quantity):
    if iris_setosa_quantity > iris_versicolour_quantity and iris_setosa_quantity > iris_virginica_quantity:
        return "Iris-setosa"
    elif iris_versicolour_quantity > iris_virginica_quantity:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"


if __name__ == "__main__":
    lines = FILE.readlines()
    random.shuffle(lines)

    training_base_array = []
    test_base_array = []

    for i in range(len(lines)):
        iris = Iris(lines[i])

        if i < TRAINING_BASE_SIZE:
            training_base_array.append(iris)
        else:
            test_base_array.append(iris)

    for i in range(len(test_base_array)):
        i_test = test_base_array[i]

        decision = do_train(i_test)

        if i_test.class_name == decision:
            HITS_COUNT = HITS_COUNT + 1
        else:
            ERRORS_COUNT = ERRORS_COUNT + 1

    print("Amount of Hits:  ", HITS_COUNT)
    print("Amount of Errors:", ERRORS_COUNT)
    print()

    rate = (100.0 / TEST_BASE_SIZE) * HITS_COUNT
    print("Hit Rate: ", round(rate, 2), "%")
