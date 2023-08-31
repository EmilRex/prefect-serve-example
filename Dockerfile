FROM prefecthq/prefect:2-latest

# Install from main until 2.12.0 is released
RUN pip install git+https://github.com/prefecthq/prefect.git@main

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY app.py /opt/prefect/app.py
COPY flows/ /opt/prefect/flows

CMD ["python", "/opt/prefect/app.py"]
