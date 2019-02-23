FROM python:3.6

ENV BASEDIR /App
ENV MASTER_ROOT $BASEDIR/apicrawler
ENV PATH "$BASEDIR:$PATH"

ADD ./apicrawler /App/apicrawler
ADD ./apicrawler_slave /App/apicrawler_slave
ADD ./requirements.txt /App
ADD ./__init__.py /App
ADD ./start_master.sh $BASEDIR/

# For windows file format
RUN chmod +x $BASEDIR/start_master.sh
RUN sed -i -e 's/\r$//' $BASEDIR/start_master.sh

#WORKDIR /App/apicrawler
WORKDIR $BASEDIR

# 安装支持

RUN pip install -r ./requirements.txt