import os
import numpy as np

# Contoh path ke file .npy
file_path = os.path.join('data', 'A', '0', '0.npy')

# Memuat data
keypoints = np.load(file_path)

# Menampilkan data
print(keypoints)