Project Summary: <br />
Automated Hair Removal in Image Processing consisting of 200 images of skin lesions. Each image is annotated with values from 0 (No hair), 1(Some hair) or 2(A lot of hair) with 101 annotated images. The goal was to create an algorithm to remove the hair from these images so we could differentiate which where cancerous and non-cancerous moulds.

1. Introduction <br />
This project aims to automate hair removal from images using image processing techniques such as blackhat filtering and thresholding to enhance image clarity.

2. Communication <br />
We primarily communicated via Messenger where we distributed the tasks in the group and wrote some messages as soon as we were done with certain tasks as all the group members could check it and see if we were in agreement. We also had in-person discussions during exercise classes.

3. Familiarizing with GitHub <br />
Since most team members were not experienced with GitHub, we began by learning its basic commands. Bartosz guided the team, and Oliver created the repository and invited the group members. During the project, we encountered merge conflicts, which Bartosz managed to resolve.

4. Labeling <br />
We analyzed our tasks and selected 101 images for labeling. Each member labeled images separately in individual CSV files without using specialized software. Nicolai joined all of these into a single results.csv file and Matej then consolidated and polished it in accordance with requirements. As a group we agreed on most of these but there were still some where there were differing opinions or one group member that judged differently.
Bellow are some images were we collectively agreed had same ratings as well as some in which where we did not agree on the density of hair, and the possible reasons for this:

![img_0788](https://github.com/user-attachments/assets/67094825-dfbf-495c-92c8-2a08909d75bf)

We all agreed that this image had a rating of 1 due to some hair presence

![img_0789](https://github.com/user-attachments/assets/3ab2f2e9-956d-441a-bbe5-27ffdd5ecc4d)

We all also agreed that this image had a rating of 2 because of the large amount of hair it contains

![img_0790](https://github.com/user-attachments/assets/12c21fd0-844b-4645-bd6a-c9af1077f508)

We all agreed that this image had a rating of 0 due to the lack of hair presence


![img_0884](https://github.com/user-attachments/assets/5db9b724-b38e-4921-b9d5-bbecd28c023b)

But we also had some in which we had a split decision in the group, where two argued that it was a 1 and the other two argued that it was a 2. When looking at it, this could be because of some factors, like the hair thickness or how dark/light the hair on the picture is, as well as how dark/light the skin is, and these factors lead to our differences in judgement. Another reason could have also been the fact that some of these lesions were dark, which could also lead to some of us not being able to notice some lighter hair in the picture. And all of these problems can also be applied to the algorithm and understand why sometimes it may not remove the hair for example.

6. Code Implementation <br />
We used a slightly different approach than the original uploaded code. Oliver, with input from ChatGPT and peer discussions, implemented the code with added iter and next methods. We completed the required filepath handling and loop implementation for processing.

7. Methodology

File Handling: <br /> Images are loaded using the ImageDataLoader class, filtering files by loading "data-student.csv", finding file names assigned to our specific group and only using said specific files.

Image Processing: <br />
readImageFile converts images to RGB and grayscale.

Hair Removal Process: <br />
Blackhat Filtering: Highlights hair contours using morphological transformations.

Thresholding: <br />
Enhances hair structures for better segmentation.

Inpainting: <br />
Uses OpenCV’s cv2.inpaint function to remove detected hair regions and reconstruct the image.

Saving Processed Images: <br />
Output images are saved in the ./result directory using saveImageFile.

8. Interesting Findings <br />
Our model was mostly effective, but there is still room for improvement. Unfortunately, since we did not have ground-truth images for our inputs, we could not estimate the Dice scores of our model. We could only evaluate results visually.

9. Results and Conclusion <br />
The implemented pipeline efficiently removes hair artifacts, enhancing images for further analysis. Future improvements could involve adaptive thresholding and further refinement based on theoretical learnings, such as modifying parameters and brush types for better hair removal from week 4's exercises.

10. Summary
After reviewing our work, Oliver outlined the key points for the summary and Nicolai helped by adding and editing some points, ensuring a clear presentation of our findings and methodologies. Matej helped with the formatting and proofreading.
