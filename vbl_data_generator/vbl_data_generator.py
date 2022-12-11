import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class vbl_data_generator:

    def __init__(self):
        pass

    def calculate_point_colors(self, array, vmin, vmax, weight_func, colormap_name):
        norm = mpl.colors.Normalize(vmin, vmax, clip=True)(array).data
        cmap = plt.cm.get_cmap(colormap_name)(norm)
        cmap[:, -1] = weight_func(norm)
        return np.float32(cmap)

    #def calculate_texture_colors(self, array, vmin, vmax, displ_func, colormap_name):
    #    norm = mpl.colors.Normalize(vmin, vmax, clip=True)(array).data
    #    cmap = plt.cm.get_cmap(colormap_name)(norm) * 255
    #    cmap[:, -1] = displ_func(norm)
    #    return np.uint8(cmap)

    def calculate_volume_colors(self, array, vmin, vmax):
        return np.uint8(mpl.colors.Normalize(vmin, vmax, clip=True)(array).data * 255)

    #def generate_volume(self, arrays=[], limits=[]):
    #    volumes = []
    #    for array in arrays:
    #        volumes.append(self.calculate_volume_colors(self, array, vmin, vmax))
    #    return np.stack(volumes, axis=1)

    def generate_binary_data(self, array, output_file):
        array.tofile(output_file)
