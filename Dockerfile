
FROM debian:11

RUN apt-get update
RUN apt-get -y install python3 python3-pip libglib2.0-0 libgl1 libqt5gui5 libglu1-mesa

RUN pip3 install PyQt5 ezdxf PyOpenGL Pillow pygame pyclipper setproctitle freetype-py matplotlib svgwrite

CMD ["/bin/bash"]

