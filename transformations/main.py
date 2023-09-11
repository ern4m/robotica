#!/usr/bin/python3.11

import numpy as np
import matplotlib.pyplot as plt
import random
from dataclasses import dataclass
import typing

# classes
# @dataclass
# class Transform:
#     rotate: np.array

# functions
## suposed to be 3x3 matrix on all operations
def vec3_id(point):
    p = np.identity(3)
    p[:, 2][0:2] = point
    return p

def vec3_zeros(point):
    p = np.zeros((3, 3))
    p[:, 2][0:2] = point
    return p
    
def rotate(angle, point):
    if point.shape == (3,3):
        p = get_point(point)
        new_angle = 0
        old_angle = int(np.degrees(np.arccos(point[0][0])).round())
        print(f"old angle: {old_angle}")
        if old_angle == 0:
            new_angle = angle
            print(f"new angle if: {new_angle}")
            # print(f"new angle: {new_angle}")
        else:
            new_angle = angle + old_angle
            print(f"new angle else: {new_angle}")
        print(f"new angle: {new_angle}")
        c, s = np.cos(np.radians(new_angle)), np.sin(np.radians(new_angle))
        print(c,s)
        m_rotate = np.array([[c, -s, p[0]], [s, c, p[1]], [0, 0, 1]])
        print(m_rotate)
        return m_rotate
    else:
        angle = np.radians(angle)
        c, s = np.cos(angle), np.sin(angle)
        m_rotate = np.array([[c, -s, point[0]], [s, c, point[1]], [0, 0, 1]])
        return m_rotate
 

def translate(vec_trans, point):
    if point.shape == (3,3):
        _p = np.copy(point)
        _vec = vec3_zeros(vec_trans)
        return np.add(_p, _vec)
    else:
        m_trans = vec3_zeros(vec_trans)
        m_trans[:, 2][0:2] = point
        return m_trans

def matmull(m1, m2):
    return np.matmul(m1, m2)

def get_rot(matrix):
  return np.append(matrix[0, :2], matrix[1, :2]).reshape(2,2)

def rand_rgb():
  r = random.randrange(0, 100, 1) / 100
  g = random.randrange(0, 100, 1) / 100
  b = random.randrange(0, 100, 1) / 100
  return (r,g,b)

def get_point(matrix):
    if (matrix.shape == (3,3)):
        point = matrix[:, 2][0:2]
        return point 
    else:
        return matrix

def plot(points):
    plt.gca().set_aspect('equal')        # Set aspect ratio
    plt.xlim(-2, 8)                    # Set x-axis range
    plt.ylim(-2, 8)

    counter = 1

    for point in points:
        # print(f"P{counter} =\n{point}")
        # getting point value
        _point = get_point(point) 

        # ploting arrow from previous to next point
        xhat = np.matmul(get_rot(point), np.array([1, 0]))
        yhat = np.matmul(get_rot(point), np.array([0, 1]))

        # draw_arrow(plt, older_point, point)
        older_point = point

        legend = np.copy(_point)
        legend -= 0.5

        color = rand_rgb()
        plt.arrow(*_point, *xhat, head_width=0.05, color=color)
        plt.arrow(*_point, *yhat, head_width=0.05, color=color)
        # plt.text(*legend, f"[{point[0]:.2f}, {point[1]:.2f}]")
        plt.text(*legend, f"{ {counter} }")
        counter += 1
    plt.show()

def parse_vec(vec):
    return vec.split(",")

def log(hist):
    print(len(hist))
    for i in hist:
        print(i,"\n")

def main():
    hist = []

    _p = np.array([0,0])
    p = vec3_id(_p)
    hist.append(p)

    while True:
        selection = input("[0] - Translate\n[1] - Rotate\n[2] - Plot\n[3] - Print matrices\n[4] - Exit\n> ")
        if selection == "0":
            vec = input("Insert translation vector:\n> ")
            vec = parse_vec(vec)
            _p = translate(vec, hist[-1])
            hist.append(_p)
            log(hist)
        elif selection == "1":
            angle = input("Insert the rotation angle:\n> ")
            _p = rotate(int(angle), hist[-1])
            hist.append(_p)
            log(hist)
        elif selection == "2":
            plot(hist)
        elif selection == "3":
            log(hist)
        elif selection == "4":
            break

    return 

if __name__ == "__main__":
    main()

