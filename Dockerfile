FROM python:3.7

# root directory for our project in the container
RUN mkdir /product-catalog

# working directory
WORKDIR /product-catalog

# copy requirements.txt file
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

# copy the current directory contents into the container
ADD . /product-catalog/

# run `./runserver.sh` command
CMD ["./runserver.sh"]