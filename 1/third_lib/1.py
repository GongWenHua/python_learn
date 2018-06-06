from PIL import Image

im = Image.open('moonRising.png')
w, h = im.size
print('image size: %s x %s' % (w, h))
# 缩放
im.thumbnail((w // 2, h // 2))
print('thumbnail image to: %s x %s' % (w // 2, h // 2))
im.save('moonRising_thumb.jpg', 'jpeg')
