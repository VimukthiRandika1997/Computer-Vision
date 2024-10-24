import imgaug.augmenters as iaa
import argparse
import cv2
import glob
import matplotlib.pyplot as plt
import itertools
import datetime


def load_images(path):
    exts = ['.jpg', '.png'] # image file formats
    img_paths = [glob.glob(f'{path}/*{e}') for e in exts] # 2D array is returned
    img_paths = list(itertools.chain.from_iterable(img_paths)) # flattening to 1D array
    print(img_paths)
    images = []
    for img_path in img_paths:
        img = cv2.imread(img_path)
        images.append(img)
    return images


def show_image(imgs):
    for img in imgs:
        h, w = img.shape[:2]
        resized_img = cv2.resize(
            img, (3 * w, 3 * h), interpolation=cv2.INTER_CUBIC)
        fig = plt.gcf()
        fig.set_size_inches(18, 10)
        plt.axis('off')
        plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
        plt.show()
        # cv2.imshow("Image", img)
        # cv2.waitKey(0)


def save_imgs(imgs):
    # get the current date and time
    now = datetime.datetime.now()
    i = 1
    for img in imgs:
        cv2.imwrite(f'../data/processed/label{i}_{now}.jpg', img)
        i += 1
    print('All images are saved!')


def rotate_img(imgs):
    seq = iaa.Sequential([
        iaa.Rotate((-15, 30))
    ], seed=42)
    return seq(images=imgs)

def main(path):
    imgs = load_images(path)
    imgs = rotate_img(imgs)
    save_imgs(imgs)
    show_image(imgs)


# Apply the augmentation
for batch_idx in range(2):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    args = parser.parse_args()

    # show_image(args.img_path)
    # load_image(args.img_path)
    main(args.path)
