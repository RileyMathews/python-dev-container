FROM python:3.7

RUN pip install --upgrade pip

RUN pip install black

WORKDIR /workspace
COPY requirements.txt* /workspace/

RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt && rm requirements.txt*; fi
