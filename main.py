import requests
from matplotlib import pyplot as plt
import numpy as np


url = "https://cdn2.poz.com/71174_RHSP-19-004.jpg_01b83f5c-df2d-41af-90e8-12f8af59feb8.jpeg"


def check_web_connection():
    res_status = ""
    try:
        res_status = requests.get(url, stream=True).status_code
    except requests.exceptions.ConnectionError:
        print("Grrr, no internet, gonna use local dog.")
    return res_status


def use_local_img():
    return plt.imread("domestic_k9/local_doggo.jpeg")


def use_web_img():
    img_data_from_url = requests.get(url, stream=True).raw
    img = plt.imread(img_data_from_url, format="jpeg")
    plt.imsave("stray_k9/web_doggo.jpeg", img)
    return img


def get_dog():
    img = ""
    if check_web_connection() == requests.codes.ok:
        img = use_web_img()
    else:
        img = use_local_img()
    return img


def slice_vertically(img):
    slice_width = 9  # ! Hard coded to evenly divide img and avoid broadcasting errors.
    index = 0
    step_1 = 0
    step_2 = slice_width  # ! We need every second slice, so to catch the slices that where stepped over, we start from end of first slice.
    dog_1 = np.empty_like(img)
    dog_2 = np.empty_like(img)

    while step_1 < np.size(img, 1):
        # ! 1) Slice img;
        slice_of_dog_1 = img[:, step_1 : step_1 + slice_width]
        slice_of_dog_2 = img[:, step_2 : step_2 + slice_width]
        # ! 2) Replace empty (0) values in empty array with slice;
        dog_1[:, index : index + slice_width] = slice_of_dog_1
        dog_2[:, index : index + slice_width] = slice_of_dog_2

        # ! 3) Step once to next index in empty array to put slices next to each other;
        index += slice_width
        # ! 4) Double step in img, repeat till end of img horizontal axis.
        step_1 += slice_width * 2
        step_2 += slice_width * 2

    # ! Dirt is the empty (black) part left after slicing that we need to drop.
    # ! More less equal to half of original img.
    clean_dog_1, dirt = np.split(dog_1, 2, axis=1)
    clean_dog_2, dirt = np.split(dog_2, 2, axis=1)

    plt.imsave("sliced_dogs/gen_1/dog_1.jpeg", clean_dog_1)
    plt.imsave("sliced_dogs/gen_1/dog_2.jpeg", clean_dog_2)


# ! Same logic, different axis. Batch added to avoid overwriting puppies.
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

    plt.imsave(f"sliced_dogs/gen_2/dog_{dog_num}.jpeg", clean_dog_1)
    plt.imsave(f"sliced_dogs/gen_2/dog_{dog_num + 1}.jpeg", clean_dog_2)


def show_result_grotesque_experiment():
    use_local_doggo = False
    elder_dog = ""

    try:
        elder_dog = plt.imread("stray_k9/web_doggo.jpeg")
    except FileNotFoundError:
        use_local_doggo = True
        print("Wuf, no web doggo, will use local.")

    if use_local_doggo:
        elder_dog = plt.imread("domestic_k9/local_doggo.jpeg")

    first_gen_dog_1 = plt.imread("sliced_dogs/gen_1/dog_1.jpeg")
    first_gen_dog_2 = plt.imread("sliced_dogs/gen_1/dog_2.jpeg")

    second_gen_dog_1 = plt.imread("sliced_dogs/gen_2/dog_1.jpeg")
    second_gen_dog_2 = plt.imread("sliced_dogs/gen_2/dog_2.jpeg")
    second_gen_dog_3 = plt.imread("sliced_dogs/gen_2/dog_3.jpeg")
    second_gen_dog_4 = plt.imread("sliced_dogs/gen_2/dog_4.jpeg")

    rows = 3
    columns = 4

    fig = plt.figure(figsize=(10, 7))

    fig.add_subplot(rows, columns, 1)

    plt.imshow(elder_dog)
    plt.axis("off")
    plt.title("Elder gen 0")

    fig.add_subplot(rows, columns, 5)

    plt.imshow(first_gen_dog_1)
    plt.axis("off")
    plt.title("Senior 1 gen 1")

    fig.add_subplot(rows, columns, 6)

    plt.imshow(first_gen_dog_2)
    plt.axis("off")
    plt.title("Senior 2 gen 1")

    fig.add_subplot(rows, columns, 9)

    plt.imshow(second_gen_dog_1)
    plt.axis("off")
    plt.title("Junior 1 gen 2")

    fig.add_subplot(rows, columns, 10)

    plt.imshow(second_gen_dog_2)
    plt.axis("off")
    plt.title("Junior 2 gen 2")

    fig.add_subplot(rows, columns, 11)

    plt.imshow(second_gen_dog_3)
    plt.axis("off")
    plt.title("Junior 3 gen 2")

    fig.add_subplot(rows, columns, 12)

    plt.imshow(second_gen_dog_4)
    plt.axis("off")
    plt.title("Junior 4 gen 2")

    plt.show(block=False)
    plt.pause(7)
    plt.close()


original_dog = get_dog()

slice_vertically(original_dog)

first_gen_dog_1 = plt.imread("sliced_dogs/gen_1/dog_1.jpeg")
first_gen_dog_2 = plt.imread("sliced_dogs/gen_1/dog_2.jpeg")

slice_horizontally(first_gen_dog_1, 1)
slice_horizontally(first_gen_dog_2, 2)

show_result_grotesque_experiment()
