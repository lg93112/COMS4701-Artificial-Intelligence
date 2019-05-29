
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.cluster import KMeans

im = Image.open('trees.png')
rgb_im = im.convert('RGB').copy()
row, col = rgb_im.size
data = np.array(list(rgb_im.getdata()))
pix = rgb_im.load()

def kmeans_seg_img(n_clusters):
    kmeans = KMeans(n_clusters).fit(data)
    centers = np.around(kmeans.cluster_centers_).astype(int)

    for i in range(len(data)):
        y = i / row
        x = i % row
        label = kmeans.labels_[i]
        center = centers[label]
        pix[x,y] = tuple(center)

    rgb_im.show()

if __name__ == '__main__':
    for cluster in [5, 10, 15]:
        kmeans_seg_img(cluster)

