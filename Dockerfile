FROM python:3.6.9

# Bundle app source
COPY . /

# Install app dependencies
RUN cp -f requirements.txt /src/ut_anagramma/requirements.txt && \
    cd src/ut_anagramma && \
    ls -a && \
    pip install -r requirements.txt

# Define app directory
WORKDIR /src/ut_anagramma

EXPOSE 8082
ENTRYPOINT ["python"]
CMD ["./main.py"]
