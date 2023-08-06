import cv2
import argparse
import re
import ctypes
from PIL import Image
import img2pdf
import os
import pytesseract
import pymongo
from pdf2image import convert_from_path
import math
import cv2
import numpy as np
from typing import Tuple, Union
from deskew import determine_skew

#function to rotate and remove the skew from the image
def rotate(
        image: np.ndarray, angle: float, background: Union[int, Tuple[int, int, int]]
) -> np.ndarray:
    old_width, old_height = image.shape[:2]
    angle_radian = math.radians(angle)
    width = abs(np.sin(angle_radian) * old_height) + \
        abs(np.cos(angle_radian) * old_width)
    height = abs(np.sin(angle_radian) * old_width) + \
        abs(np.cos(angle_radian) * old_height)

    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    rot_mat[1, 2] += (width - old_width) / 2
    rot_mat[0, 2] += (height - old_height) / 2
    return cv2.warpAffine(image, rot_mat, (int(round(height)), int(round(width))), borderValue=background)


#function  to get the starting parameter and ending paramter for part 3 
def getstartend(total_amount, text):
    
    lines = text.split("\n")

    #remove the empty lines
    non_empty_lines = [line for line in lines if line.strip() != ""] 
    string_without_empty_lines = ""
    for line in non_empty_lines:
          string_without_empty_lines += line + "\n"
    text=string_without_empty_lines #This conatins no empty lines

    total_amount=total_amount.strip()

    #regex to match the first word in the line where total amount occurs and the first of the next line of total amount. These are the start and the end parameters respectively
    start_end=re.search('\n.*?'+f"\s{total_amount}"+'.*?\n\w+', text)
    if(start_end!=None):
        start=start_end.group().split(" ")[0].strip()
        end=start_end.group().split("\n")[-1].strip()

    else:
        #If no regex matches
        print("start, end cannot be found")
    return "-1", "-1"

#function to get the desired fields when a template has been matched for the pdf
def getinf(item):

    #Cropping and saving the raectangle that contains the keyword
    img1 = Image.open("page0.jpg")
    img1 = img1.crop((item["keyword_cordinates"]["x1"]+shiftx, item["keyword_cordinates"]
                     ["y1"]+shifty, item["keyword_cordinates"]["x2"]+shiftw, item["keyword_cordinates"]["y2"]+shifth))
    image=cv2.imread('page0.jpg')
    img1.save('img2.png')
    img1.close()
    #reading text from the cropped image to get the keyword
    text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))


    #Cropping and saving the raectangle that contains the Date of Invoice
    img1 = Image.open("page0.jpg")
    img1 = img1.crop((item["Date"]["x1"]+shiftx, item["Date"]
                     ["y1"]+shifty, item["Date"]["x2"]+shiftw, item["Date"]["y2"]+shifth))
    img1.save('img2.png')
    img1.close()
    #reading text from the cropped image to get the Date of Invoice
    text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
    print("Date of Invoice: ", text)

    #reading the Invoice No after selecting the bounding box
    img1 = Image.open("page0.jpg")
    img1 = img1.crop((item["Invoice_No"]["x1"]+shiftx, item["Invoice_No"]
                     ["y1"]+shifty, item["Invoice_No"]["x2"]+shiftw, item["Invoice_No"]["y2"]+shifth))
    img1.save('img2.png')
    img1.close()
    text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
    print("invoice No ", text)

    #reading the Total bill after selecting the bounding box
    img1 = Image.open("page0.jpg")
    img1 = img1.crop((item["Total Bill"]["x1"]+shiftx, item["Total Bill"]
                     ["y1"]+shifty, item["Total Bill"]["x2"]+shiftw, item["Total Bill"]["y2"]+shifth))
    img1.save('img2.png')
    img1.close()
    text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
    print("Total Bill: ", text)


    #reading the Buyer Address after selecting the bounding box
    total_amount=text
    img1 = Image.open("page0.jpg")
    img1 = img1.crop((item["Buyer"]["x1"]+shiftx, item["Buyer"]
                     ["y1"]+shifty, item["Buyer"]["x2"]+shiftw,item["Buyer"]["y2"]+shifth))
    img1.save('img2.png')
    img1.close()
    text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
    print("Buyer: ", text)


    #reading the Seller Address  after selecting the bounding box
    img1 = Image.open("page0.jpg")
    img1 = img1.crop((item["Seller"]["x1"]+shiftx, item["Seller"]
                     ["y1"]+shifty, item["Seller"]["x2"]+shiftw, item["Seller"]["y2"]+shifth))
    img1.save('img2.png')
    img1.close()
    text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
    print("Seller: ", text)

    return total_amount


