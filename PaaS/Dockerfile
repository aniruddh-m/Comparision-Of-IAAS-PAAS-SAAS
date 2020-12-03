FROM ubuntu
RUN apt-get update
RUN apt-get install -y stress-ng
RUN apt-get install sysbench
COPY entrypoint_test.sh /
ENTRYPOINT ["/entrypoint_test.sh"]
CMD ["6000"]
