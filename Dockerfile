FROM python:3.6
RUN mkdir src
ADD src/* src/
ADD cmd_calculate_overflow.py .
ENTRYPOINT ["python", "cmd_calculate_overflow.py"]