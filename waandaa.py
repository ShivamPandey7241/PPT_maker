from wand.image import Image

img = input("Image name\t")
logo = input("logo name\t")
naam = input("file name\t")

with Image(filename= img) as image:
    with Image(filename= logo) as water:
        water.resize(1700, 600)
        with image.clone() as watermark:
            watermark.watermark(water, 0.1, 10, 20)
            watermark.save(filename= naam)
            