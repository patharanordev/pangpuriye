import os
import cv2 as cv
import numpy as np
import easyocr
import Levenshtein
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pdf2image import convert_from_bytes, convert_from_path
from pangpuriye.common.file_handler import FileHandler

class OCR:
    
    def __init__(self):
        self.fh = FileHandler()
        
        # Warning :
        # In easyocr.Reader(...)
        # 
        # At the first time you use, 
        # EasyOCR will then check if you have necessary model files and download them automatically. 
        # It will load model into memory which can take a few seconds depending on your hardware. 
        # After it is done, you can read as many images as you want without running this line again.
        self.reader = easyocr.Reader(['th', 'en'], gpu=True)

    def pdf2image(self, fpath):
        
        ispdf = False
        
        if '://' in fpath:
            link_path = fpath.split('/')
            if link_path[-1].split('.')[-1].lower() == 'pdf':
                fname = link_path[-1]
                pages = convert_from_path(fpath)
                ispdf = True
            else:
                fname = None
                pages = None
        else:
            fname, fbytes = self.fh.get_byte(fpath)
            pages = convert_from_bytes(fbytes, fmt='jpeg')
            ispdf = True
        
        pdffile = []
        if ispdf:
            for i, page in enumerate(pages):
                pdffile.append(page)
                
        return fname, pdffile
    
    def crop_in_area(self, img, \
             min_width, max_width, min_height, max_height, \
             fromColorRange, toColorRange, \
             filename, fpath):
        
        img = np.array(img)
        img = img[min_height:max_height, min_width:max_width]
    
        if(not os.path.exists(fpath)):
            os.mkdir(fpath)
        
        img_path = '{}/{}.png'.format(fpath, filename)
        img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        try:
            
            box = cv.inRange(img_hsv, fromColorRange, toColorRange)
            thresh = cv.threshold(box, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

            # Morph open to remove noise
            kernel = cv.getStructuringElement(cv.MORPH_RECT, (2,2))
            opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)

            # Find contours and remove small noise
            cnts = cv.findContours(opening, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            for c in cnts:
                area = cv.contourArea(c)
                if area < 50:
                    cv.drawContours(opening, [c], -1, 0, -1)

            # Invert and apply slight Gaussian blur
            result = 255 - opening
            result = cv.GaussianBlur(result, (3,3), 0)
        
            cv.imwrite(img_path, result)
        except:
            img_path = None
            
        return img_path
    
    def cropping_rect_by_colours(self, image, mask):
        contour, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        area = max(contour, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(area)
        return image[y:y+h, x:x+w]
    
    def set_easyocr_reader(self, reader):
        self.reader = reader
        
    def get_month(self, word, lang):
        month = None
        if lang == 'th':
            speed_list = ['ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.' 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.','ธ.ค.']
            leven_list = [Levenshtein.ratio('ม.ค.', word), 
                          Levenshtein.ratio('ก.พ.', word), 
                          Levenshtein.ratio('มี.ค.', word),
                          Levenshtein.ratio('เม.ย.', word),
                          Levenshtein.ratio('เม.ย.', word),
                          Levenshtein.ratio('มิ.ย.', word),
                          Levenshtein.ratio('ก.ค.', word),
                          Levenshtein.ratio('ส.ค.', word),
                          Levenshtein.ratio('ก.ย.', word),
                          Levenshtein.ratio('ต.ค.', word),
                          Levenshtein.ratio('พ.ย.', word),
                          Levenshtein.ratio('ธ.ค.', word),
                          ]
            print(leven_list)
            month = speed_list[np.argmax(leven_list)]
        return month
    
    def imshow(self, fpath):
        img = mpimg.imread(fpath)
        plt.imshow(img)
        plt.show()
        
    def todo():
        # TODO:
        # - 4-point-perspective-transform (https://github.com/jrosebr1/imutils#4-point-perspective-transform)
        pass