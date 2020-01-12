# Requirements: Python 3 and OpenCV.
# If you don’t have OpenCV installed, install it via pip:
#     pip install opencv-python

import sys, argparse
import os, re

#
# Array in text file:
#   Can be copy/paste it to a scad file
# How to generate:
#   > python img2gray.py myimage.png myimage.txt
#
def img2Txt(destname, img):
    with open(destname, 'w') as dest:
        img2LevelsArray(dest,img)

#
# Array in scad file:
#   Can be directly imported in another scad file
#     use <myimage.scad>
#     data = levels_myimage();
# How to generate:
#   > python img2gray.py myimage.png myimage.scad
#
def img2Scad(destname, img):
    identifierChars = re.compile('[^a-zA-Z0-9_]')
    name, ext = os.path.splitext(os.path.basename(destname))
    with open(destname, 'w') as dest:
        dest.write('function levels_%s() =\n' % identifierChars.sub('', name) )
        img2LevelsArray(dest,img)
        dest.write(';\n')

def img2LevelsArray(dest, img):
    leng = len(img)
    dest.write('[\n')
    for r in range(0, leng - 1):
        dest.write('\t')
        dest.write(str([px for px in img[r]]))
        dest.write(',\n')
    dest.write('\t')
    dest.write(str([px for px in img[r]]))
    dest.write('\n]')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="the source image")
    parser.add_argument("dest", help="the dest text")

    if(len(sys.argv) < 3):
        parser.print_help()
    else:
        try:
            import cv2
            args = parser.parse_args()
            img = cv2.imread(args.src)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            name, ext = os.path.splitext(args.dest)
            ext = ext.lower()
            if ext==".txt":
                img2Txt (args.dest, gray_img)
            elif ext==".scad":
                img2Scad (args.dest, gray_img)
            else:
                print('Unsupported destination file extension: %s' % ext)

        except Exception as err:
            print("ERROR: ", format(err))
            print('If you don’t have OpenCV installed, install it via pip.')
            print('> pip install opencv-python')

main()


