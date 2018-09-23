from PIL import Image
import pytesseract
import pickle

# Run OCR - Tesseract
def run_tesseract(PATH, PICTURE_PATH, COORDINATES, THRESHOLD_VALUE):
    # Open image
    img = Image.open(PICTURE_PATH)

    # Crop image
    cropped = img.crop(COORDINATES)

    # Apply threshold
    fn = lambda x : 255 if x > THRESHOLD_VALUE else 0
    final_image = cropped.convert('L').point(fn, mode='1')

    final_image.save(PATH + '/server/static/data/images/result.png')

    # Return OCR'd value as an integer
    return int(pytesseract.image_to_string(final_image, lang='analog', config='-psm 10 nobatch digits'))
