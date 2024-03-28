FROM nginx:1.19.5

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./run.sh /run.sh

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    chmod +x /run.sh

VOLUME /vol/static

CMD ["/run.sh"]
