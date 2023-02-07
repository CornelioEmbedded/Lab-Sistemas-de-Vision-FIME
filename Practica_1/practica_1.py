import cv2

PHOTO_1 = r"Practica_1\foto_prueba.png"

def adq_preprocess_photo(path, type):
    type_dict = {'gray': cv2.IMREAD_REDUCED_GRAYSCALE_2,
            'color': cv2.IMREAD_REDUCED_COLOR_2,
            'unchanged': cv2.IMREAD_IGNORE_ORIENTATION}
    
    img = cv2.imread(path, type_dict[type])
    try:
        cv2.imshow("image", img)
        cv2.waitKey(0)
    except:
        pass
    cv2.destroyAllWindows()

adq_preprocess_photo(PHOTO_1, 'color')