#Function for selecting the rectange by dragging the mouse
def shape_selection(event, x, y, flags, param):
    # grab references to the global variables

    global ref_point2, crop

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        # ref_point = [(x, y)]
        ref_point.append((x, y))
        # it+=1
        ref_point2 = [(x, y)]

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        if(curr == 1):
            ref_point.append((x, y))
            cv2.rectangle(image, ref_point[len(
                ref_point)-1], ref_point[len(ref_point)-2], (0, 255, 0), 2)
        elif(curr == 2):
            ref_point2.append((x, y))
            cv2.rectangle(image, ref_point2[0], ref_point2[1], (0, 255, 0), 2)
        # cv2.resizeWindow("image", 1000,1500)
        cv2.imshow("image", image)

#Connection to db
connection = pymongo.MongoClient('127.0.0.1:27017')
db = connection.invoiceocr


#Intializing Some variables for part3
ref_point = []
total_amount=""
crop = False
onboard=0
flag=0
shiftx=0
shifty=0
shiftw=0
shifth=0

print("Select boxes in the order:\n1.Keyword\n2.Date of Invoice\n3.Invoice No.\n4.Buyer Details\n5.Seller Details   ")

#Extracting the file from the arguments passed in the command line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--pdf", required=True, help="Path to the pdf")
args = vars(ap.parse_args())

#converting pdf into images for every page of the pdf
images = convert_from_path(args["pdf"])

#Extracting the image of each pages from the pdf
no_of_pages=len(images)
for i in range(len(images)):
    images[i].save('page' + str(i) + '.jpg', 'JPEG')


