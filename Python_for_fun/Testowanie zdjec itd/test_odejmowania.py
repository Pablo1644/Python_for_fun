import cv2

# images are in the same folder as that program
path1 = 'pierwszy.png'
path2 = 'drugi.png'


def get_difference(image_path_1, image_path_2, name_of_file):
    image1 = cv2.imread(image_path_1, 0)
    image2 = cv2.imread(image_path_2, 0)
    difference = cv2.absdiff(image1, image2)
    cv2.imwrite(str(name_of_file) + '.png', difference)


# gray_img = cv2.imread('f1.png', 0)
get_difference(path1, path2, "Test2")