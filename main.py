from os.path import join, abspath
import os
import matplotlib.pyplot as plt

from util.img_util import readImageFile, saveImageFile, ImageDataLoader
from util.inpaint_util import removeHair

#filling this for the program
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data")

image_loader = ImageDataLoader(directory=file_path)

save_dir = './result'

counter = 0

for image_path in image_loader:
    counter += 1
    # read an image file
    img_rgb, img_gray = readImageFile(image_path)

    # apply hair removal
    blackhat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=5, threshold=10)

    # plot the images
    # plt.figure(figsize=(15, 10))

    # # original image
    # plt.subplot(2, 2, 1)
    # plt.imshow(img_rgb)
    # plt.title("Original Image")
    # plt.axis("off")

    # # blackHat image
    # plt.subplot(2, 2, 2)
    # plt.imshow(blackhat, cmap="gray")
    # plt.title("BlackHat Image")
    # plt.axis("off")

    # # thresholded mask
    # plt.subplot(2, 2, 3)
    # plt.imshow(thresh, cmap="gray")
    # plt.title("Thresholded Mask")
    # plt.axis("off")

    # # inpainted image
    # plt.subplot(2, 2, 4)
    # plt.imshow(img_out)
    # plt.title("Inpainted Image")
    # plt.axis("off")

    # plt.tight_layout()
    # plt.show()

    # save the output image
    save_file_path = join(save_dir, f"output{counter}.png")
    saveImageFile(img_out, save_file_path)
