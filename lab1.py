import cv2
import numpy as np

def load_image(image_path):
    
    ######### Your code goes here #########

    #######################################

    return img

def negative_image(img):

    ######### Your code goes here #########



    #######################################

    return img

def additive_factor(img, value):

    ######### Your code goes here #########



    #######################################

    return img

def multiplicative_factor(img, value):

    ######### Your code goes here #########

    




    #######################################

    return img

def draw_color_cubes(size=256):

    img = None

    ######### Your code goes here #########






    #######################################

    return img

def create_matrix(size=3):

    matrix = None

    ######### Your code goes here #########





    #######################################

    return matrix

def compute_inverse(matrix):

    inverse = None

    ######### Your code goes here #########








    #######################################

    return inverse


if __name__ == '__main__':

    image_path = 'images/Lena_24bits.bmp'
    img = load_image(image_path)

    img_additive_factor = additive_factor(img, 50)
    img_multiplicative_factor = multiplicative_factor(img, 1.1)
    img_negative = negative_image(img)
    img_color_cubes = draw_color_cubes()
    matrix = create_matrix()
    compute_inverse(matrix)
    
    cv2.imshow('image', img)
    cv2.imshow('image_additive_factor', img_additive_factor)
    cv2.imshow('image_multiplicative_factor', img_multiplicative_factor)
    cv2.imshow('image_negative', img_negative)
    cv2.imshow('color_cubes', img_color_cubes)
    cv2.waitKey(0)
