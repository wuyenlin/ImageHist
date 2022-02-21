import os
import cv2 as cv
import matplotlib.pyplot as plt

def ImageHist(file_name: str, DPI: int, output_dim=None):
    img = cv.imread(file_name)
    img_h, img_w = img.shape[0], img.shape[1]

    base = os.path.basename(file_name)
    name = os.path.splitext(base)[0]
    ext = os.path.splitext(base)[1]
    histb = cv.calcHist([img],[0],None,[256],[0,256])
    histg = cv.calcHist([img],[1],None,[256],[0,256])
    histr = cv.calcHist([img],[2],None,[256],[0,256])
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
    
    plt.xlabel('Pixel intensity')
    plt.ylabel('Number of pixels',horizontalalignment='left',position=(1,1))    
    figure = plt.gcf() # get current figure
    ax1.fill(histr,'r');
    ax2.fill(histg,'g');
    ax3.fill(histb,'b');
    if output_dim:
        figure.set_size_inches(image_width, image_height)#in inches
    # when saving, specify the DPI
    new_file_name = "histogram_{}{}".format(name, ext)
    print("\nThe filename is: {}".format(new_file_name))
    plt.savefig(new_file_name, dpi = DPI, bbox_inches='tight')
    plt.setp([a.get_xticklabels() for a in f.axes[:-5]], visible=True)
    plt.show()


def main():
    ImageHist('./demo.jpeg', 600)

if __name__ == '__main__':
    main()
