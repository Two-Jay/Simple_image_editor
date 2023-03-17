from PIL import Image


class ImageLoader():
    def __init__(self):
        self.image = None

    def __enter__(self):
        self.image = Image.open("src/assets/images/PyQt6.png")
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.image:
            self.image.close()

class ImageManager():
    def __init__(self):
        self.image = None

    def load_image(self):
        with ImageLoader() as loader:
            self.image = loader.image
            self.image.show()