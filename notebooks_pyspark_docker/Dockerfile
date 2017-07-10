FROM anapsix/alpine-java:8
ENV spark_package spark-2.1.0-bin-hadoop2.7.tgz
ADD http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz /tmp/ 

RUN apk add --no-cache python freetype \ 
    && apk add --update --no-cache --virtual=deps python-dev freetype-dev make g++ gfortran musl-dev \ 
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \ 
    && apk add --no-cache --virtual=wget wget \ 
    && cd /tmp/ && wget https://bootstrap.pypa.io/get-pip.py \ 
    && python get-pip.py \ 
    && pip install numpy matplotlib pandas BeautifulSoup ipython jupyter \ 
    && cd /opt/ && tar xzvf /tmp/${spark_package} \ 
    && rm -rf /var/cache/apk/* /tmp/* /root/src/ /root/.cache/pip/* \ 
    && apk del wget deps \ 
    && mkdir /notebook \ 
    && echo "PYSPARK_DRIVER_PYTHON=\"jupyter\" PYSPARK_DRIVER_PYTHON_OPTS=\"notebook --port 8888 --ip='0.0.0.0' --notebook-dir=/notebook --no-browser\" /opt/spark-2.1.0-bin-hadoop2.7/bin/pyspark" > /opt/start_notebook.sh

EXPOSE 8888

ENTRYPOINT ["/bin/bash","/opt/start_notebook.sh"]
