# Prerequisite
~~~bash
pip install -r requirements.txt
~~~


# How to build for standalone exe
~~~bash
pyinstaller --onefile main.py
~~~


# How to run unit tests
~~~bash
# output on terminal
python -m pytest 
# output as junit formar
python -m pytest --junitxml=./test.xml
~~~

# Jenkins CI/CD
https://jenkins.marius.best


# how to build the docker image
~~~bash
cd docker/unittest
docker build -t unittest -f unittest.Dockerfile .
~~~

## run unit tests
run from root folder
~~~bash
docker run -v ${PWD}:/data unittest
~~~