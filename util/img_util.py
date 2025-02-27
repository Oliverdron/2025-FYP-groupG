import random
import os
import cv2
import pandas as pd

#Change to get the files of different group

def readImageFile(file_path):
    # read image as an 8-bit array
    img_bgr = cv2.imread(file_path)

    # convert to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    try:
        # convert BGR
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # save the image
        success = cv2.imwrite(file_path, img_bgr)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False


class ImageDataLoader:
    def __init__(self, directory, shuffle=False, transform=None, ID='G'):
        self.directory = directory
        self.shuffle = shuffle
        self.transform = transform
        self.ID = ID

        # get a sorted list of all files in the directory
        # use the csv file to check which files are assigned to the group G
        files_to_read = pd.read_csv(self.directory +"-student.csv")
        files_to_read = files_to_read[files_to_read['Group_ID']==self.ID]['File_ID']
        self.file_list = pd.array([os.path.join(self.directory, i) for i in files_to_read])
        mask_for_missing_files = [os.path.isfile(f) for f in self.file_list]
        self.file_list = self.file_list[mask_for_missing_files]
        if not self.file_list:
            raise ValueError("No image files found in the directory. Check the data folder")

        # shuffle file list if required
        if self.shuffle:
            random.shuffle(self.file_list)

        # get the total number of batches
        self.num_batches = len(self.file_list)

    def __len__(self):
        return self.num_batches

    def __iter__(self):
        # fill in with your own code below
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < self.num_batches:
            file_path = self.file_list[self.index]
            self.index += 1
            return file_path
        else:
            raise StopIteration
            
        