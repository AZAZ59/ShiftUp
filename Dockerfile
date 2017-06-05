# Instructions copied from - https://hub.docker.com/r/continuumio/anaconda/
FROM continuumio/anaconda3

# tell the port number the container should expose
EXPOSE 5000

#ADD ./run.py /opt/ShiftUp/run.py
#ADD ./Collector /opt/ShiftUp/Collector
#ADD ./Database /opt/ShiftUp/Database

ADD ./ /opt/ShiftUp

WORKDIR /opt/ShiftUp


RUN pip install vk
RUN pip install flask_profiler
RUN pip install SQLAlchemy-Paginator
# run the command
CMD ["python", "./app.py"]
