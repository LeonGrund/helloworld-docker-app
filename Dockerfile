FROM python

COPY test.py /run

CMD [ "python", "/run/test.py" ]
