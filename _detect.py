import cv2
import numpy as np

cap = cv2.VideoCapture(0)

book1 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book1.jpg")
book2 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book2.jpg")
book3 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book3.jpg")
book4 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book4.jpg")
book5 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book5.jpg")
book6 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book6.jpg")
book7 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book7.jpg")
book8 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book8.jpg")
book9 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book9.jpg")
book10 = cv2.imread("E:\\AI files\\C4T_main_module\\sift_homework\\book10.jpg")

books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]

gray_books = []
kp1 = []
des1 = []
for book in books:
    gray_book = cv2.cvtColor(book, cv2.COLOR_RGB2GRAY)
    gray_books.append(gray_book)
    sift1 = cv2.xfeatures2d.SIFT_create()
    k1, d1 = sift1.detectAndCompute(gray_book, None)
    kp1.append(k1)
    des1.append(d1)

while True:

    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    sift2 = cv2.xfeatures2d.SIFT_create()
    kp2, des2 = sift2.detectAndCompute(gray_frame, None)

    if len(kp2) > 10:

        M_list = []
        M_list_all = []
        true_good = []

        width = book1.shape[1] + frame.shape[1]
        height = book1.shape[0] + frame.shape[0]
        oI = np.zeros((width, height, 3), dtype=np.uint8)

        for index in range(len(books)):
            BF = cv2.BFMatcher_create()
            matches = BF.knnMatch(des1[index], des2, k=2)

            good = []
            new_good = []

            for m, n in matches:
                if m.distance < 0.4 * n.distance:
                    good.append([m])
                    new_good.append(m)

            if len(new_good) > 4:
                true_good.append(good)
                src_ds = np.float32([kp1[index][m.queryIdx].pt for m in new_good]).reshape(-1, 1, 2)
                dst_ds = np.float32([kp2[m.trainIdx].pt for m in new_good]).reshape(-1, 1, 2)

                M, H = cv2.findHomography(src_ds, dst_ds, cv2.RANSAC, 5.0)

                h, w = gray_frame.shape
                point_corner = np.float32([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]]).reshape(-1, 1, 2)

                if M is None:
                    M_list_all.append([])
                else:
                    M_list_all.append(len(new_good))
                    M_list.append(len(new_good))
                    pts = cv2.perspectiveTransform(point_corner, M)
                    cv2.polylines(frame, np.int32([pts]), True, (0, 255, 0), 3)
            else:
                true_good.append([])
                M_list_all.append([])

        number = 0
        if M_list:
            for num in range(len(M_list_all)):
                if M_list_all[num] == max(M_list):
                    number = num
                    break

        outImg = cv2.drawMatchesKnn(books[number], kp1[number], frame, kp2, true_good[number], oI)

        cv2.imshow("outImg", outImg)

    k = cv2.waitKey(30)

    if k == 27:
        cap.release()
        break
