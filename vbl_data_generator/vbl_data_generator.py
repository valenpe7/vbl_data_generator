import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class vbl_data_generator:
    
    def __init__(self):
        pass

    def calculate_particle_colors(self, array, vmin, vmax, colormap):
        return np.float32(plt.cm.get_cmap(colormap)(mpl.colors.Normalize(vmin, vmax, clip=True)(array).data))
    
    def calculate_volume_colors(self, array, vmin, vmax):
        return np.int8(mpl.colors.Normalize(vmin, vmax, clip=True)(array).data * 255)
    
    #def generate_volume(self, arrays=[], limits=[]):
    #    volumes = []
    #    for array in arrays:
    #        volumes.append(self.calculate_volume_colors(self, array, vmin, vmax))
    #    return np.stack(volumes, axis=1)
    
    def generate_binary_data(self, array, output_file):
        array.tofile(output_file)
