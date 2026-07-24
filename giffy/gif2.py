from PIL import Image

frames = []

for i in range(37):
    frames.append(Image.open(f"frame_{i:02d}_delay-0.1s.png"))

frames[0].save(
    "dancingcroc.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0,
    disposal=2
)
print("Gif created successfully ! Check dancingcroc.gif")

#check if the dimensions are equal of frames
# import numpy as np
# img1 = iio.imread("frame_00_delay-0.1s.png")
# img2 = iio.imread("frame_01_delay-0.1s.png")
# print(np.array_equal(img1, img2))