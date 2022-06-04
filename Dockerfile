FROM python

COPY . /

WORKDIR /
RUN pip3 install boto3 
RUN pip3 install pandas
RUN pip3 install fsspec s3fs
RUN chmod 777 fileconversion.py
RUN sudo usermod -aG docker $(whoami)
RUN chown docker:docker -R fileconversion.py
ENTRYPOINT ["python3", "fileconversion.py"]
