# Setup
import matplotlib.pyplot as plt
from skimage import color
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter, line
from skimage.io import imread
from math import degrees
from math import pi
from os import walk, path, chdir, getcwd
from os.path import abspath, dirname

# Set directory to current script location
# https://stackoverflow.com/a/69556612/13801562
chdir(dirname(abspath(__file__)))

# Functions
# https://www.tutorialspoint.com/file-searching-using-python
def find_files(filename, search_path):
   result = []

   # Walking top-down from the root
   for root, dir, files in walk(search_path):
      if filename in files:
         result.append(path.join(root, filename))
         result = str(result)
         result = result.replace("'", "")
         result = result.replace("[", "")
         result = result.replace("]", "")
   return str(result)

def grain_orientation(radians):
    if radians >= pi/3 and radians <= 2*pi/3 or radians >= 4/3*pi and radians <= 5/3*pi:
        return 'Vertical'
    else:
        return 'not Vertical'

# https://stackoverflow.com/a/23326219/13801562
def number():
    while True:
        try:
            chosen_number = int(input('\nChoose a whole number between 1 and 15,000\n\n'))
            break
        except:
            print('Your answer must be an integer between 1 and 15,000. Try again!\n')
    return chosen_number

def rice_options():
    while True:
        try:
            rice = input('\nChoose one of the following rice varietals:\nArborio\nBasmati\nIpsala\nJasmine\nKaracadag\n\n')
            break
        except:
            print('\nYour answer must be one of the following rice varietals:\nArborio\nBasmati\nIpsala\nJasmine\nKaracadag\n\n')
    return rice

# User Input Intermediate values
image_number = number()
rice_choice = rice_options()
file = find_files('{} ({}).jpg'.format(rice_choice, image_number), 'Rice_Image_Dataset')
print('\nThis should take between 1 and 10 seconds per query.\nPlease close any chart programs from this query to reset the script before running your next query.\n')
print(file)
print(getcwd())

# Data Prep
image_rgb = imread(str(file))
image_gray = color.rgb2gray(image_rgb)

# Orientation Algorithm
# https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_regionprops.html
# https://scikit-image.org/docs/stable/auto_examples/edges/plot_circular_elliptical_hough_transform.html
# Find the edges of the rice grain
edges = canny(image_gray, sigma = 2.0, low_threshold = 0.55, high_threshold = 0.8)

# Perform a Hough Ellipse Transform to find a valid elliptical approximation of the grain
# Threshold of 150 holds for a small sample of non-symmetrical rice grains
result = hough_ellipse(edges, accuracy = 20, threshold = 150)
result.sort(order = 'accumulator')

# Estimated parameters for the ellipse
best = list(result[-1])
yc, xc, a, b = (int(round(x)) for x in best[1:5])
orientation = best[5] # This is what really matters for the program

# Result
# Draw the ellipse on the original image
cy, cx = ellipse_perimeter(yc, xc, a, b, orientation)
image_rgb[cy, cx] = (250, 0, 0)

# Draw vertical reference line
vertical_line = line(0, 125, 249, 125)
image_rgb[vertical_line] = (246, 194, 139)

# Plot the rice grain and ellipse
fig, ax = plt.subplots()
ax.set_title('Rice Grain Elliptical Approximation\n${:.0f}\\degree$ from Vertical Axis\n$\\therefore$ this {} Grain is {}'.format((degrees(orientation) + 90), rice_choice, grain_orientation(orientation)),
             fontsize = 20, pad = 15).set_color('#171819')
ax.imshow(image_rgb)
# https://stackoverflow.com/a/25864515/13801562
ax.axis('off')
plt.tight_layout()
plt.show()