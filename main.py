import os
from fractions import Fraction

from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    decoded_dict = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        decoded_dict[decoded] = value
    ret['ISO'] = decoded_dict['ISOSpeedRatings']
    ret['Shutter Speed'] = Fraction((decoded_dict['ExposureTime']))
    ret['Aperture'] = decoded_dict['MaxApertureValue']
    ret['Exposure Value'] = decoded_dict['ExposureBiasValue']
    return ret


def get_file() -> str:
    files = []
    print(os.listdir('images'))
    for file in os.listdir('images'):
        extension = os.path.splitext(file)[1]
        if extension == '.jpg' or extension == '.jpeg':
            files.append(file)
    for i in range(len(files)):
        print(str(i + 1) + ') ' + files[i])

    chosen_file = -1
    while chosen_file < 0 or chosen_file >= len(files):
        chosen_file = int(input('Which file would you like to look at?')) - 1
    return files[chosen_file]


def main():
    info = get_exif('images/' + get_file())
    for tag in info:
        print(tag + ' = ' + str(info[tag]))


if __name__ == '__main__':
    main()
