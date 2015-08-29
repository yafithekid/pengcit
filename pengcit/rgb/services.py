from heapq import heappush, heappop
import operator
from PIL import Image


class RGBCounter:
    def __init__(self):
        self.image = None
        self.width = 0
        self.height = 0

    def set_image_from_path(self, image_path: str):
        self.image = Image.open(image_path)
        (self.width, self.height) = self.image.size

    def count_rgb(self):
        result = {}
        pix = self.image.load()

        for x in range(self.width):
            for y in range(self.height):
                if not pix[x, y] in result:
                    result[pix[x, y]] = 0
                result[pix[x, y]] += 1
        return len(result)

    def get_most_frequent_rgb(self):
        result = {}
        h = []
        pix = self.image.load()

        for x in range(self.width):
            for y in range(self.height):
                if not pix[x, y] in result:
                    result[pix[x, y]] = 0
                result[pix[x, y]] += 1
        for key in result.keys():
            heappush(h, (-result[key], key))
        result = []
        for i in range(10):
            if len(h) == 0:
                break
            (c, key) = heappop(h)
            (r, g, b) = key
            result.append((r, g, b, -c))
        return result
