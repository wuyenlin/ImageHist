import os
import cv2 as cv
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser("Set Image Histogram parameters", add_help=False)
parser.add_argument("--file_name", type=str, default='./demo.jpg')
parser.add_argument("--dpi", type=int, default=600)
parser.add_argument("--save_img", action="store_true")

args = parser.parse_args()


def ImageHist(args):
    img = cv.imread(args.file_name)
    assert img.shape[2] == 3

    hist = []
    for i in range(3):
        hist.append( cv.calcHist(images=[img], channels=[i], mask=None, histSize=[256], ranges=[0,256]) )

    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
    ax1.plot(hist[0], 'r')
    ax2.plot(hist[1], 'g')
    ax3.plot(hist[2], 'b')
    plt.xlabel('Pixel intensity')
    plt.ylabel('Number of pixels', horizontalalignment='left', position=(1,1))    

    if args.save_img:
        base = os.path.basename(args.file_name)
        name, extension = base.split('.')
        hist_file = "hist_{}.{}".format(name, extension)
        plt.savefig(hist_file, dpi=args.dpi, format=extension, bbox_inches='tight')
        print('Histogram saved as ./{}'.format(hist_file))

    plt.show()



if __name__ == '__main__':
    ImageHist(args)
