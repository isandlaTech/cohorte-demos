FROM cohorte/cohorte-runtime:1.1.2

MAINTAINER Bassem Debbabi <bassem.debbabi@isandlatech.com>

ENV MODIFICATION_DATE=20160525_1613
ENV COHORTE_BASE=/opt/led-gateway

COPY ./demoled/led-gateway.service ./etc/systemd/system/led-gateway.service
COPY ./demoled/led-gateway ./opt/led-gateway

RUN systemctl enable led-gateway.service
RUN ls -l ./opt

WORKDIR ./opt/led-gateway

EXPOSE 40000 80 9001

VOLUME [ "/opt/led-gateway"]

CMD ["/usr/sbin/init"]