found = 0 #variable to check if a matching template is found
image = cv2.imread('page0.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
angle = determine_skew(grayscale)  # determine the skew angle prsent in the original image
rotated = rotate(image, angle, (0, 0, 0))  #cancelling the skew in the original image and rorated is the new image after cancelling the skew in the original image
cv2.imwrite('page0.jpg', rotated) 
matched_doc="" # to store the temaplate that has match with the template

#extarcting the text of the page1
text = str(pytesseract.image_to_string(
                Image.open(r"page0.jpg"), lang='eng'))

#check if a matching template exists with teh same keyword and keyword bounding boxes
for document in db.invoices.find():
    img1 = Image.open("page0.jpg")
    img3 = img1.crop((document["keyword_cordinates"]["x1"], document["keyword_cordinates"]
                     ["y1"], document["keyword_cordinates"]["x2"], document["keyword_cordinates"]["y2"]))
    img3.save('img3.png')
    img3.close()
    image = Image.open('img3.png')
    image.close()
    text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
    text=text.strip()
    foundregex=re.search(r'[a-zA-Z]+', text)
    if(foundregex!=None):
        text=foundregex.group()
    key=document["keyword"].strip()
    if(text== key):
        found = 1
        total_amount=getinf(document)
        matched_doc=document["keyword"].strip()
        if(no_of_pages!=document["no_of_pages"]):
            print("-1")
            flag=-1
            break
        
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # to make tesseract work, put in the exact path of tesseract

#matching every word of the pdf to every keyword to find the shift and confirming by matching with seller key
if(found==0 ):
    for document in db.invoices.find():
        img = Image.open('page0.jpg')
        data = pytesseract.image_to_data(img, output_type='dict') 
        boxes = len(data['level'])

        for i in range(boxes):
            
            if data['text'][i].strip()!= ''.strip():
                key_to_match=data['text'][i]
                foundregex=re.search(r'[a-zA-Z]+', key_to_match)

                #Checking only for valid strings
                if(foundregex!=None):
                    key_to_match=foundregex.group() 
                
                #If keyword matches with a word in the pdf, get the x, y shift of teh keyword coordinates stored
                if((key_to_match)==document["keyword"]):
                    shiftx=data["left"][i]-document["keyword_cordinates"]["x1"]
                    shifty=data["top"][i]-document["keyword_cordinates"]["y1"]
                    shiftw=data["left"][i]-document["keyword_cordinates"]["x1"]
                    shifth=data["top"][i]-document["keyword_cordinates"]["y1"]
                    img1 = Image.open("page0.jpg")
                    img1 = img1.crop((document["Seller"]["x1"]+shiftx, document["Seller"]
                                     ["y1"]+shifty, document["Seller"]["x2"]+shiftw, document["Seller"]["y2"]+shifth))
                    img1.save('img2.png')
                    img1.close()
                    text = str(pytesseract.image_to_string(Image.open(r"img2.png"), lang='eng'))

                    #Confirming if the seller key matches then only we consider this template otherwise we send it for onboarding
                    if( text.split("\n")[0].strip()==document["seller_key"].strip()):
                        found=1
                        break
        
        
        if(found==1):
            matched_doc=document["keyword"].strip()
            total_amount=getinf(document)
            if(no_of_pages!=document['no_of_pages']):
                print("-1")
                flag=-1 #flag indicates if nof pages in teh onboarded pdf and teh current pdf are same or not, if not sent for manual (-1)
                break
            
            break


#When no template has been matched 
if(found == 0 and flag!=-1):
    onboard=1
    print("Onboarding")
    image = cv2.imread("page0.jpg")
    clone = image.copy()

    cv2.namedWindow("image", cv2.WINDOW_NORMAL) #resizing the output window
    cv2.setMouseCallback("image", shape_selection) #to select rectangle by pressing and releasing mousebutton
    curr = 1
    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        #When c is prssed on the keyword the opencv window closes
        if key == ord("c"): 
            break

    #If valid selection is made by user while dragging the rectangle, i.e, atleast one rectangle has been selected successfully
    if len(ref_point) >= 2:
        img1 = Image.open("page0.jpg")
        #cropping and saving only the rectangle portion of the image frmo where we have to extract the text
        img3 = img1.crop(
            (ref_point[0][0], ref_point[0][1], ref_point[1][0], ref_point[1][1]))
        img3.save('img2.png')
        img3.close()

        image = Image.open('img2.png')
        image.close()

        #text variable contains the text in the bounding box selected
        text = str(pytesseract.image_to_string(
            Image.open(r"img2.png"), lang='eng'))

        #getting the x and y coordinates of the keyword  from the pdf, for this the text read from the bounding box is matxhed with edvery word 
        #of the pdf and when the word matches we store its x, y coordinates as the keyword's coordinates. This is done to ensure that we dont consider the extra region of the image that ahs not 
        # text , we want a tight bound to x y coordinates for keyword
        text=text.strip()
        foundregex=re.search(r'[a-zA-Z]+', text)
        if(foundregex!=None):
            text=foundregex.group()
        
        #onverting the whole pdf to text to match its every word
        myimg=Image.open('page0.jpg')
        data = pytesseract.image_to_data(myimg, output_type='dict')
        boxes = len(data['level'])
 
        for i in range(boxes):
            key_to_match=data['text'][i].strip()
            if(key_to_match!=""):
                foundregex=re.search(r'[a-zA-Z]+', key_to_match)
                if(foundregex!=None):
                    key_to_match=foundregex.group()
              
                if key_to_match.strip() == text.strip():
                    break

        #inserting the new template in the db
        db.invoices.insert_one({"keyword":text})
        keyword = text
        db.invoices.update_one({"keyword": keyword}, {"$set": {"no_of_pages": no_of_pages}})
        db.invoices.update_one({"keyword": keyword}, {
        "$set": {"keyword_cordinates": {"x1":data["left"][i], "y1":data["top"][i], "x2": data["left"][i]+data["width"][i], "y2":data["top"][i]+data["height"][i]}}})
       

        #extracting the date of invoice from the bounding box selected for it and storing its keyword coordinates in the database
        img3 = img1.crop(
        (ref_point[2][0], ref_point[2][1], ref_point[3][0], ref_point[3][1]))
        db.invoices.update_one({"keyword": keyword}, {
        "$set": {"Date": {"x1": ref_point[2][0], "y1": ref_point[2][1], "x2": ref_point[3][0], "y2": ref_point[3][1]}}})
        img3.save('img2.png')
        img3.close()
        image = Image.open('img2.png')
        image.close()
        text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
        text=text.strip()
        print("Date of Invoice: ", text)

        #extracting the Invoice No. from the bounding box selected for it and storing its keyword coordinates in the database
        img3 = img1.crop(
        (ref_point[4][0], ref_point[4][1], ref_point[5][0], ref_point[5][1]))
        db.invoices.update_one({"keyword": keyword}, {
        "$set": {"Invoice_No": {"x1": ref_point[4][0], "y1": ref_point[4][1], "x2": ref_point[5][0], "y2": ref_point[5][1]}}})
        img3.save('img2.png')
        img3.close()
        image = Image.open('img2.png')
        image.close()
        text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
        text=text.strip()
        print("Invoice No: ", text)

        #extracting the Total Bill from the bounding box selected for it and storing its keyword coordinates in the database
        img3 = img1.crop(
        (ref_point[6][0], ref_point[6][1], ref_point[7][0], ref_point[7][1]))
        db.invoices.update_one({"keyword": keyword}, {
        "$set": {"Total Bill": {"x1": ref_point[6][0], "y1": ref_point[6][1], "x2": ref_point[7][0], "y2": ref_point[7][1]}}})
        img3.save('img2.png')
        img3.close()
        image = Image.open('img2.png')
        image.close()
        text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
        text=text.strip()
        print("Total Bill ", text)
        total_amount=text

        #Stroring the word before and after the total bill for part 3
        wholetext = str(pytesseract.image_to_string(
            Image.open(r"page0.jpg"), lang='eng'))
        wholetext=wholetext.strip()
        match_start, match_end=getstartend(total_amount, wholetext)
        
        db.invoices.update_one({"keyword": keyword}, {
            "$set": {"match_start": match_start}})
        db.invoices.update_one({"keyword": keyword}, {
            "$set": {"match_end": match_end}})
    

        #extracting the Buyer Address from the bounding box selected for it and storing its keyword coordinates in the database
        img3 = img1.crop(
        (ref_point[8][0], ref_point[8][1], ref_point[9][0], ref_point[9][1]))
        db.invoices.update_one({"keyword": keyword}, {
        "$set": {"Buyer": {"x1": ref_point[8][0], "y1": ref_point[8][1], "x2": ref_point[9][0], "y2": ref_point[9][1]}}})
        img3.save('img2.png')
        img3.close()
        image = Image.open('img2.png')
        image.close()
        text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
        text=text.strip()
        print("Buyer: ", text)

        #extracting the Seller Address from the bounding box selected for it and storing its keyword coordinates in the database
        img3 = img1.crop(
        (ref_point[10][0], ref_point[10][1], ref_point[11][0], ref_point[11][1]))
        db.invoices.update_one({"keyword": keyword}, {
        "$set": {"Seller": {"x1": ref_point[10][0], "y1": ref_point[10][1], "x2": ref_point[11][0], "y2": ref_point[11][1]}}})
        img3.save('img2.png')
        img3.close()
        image = Image.open('img2.png')
        image.close()
        text = str(pytesseract.image_to_string(
        Image.open(r"img2.png"), lang='eng'))
        text=text.strip()
        sellerkey=text.split("\n")[0]
        db.invoices.update_one({"keyword": keyword},{"$set": {"seller_key": sellerkey}})
        print("Seller: ", text)

    cv2.destroyAllWindows()

