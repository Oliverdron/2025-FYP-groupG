Project Report: Automated Hair Removal in Image Processing

1. Introduction
This project aims to automate hair removal from images using image processing techniques such as blackhat filtering and thresholding to enhance image clarity.

2. Communication
We primarily communicated via Messenger and in-person discussions during exercise classes.

3. Familiarizing with GitHub
Since most team members were not experienced with GitHub, we began by learning its basic commands. Bartosz guided the team, and Oliver created the repository and invited the group members. During the project, we encountered merge conflicts, which Bartosz managed to resolve.

4. Labeling
We analyzed our tasks and selected 100 images for labeling. Each member labeled images separately in individual CSV files without using specialized software. Matej then consolidated all results into a single results.csv file.

5. Code Implementation
We used a slightly different approach than the original uploaded code. Oliver, with input from ChatGPT and peer discussions, implemented the code with added iter and next methods. We completed the required filepath handling and loop implementation for processing.

6. Methodology

File Handling: Images are loaded using the ImageDataLoader class, filtering files within a specific range.

Image Processing: 
readImageFile converts images to RGB and grayscale.

Hair Removal Process:

Blackhat Filtering: Highlights hair contours using morphological transformations.

Thresholding: Enhances hair structures for better segmentation.

Inpainting: Uses OpenCV’s cv2.inpaint function to remove detected hair regions and reconstruct the image.

Saving Processed Images: Output images are saved in the ./result directory using saveImageFile.

7. Interesting Findings
Our model was mostly effective, but there is still room for improvement. Unfortunately, since we did not have ground-truth images for our inputs, we could not estimate the Dice scores of our model. We could only evaluate results visually.

8. Results and Conclusion The implemented pipeline efficiently removes hair artifacts, enhancing images for further analysis. Future improvements could involve adaptive thresholding and further refinement based on theoretical learnings, such as modifying parameters and brush types for better hair removal from week 4's exercises.

9. Summary
After reviewing our work, Oliver outlined the key points for the summary, ensuring a clear presentation of our findings and methodologies.