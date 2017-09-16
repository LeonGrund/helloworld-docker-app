FROM elyase/staticpython

COPY test.py /run
# requirements.txt /run/

# pip install --requirement /run/requirements.txt

EXPOSE 80:8080

CMD [ "python", "run/test.py" ]
