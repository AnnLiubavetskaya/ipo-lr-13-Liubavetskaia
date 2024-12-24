from PIL import Image

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.image_path)
        return self.image

    def save_image(self, save_path):
        self.image.save(save_path)

    def resize_image(self, size):
        self.image = self.image.resize(size)
        return self.image

    def change_format_to_jpg(self, save_path):
        self.image.save(save_path, format='JPEG')

    def rotate_image_45(self):
        self.image = self.image.rotate(45)
        return self.image

    def get_image(self):
        return self.image