import requests
import matplotlib.pyplot as pyplot
import numpy as np

url = "https://cdn2.poz.com/71174_RHSP-19-004.jpg_01b83f5c-df2d-41af-90e8-12f8af59feb8.jpeg"
res_status = requests.get(url, stream=True).status_code


def show_and_close_img(img):
    pyplot.imshow(img)
    pyplot.show(block=False)
    pyplot.pause(3)
    pyplot.close()


def use_local_img():
    img = pyplot.imread("domestic_k9/Doggo.jpeg")
    return img


def use_web_img():
    img_data_from_url = requests.get(url, stream=True).raw
    img = pyplot.imread(img_data_from_url, format="jpeg")
    return img


def get_dog():
    img = ""
    if res_status == requests.codes.ok:
        img = use_web_img()
    else:
        img = use_local_img()
    return img


original_dog = pyplot.imread("domestic_k9/Doggo.jpeg")


def slice_vertically(img):
    slice_width = 9
    index = 0
    step_1 = 0
    step_2 = slice_width
    dog_1 = np.empty_like(img)
    dog_2 = np.empty_like(img)

    while step_1 < np.size(img, 1):
        slice_of_dog_1 = img[:, step_1 : step_1 + slice_width]
        slice_of_dog_2 = img[:, step_2 : step_2 + slice_width]
        dog_1[:, index : index + slice_width] = slice_of_dog_1
        dog_2[:, index : index + slice_width] = slice_of_dog_2

        index += slice_width
        step_1 += slice_width * 2
        step_2 += slice_width * 2

    clean_dog_1, dirt = np.split(dog_1, 2, axis=1)
    clean_dog_2, dirt = np.split(dog_2, 2, axis=1)

    pyplot.imsave("sliced_dogs/gen_1/dog_1.jpeg", clean_dog_1)
    pyplot.imsave("sliced_dogs/gen_1/dog_2.jpeg", clean_dog_2)


def slice_horizontally(img, batch):
    slice_width = 2
    index = 0
    step_1 = 0
    step_2 = slice_width
    dog_1 = np.empty_like(img)
    dog_2 = np.empty_like(img)

    while step_1 < np.size(img, 0):
        slice_of_dog_1 = img[step_1 : step_1 + slice_width]
        slice_of_dog_2 = img[step_2 : step_2 + slice_width]
        dog_1[index : index + slice_width] = slice_of_dog_1
        dog_2[index : index + slice_width] = slice_of_dog_2

        index += slice_width
        step_1 += slice_width * 2
        step_2 += slice_width * 2

    clean_dog_1, dirt = np.split(dog_1, 2, axis=0)
    clean_dog_2, dirt = np.split(dog_2, 2, axis=0)

    dog_num = 1

    if batch <= 1:
        dog_num = 1
    else:
        dog_num = batch + 1

    pyplot.imsave(f"sliced_dogs/gen_2/dog_{dog_num}.jpeg", clean_dog_1)
    pyplot.imsave(f"sliced_dogs/gen_2/dog_{dog_num + 1}.jpeg", clean_dog_2)


slice_vertically(original_dog)

first_gen_dog_1 = pyplot.imread("sliced_dogs/gen_1/dog_1.jpeg")
first_gen_dog_2 = pyplot.imread("sliced_dogs/gen_1/dog_2.jpeg")

slice_horizontally(first_gen_dog_1, 1)
slice_horizontally(first_gen_dog_2, 2)
