# Requirements: Python 3 and OpenCV.
# If you don’t have OpenCV installed, install it via pip:
#     pip install opencv-python

import sys, argparse

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
            leng = len(gray_img)
       
            with open(args.dest, 'w') as dest:
                dest.write('[\n')
                for r in range(0, leng - 1):
                    dest.write('\t')
                    dest.write(str([px for px in gray_img[r]]))
                    dest.write(',\n')
                dest.write('\t')
                dest.write(str([px for px in gray_img[r]]))
                dest.write('\n]')
        except:
            print('If you don’t have OpenCV installed, install it via pip.')
            print('> pip install opencv-python')
            
       
main()