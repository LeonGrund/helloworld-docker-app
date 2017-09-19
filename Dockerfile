FROM elyase/staticpython

COPY test.py /run

CMD [ "python", "run/test.py" ]
