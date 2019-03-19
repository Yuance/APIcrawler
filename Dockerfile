FROM python:3.6

ENV BASEDIR /App
ENV MASTER_ROOT $BASEDIR/apicrawler
ENV PATH "$BASEDIR:$PATH"

ADD ./apicrawler /App/apicrawler
ADD ./apicrawler_slave /App/apicrawler_slave1
ADD ./apicrawler_slave /App/apicrawler_slave2
ADD ./settings.py /App/apicrawler/apicrawler
ADD ./settings.py /App/apicrawler_slave1/apicrawler
ADD ./settings.py /App/apicrawler_slave2/apicrawler
ADD ./requirements.txt /App
ADD ./__init__.py /App
ADD ./start_master.sh $BASEDIR/
ADD ./start_slave1.sh $BASEDIR/
ADD ./start_slave2.sh $BASEDIR/

# For windows file format, get master and slave1, slave2 on
# TODO: set up mongodb sharding. Assign to each slave, on each machine
RUN chmod +x $BASEDIR/start_master.sh
RUN sed -i -e 's/\r$//' $BASEDIR/start_master.sh

RUN chmod +x $BASEDIR/start_slave1.sh
RUN sed -i -e 's/\r$//' $BASEDIR/start_slave1.sh

RUN chmod +x $BASEDIR/start_slave2.sh
RUN sed -i -e 's/\r$//' $BASEDIR/start_slave2.sh

#WORKDIR /App/apicrawler
WORKDIR $BASEDIR

# 安装支持

RUN pip install -r ./requirements.txt