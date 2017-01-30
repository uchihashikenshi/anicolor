# coding: utf-8

import cv2
import argparse
import numpy as np


def make_contour_image(path):
    neiborhood24 = np.array([[1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1]],
                             np.uint8)
    # グレースケールで画像を読み込む.
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("gray.jpg", gray)

    # 白い部分を膨張させる.
    dilated = cv2.dilate(gray, neiborhood24, iterations=1)
    cv2.imwrite("dilated.jpg", dilated)

    # 差をとる.
    diff = cv2.absdiff(dilated, gray)
    cv2.imwrite("diff.jpg", diff)

    # 白黒反転
    contour = 255 - diff
    cv2.imwrite("./output.jpg", contour)
    return contour

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_path', dest='input_path', default='', help='input data path')
    args = parser.parse_args()

    make_contour_image(path=args.input_path)
