import requests
import matplotlib.pyplot as pyplot
import numpy as np

# url = "https://cdn2.poz.com/71174_RHSP-19-004.jpg_01b83f5c-df2d-41af-90e8-12f8af59feb8.jpeg"
# res_status = requests.get(url, stream=True).status_code

# TODO: Create custom numpy.ndarray type for func
def show_and_close_img(img):
    pyplot.imshow(img)
    pyplot.show(block=False)
    pyplot.pause(3)
    pyplot.close()


def use_local_img():
    img = pyplot.imread("domestic_k9/Doggo.jpeg")
    show_and_close_img(img)


def use_web_img():
    img_data_from_url = requests.get(url, stream=True).raw
    img = pyplot.imread(img_data_from_url, format="jpeg")
    show_and_close_img(img)

    # if res_status == requests.codes.ok:
    #     use_web_img()
    # else:
    #     use_local_img()


img = pyplot.imread("domestic_k9/Doggo.jpeg")

print(np.size(img, 1))


def slice():
    step = 0
    slice_of_dog = np.empty_like(img)
    slice_width = 9
    while step < np.size(img, 1):
        slice_of_dog[:, step : step + slice_width] = img[:, step : step + slice_width]
        step += slice_width * 2

    return slice_of_dog


a = slice()

pyplot.imshow(a)
pyplot.show()
