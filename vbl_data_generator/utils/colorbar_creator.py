import matplotlib as mpl
import matplotlib.pyplot as plt
import png

class colorbar_creator:
    
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.cm = None
        
    def set_name(self, name):
        self.name = name
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def add_custom_colormap(self, array):
        colors_hex = []
        for i in array:
            colors_hex.append(mpl.colors.rgb2hex(i))
        self.cm = mpl.colors.LinearSegmentedColormap.from_list(self.name, colors_hex, self.width)
        
    def add_predefined_colormap(self, name):
        self.cm = plt.cm.get_cmap(name, self.width)
        
    def print_hex(self, N):
        if self.cm is not None:
            for i in range(0, self.cm.N + 1, int(self.cm.N  / (N - 1))):
                print(mpl.colors.rgb2hex(self.cm(i)))
           
    def save_colorbar(self, output_path):
        if self.cm is not None:
            colorbar = []
            for j in range(self.width):
                colorbar.extend(int(x * 255) for x in self.cm(j)[:-1])
            with open(output_path + "/" + self.name + '.png', 'wb') as f:
                w = png.Writer(self.width, self.height, greyscale=False)
                w.write(f, [colorbar])
