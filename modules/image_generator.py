import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

class ImageGenerator:
    @staticmethod
    def generate_image(value):
        # Создаем изображение с уникальным паттерном на основе числа
        size = (256, 256)
        img = Image.new("RGB", size, color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        # Генерация паттерна
        for i in range(0, size[0], 20):
            color_value = int((value * i) % 255)
            draw.line([(i, 0), (i, size[1])], fill=(color_value, 100, 150), width=2)

        filename = f"generated_{int(value*1000)}.png"
        img.save(filename)
        print(f"Изображение сохранено: {filename}")
        return filename
