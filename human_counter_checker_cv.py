# -*- coding: utf-8 -*-
import apple_keras as apple
import numpy as np
import cv2
from keras.preprocessing.image import load_img, img_to_array

cam = cv2.VideoCapture(0)
image_size = 32
categories = ["赤りんご", "青りんご"]

def main():

    while(True):
        ret, frame = cam.read()
        cv2.imshow("Show FLAME Image", frame)

        k = cv2.waitKey(1)
        if k == ord('s'):
            cv2.imwrite("output.png", frame)
            cv2.imread("output.png")

            X = []
            img = load_img("./output.png", target_size=(image_size,image_size))
            in_data = img_to_array(img)
            X.append(in_data)
            X = np.array(X)
            X  = X.astype("float")  / 256

            model = apple.build_model(X.shape[1:])
            model.load_weights("./image/apple-model.h5")

            pre = model.predict(X)
            print(pre)
            if pre[0][0] > 0.9:
                print(categories[0])
                text = 'これは' + categories[0]+ 'だよ'
                print(text)
            elif pre[0][1] > 0.9:
                print(categories[1])
                text = 'これは' + categories[1]+ 'だよ'
                print(text)

        elif k == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()