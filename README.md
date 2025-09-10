Автоматизированная система обработки данных с использованием Python, интеграции с Google Sheets, Neo4j, а также генерации и поиска изображений. Он предназначен для работы по расписанию с помощью Apache Airflow, что обеспечивает регулярное выполнение ETL-процесса и аналитики.

main.py — основной скрипт запуска, объединяющий модули обработки данных, генерации изображений и их поиска.

modules/ — папка с модулями, реализующими ключевую логику:

google_sheets.py — подключение и извлечение данных из Google Sheets.

calculator.py — обработка данных (вычисления, трансформации).

neo4j_handler.py — взаимодействие с базой данных Neo4j.

image_generator.py — создание изображений на основе результата.

image_search.py — поиск похожих изображений в локальной базе.

airflow_dag.py — DAG для автоматизации запуска через Apache Airflow.

Документация:

Python 3.8 - https://docs.python.org/3/whatsnew/3.8.html

gspread - https://docs.gspread.org/en/latest/

oauth2client - https://oauth2client.readthedocs.io/en/latest/

pandas - https://pandas.pydata.org/pandas-docs/stable/

numpy - https://numpy.org/doc/

Pillow - https://pillow.readthedocs.io/en/stable/

Imagehash - https://pypi.org/project/ImageHash/

Neo4j - https://neo4j.com/docs/

Apache Airflow - https://airflow.apache.org/docs/

Запуск основного скрипта вручную:

python main.py <start_date> <end_date>

Убедитесь, что Airflow запущен:

airflow scheduler

airflow webserver -p 8080

