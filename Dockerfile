FROM python:3.6
#ARG APIKEY
ENV BASEDIR /App
ENV MASTER_ROOT $BASEDIR/apicrawler
ENV PATH "$BASEDIR:$PATH"

ADD ./apicrawler $MASTER_ROOT
ADD ./scripts $MASTER_ROOT/scripts
ADD ./requirements.txt /App
ADD ./__init__.py /App
ADD ./start_master.sh $BASEDIR/
ADD ./start_slave1.sh $BASEDIR/

# For windows file format, get master and slave1, slave2 on
RUN chmod +x $BASEDIR/start_master.sh
RUN sed -i -e 's/\r$//' $BASEDIR/start_master.sh

RUN chmod +x $BASEDIR/start_slave1.sh
RUN sed -i -e 's/\r$//' $BASEDIR/start_slave1.sh

#WORKDIR /App/apicrawler
WORKDIR $BASEDIR

# install python library dependencies
RUN pip install -r ./requirements.txt