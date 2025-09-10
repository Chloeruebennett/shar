import imagehash
from PIL import Image
import os
import glob

class ImageSearch:
    @staticmethod
    def find_similar(image_path, threshold=5):
        database_path = 'image_db/'
        target_hash = imagehash.average_hash(Image.open(image_path))
        results = []

        for img_file in glob.glob(os.path.join(database_path, '*.png')):
            img = Image.open(img_file)
            hash_ = imagehash.average_hash(img)
            diff = target_hash - hash_
            if diff <= threshold:
                results.append(img_file)
        return results
