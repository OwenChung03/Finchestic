# Read an image with OpenCV:
import cv2
image = cv2.imread("images.jpg")
cv2.imshow("Input image", image)
cv2.waitKey()
# Extract Important Info using scipy, scikit_image, here shows repayment_date
from skimage import data, io, filters
image = data.receipt()
repayment_date = filters.sobel(image)
io.imshow(repayment_date)
io.show()
# Call API from TransUnion IDxpSM
import pandas as pd
url = 'https://www.transunion.com/product/idxp'
required_path = 'Enter a valid path'
data_path =  url + required_path
df = pd.read_csv(data_path,index_col=0)
# Pingouin library for ANOVA Analysis and Hypothesis Testing
import pandas as pd
import os

import numpy as np
import matplotlib.pyplot as plt
import pingouin as pg

# Define file paths:
file_1 = "GroupA.xlsx"
file_2 = "GroupB.xlsx"
# Read the Excel files with Pandas into a Pandas Dataframe:
Group_A_df = pd.read_excel(file_1, index_col=0)
Group_B_df = pd.read_excel(file_2, index_col=0)
Group_A = Group_A_df["Data"].values
Group_B = Group_B_df["Data"].values
fig=plt.figure(3, figsize=(5,6))
fig.clf()
plt.violinplot([Group_A, Group_B], showmedians=True)
plt.xticks([1,2], labels=["A", "B"])
plt.xlabel("Groups")
plt.ylabel("measurements")
plt.title("results")
plt.tight_layout
plt.show()
fig.savefig("results.pdf", dpi=120)
test_result = pg.ttest(Group_A, Group_B, paired=False) # Doing Hypothesis Testing
print(test_result)
# Keys Avavliable: T, p-val, dof, cohen-d, CI95%, power, BF10

# Generate random pictures with turtle library 
# But could be enhanced to create excellent artwork, align with the trade receivable real photos
# Can be replaced by fragments of the photos of receipts
from turtle import *
import turtle
from random import randint
tur = turtle.Turtle()
tur.shape('turtle')
x = randint(0, 2000000)
for i in range(x):
    tur.goto(randint(-150,0),randint(0,150))
turtle.done()