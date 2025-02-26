# Projects in Data Science (2025)

**INTRODUCTION**
This project aims to automate hair removal from images using image processing techniques such as blackhat filtering and thresholding to enhance image clarity.

**COMMUNICATION**
We mainly communicated via messenger and in-person discussions during exercides classes

**FAMALIARIZING WITH GITHUB**
Our first objetive was to get familiar with github since most of us have not really used it. Thankfully Bartosz knew a lot about, so he helped us to get accustomed to the basic commands. Oliver created the repository, invited to gorup members in. During our project, we encountered some merge conflicts but Bartosz managet to solve it at some point.

**LABALING**
We first analized what we will have to do and what tasks we had. Than we looked at the data and agreed on the 100 images that we were going to label. We than did our labeling separately to different csv files. We did not use any software for that, we did it manualy on our laptops. Than Matej collected all the reults abd pushed them in one results.csv file. 

**CODE**
We used a little bit different approach than the uploaded code. Using a little ChatGPT and discussion with other students, Oliver implemented the code with added iter and next methods. We filled all the remaining required code involving the filepath name handling and the for loop for the process. 

**METHODOLOGY**
File Handling: 
Images are loaded using the ImageDataLoader class, filtering files within a specific range.
Image Processing:
readImageFile converts images to RGB and grayscale.

Hair Removal Process: 
The removeHair function performs morphological filtering to detect hair-like structures. It applies:
Blackhat Filtering: Highlights hair contours using morphological transformations.
Thresholding: Enhances hair structures for better segmentation.
Inpainting: Uses OpenCV’s cv2.inpaint function to remove detected hair regions and reconstruct the image.

Saving Processed Images: Output images are saved in the ./result directory using saveImageFile.
Results and Conclusion:
The implemented pipeline efficiently removes hair artifacts, enhancing images for further analysis. Future improvements could involve adaptive thresholding and further implementations of the theory we have learned durning classes, like changing the parameters and types of brushes fo the remove hair function that we practised in week 4.

INTERESTING THINGS WE ENCOUNTERED:
Our model was mostly doing its job but there are still a lot od room for improvements. Unfortunatelly since we did not have the ground-thuth images for our inputs, we could not estimate the dice-scores of our model. We could only look at the results and mesure by ourselves.

**SUMMARY**
We carefully looked what we have done and Oliver wrote the outline for the summary containing the main points of our work.





