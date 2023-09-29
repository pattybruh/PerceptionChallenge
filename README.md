Library:
I used the cv2 and numpy libraries for the perception challenge.

Methodology:
My methodology was to first split the image in half vertically, that way the code wouldn't accidentally
confuse a cone from the right side while calculating the ones on the left and vise versa.

Then use cv2 inRange to mask out all the red-orangeish color of the cones. I didn't know how to extract
bright colors out of the image so I just set a color range that the cones were in.
https://pinetools.com/image-color-picker
I used this to get an idea of what the color of the cones were. Probably not practical in the actual car
because different weather conditions and lightings can change the cone color drastically but itll work
for this challenge problem.

Once the mask of contours is created, I used the .moments() function to find all the center points of the cones.
With the center cones I just did a means squared error linear regression on all the points to figure
out the start and end points of the line and draw it.

Once thats complete I combine the two halfs back together and the final image is what I got.