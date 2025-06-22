FROM python:3.11

# Set working directory
WORKDIR /app

RUN apt-get update

# Create venv
ENV VIRTUAL_ENV=/opt/venv
RUN python3.11 -m venv ${VIRTUAL_ENV}
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy in requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Expose port
EXPOSE 5002

# entrypoint
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]