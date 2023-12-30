from PIL import Image


def resize_image(size1, size2):
    image = Image.open("")

    print(f"current size: {image.size}")

    resizedImage = image.resize((size1, size2))

    resizedImage.save("Resized image" + size1 + ".jpg")


size1 = int(input("Enter the width of the image: "))
size2 = int(input("Enter length of the image: "))

resize_image(size1, size2)