from PIL import ImageFilter, ImageDraw, ImageFont, Image

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_sharpen_filter(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        return self.image

    def add_border(self, border_size, color='black'):
        width, height = self.image.size
        new_size = (width + 2 * border_size, height + 2 * border_size)
        new_image = Image.new("RGB", new_size, color)
        new_image.paste(self.image, (border_size, border_size))
        self.image = new_image
        return self.image

    def add_text(self, text, position, font=None, font_size=20, color='white'):
        draw = ImageDraw.Draw(self.image)
        if font is None:
            font = ImageFont.truetype("arial.ttf", font_size)
        draw.text(position, text, fill=color, font=font)
        return self.image