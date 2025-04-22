from fimage import FImage, Saturation, Contrast, Brightness, Sepia
from fimage.presets import SinCity, Love, OrangePeel

#example image
image = FImage('img.jpg')

def apply_filter():
    while True:
        which_filter = input("'Sincity' filter ->    1 \n"
                             "'Mixed' filter ->      2\n"
                             "'Sepia' filter ->      3\n"
                             "'Love' filter ->       4\n"
                             "'OrangePeel' filter -> 5\n"
                             "enter: ")
        if which_filter == "1":
            image.apply(SinCity())
            break
        elif which_filter == "2":
            image.apply(Saturation(20), Contrast(25), Brightness(15))
            break
        elif which_filter == "3":
            image.apply(Sepia(90))
            break
        elif which_filter == "4":
            image.apply(Love())
            break
        elif which_filter == "5":
            image.apply(OrangePeel())
            break

        else:
            print("please enter (1,5)")
    image.save('filter_img.jpg')

if __name__ == "__main__":
    apply_filter()

