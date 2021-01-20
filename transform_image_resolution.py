from PIL import Image
import os
import argparse


def rescale_images(directory, size):
    for img in os.listdir(directory):
        im = Image.open(directory + img)
        im_resized = im.resize(size, Image.ANTIALIAS)

        if im.mode in ["RGBA", "P"]:
            im_resized = im_resized.convert("RGB")

        im_resized.save(directory + img, format='JPEG', quality=95)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'),
                        help='Image size')
    args = parser.parse_args()
    rescale_images(args.directory, args.size)
