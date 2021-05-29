.PHONY: start

start: 
	docker build -t app:latest .
	docker run -p 8501:8501 app:latest