FROM python:3.8

ENV GROUPO_NUMERO 46

COPY docker.py .

RUN python3 docker.py 

EXPOSE 9080

CMD ["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"]
