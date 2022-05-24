# Pruebas lint

pip3 install pylint

cd proyecto2soa

# Para start_service
pylint start_service/src/app.py start_service/src/queue_connection.py

# Para image_analyzer_service
pylint image_analyzer_service/src/app.py image_analyzer_service/src/analyzer.py image_analyzer_service/src/emotion_detection.py image_analyzer_service/src/queue_connection.py

# Para save_service
pylint save_service/src/app.py
pylint save_service/src/write_file.py

