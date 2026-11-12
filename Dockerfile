FROM rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.13.0
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --no-deps -r /app/requirements.txt && \
    python3 -c "import torch; print(torch.__version__)" && \
    mkdir -p /app/output /app/input /models
COPY . /app
RUN chmod +x /app/app.py
CMD ["tail", "-f", "/dev/null"]
