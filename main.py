import sys
import logging
from datetime import datetime, timedelta
from modules import GoogleSheets, Calculator, Neo4jHandler, ImageGenerator, ImageSearch

logging.basicConfig(level=logging.INFO)

def run_pipeline(start_date: str, end_date: str):
    sheets = GoogleSheets()
    data = sheets.fetch_data(start_date, end_date)

    calc = Calculator()
    result_value = calc.process(data)

    neo4j = Neo4jHandler()
    neo4j.record_result(result_value)

    image_path = ImageGenerator.generate_image(result_value)

    similar_images = ImageSearch.find_similar(image_path)
    logging.info(f"Похожие изображения: {similar_images}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python main.py <start_date> <end_date>")
        sys.exit(1)
    start, end = sys.argv[1], sys.argv[2]
    run_pipeline(start, end)
