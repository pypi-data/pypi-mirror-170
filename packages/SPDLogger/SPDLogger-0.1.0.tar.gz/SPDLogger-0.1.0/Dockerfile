FROM python:3.7

COPY ./ /srv
RUN pip install twine
# RUN cd /srv && python setup.py install
# RUN cd /usr/local/lib/python3.7/site-packages/ && unzip SPDLogger-0.1.0-py3.7.egg
RUN cd /srv && python setup.py sdist && twine upload --repository-url https://pypiserver.qa.di.in.spdigital.sg:4443 -u username -p password dist/*
RUN pip install jupyter
