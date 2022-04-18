FROM ubuntu:bionic



RUN apt-get update && apt-get install -y curl
RUN apt-get update && apt-get install -y nginx
RUN apt-get update && apt-get install -y vim
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN apt-get update && apt-get install -y gcc
RUN apt-get update && apt install -y net-tools
RUN rm -rf /tmp/mem1.c
COPY mem1.c /tmp/mem1.c
RUN cd  /tmp && gcc mem1.c
#CMD service nginx start
CMD /tmp/a.out
