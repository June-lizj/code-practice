from PIL import Image
import pytesseract
import os

file_path = 'D:/download/图片'
files = list(next(os.walk(file_path))[2])


def is_pic(file):
    return file[-4:] == '.png'


pic_name_list = list(filter(is_pic, files))


# for pic_name in pic_name_list:
#     pic_name = file_path + '/' + pic_name
#     text = pytesseract.image_to_string(Image.open(pic_name), lang='chi_sim')
#     text = text.replace(' ', '')
#     with open('pic_text.txt', 'a', encoding='utf-8') as f:
#         f.write(text)
#         f.write('\n' + '='*30 + pic_name + '='*30 + '\n')
def pic2text(pic_name):
    pic_name = file_path + '/' + pic_name
    print(pic_name)
    text = pytesseract.image_to_string((Image.open(pic_name)), lang='chi_sim')
    text = text.replace(' ', '')
    with open('pic_text.txt', 'a', encoding='utf-8') as f:
        f.write('\n' + '= ' * 30 + pic_name + '=' * 30 + '\n')
        f.write(text)


list(map(pic2text, pic_name_list))
