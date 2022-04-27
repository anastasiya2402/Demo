FROM ubuntu
MAINTAINER Anastasia

#USER root

# set noninteractive installation
RUN export DEBIAN_FRONTEND=noninteractive

# install tzdata package
RUN apt-get update && apt-get install -y tzdata

# install packages for scipy
RUN apt-get update --fix-missing && apt-get install -y libatlas-base-dev gfortran

# set your timezone
RUN ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata

# Essential tools and xvfb
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    unzip \
    curl \
    xvfb \
    wget \
    nano \
    allure \
    openjdk-8-jdk \
    ffmpeg \
    xclip \
    libaio1
# Fix Java certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# install numpy for python
RUN apt-get update && apt-get install python-numpy -y

# Setup JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# MySQL connector for python
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    default-libmysqlclient-dev

# Install Oracle DB client
RUN mkdir /opt/oracle && cd /opt/oracle \
    && wget https://download.oracle.com/otn_software/linux/instantclient/215000/instantclient-basic-linux.x64-21.5.0.0.0dbru.zip \
    && unzip instantclient-basic-linux.x64-21.5.0.0.0dbru.zip \
    && rm -f instantclient-basic-linux.x64-21.5.0.0.0dbru.zip \
    && cd /opt/oracle/instantclient* \
    && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
    && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig

# Install Oracle SQLPlus client
RUN cd /opt/oracle \
    && wget https://download.oracle.com/otn_software/linux/instantclient/215000/instantclient-sqlplus-linux.x64-21.5.0.0.0dbru.zip \
    && unzip instantclient-sqlplus-linux.x64-21.5.0.0.0dbru.zip \
    && rm -f instantclient-sqlplus-linux.x64-21.5.0.0.0dbru.zip \
    && cd /opt/oracle/instantclient* \
    && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
    && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig \
    && cd /

# Add Oracle Client and Tools to the PATH
ENV PATH="/opt/oracle/instantclient_21_5:${PATH}"
ENV ORACLE_HOME="/opt/oracle/instantclient_21_5"

# Install google api
RUN pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


# Chrome browser to run the tests
RUN echo 'Create directory for browsers' \
    && mkdir -p /usr/share/desktop-directories \
    && echo 'Get the latest stable Chrome' \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb

# Disable the SUID sandbox so that chrome can launch without being in a privileged container
RUN dpkg-divert --add --rename --divert /opt/google/chrome/google-chrome.real /opt/google/chrome/google-chrome \
    && echo "#!/bin/bash\nexec /opt/google/chrome/google-chrome.real --no-sandbox --disable-setuid-sandbox \"\$@\"" > /opt/google/chrome/google-chrome \
    && chmod 755 /opt/google/chrome/google-chrome

# Chrome Driver
#ENV PANTHER_NO_SANDBOX 1
#ENV PANTHER_CHROME_ARGUMENTS='--headless --no-sandbox --disable-infobars --disable-dev-shm-usage --disable-gpu --disable-extensions --remote-debugging-port=9222'e
RUN echo 'Pull appropriate chromedriver' \
    && CHROME_DRIVER_VERSION=`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE` \
	&& mkdir -p /opt/selenium \
    && curl https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -o /opt/selenium/chromedriver_linux64.zip \
    && cd /opt/selenium; unzip /opt/selenium/chromedriver_linux64.zip; rm -rf chromedriver_linux64.zip; ln -fs /opt/selenium/chromedriver /usr/local/bin/chromedriver;


# set a virtual display
ENV DISPLAY :20

# install odbc
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN apt-get install -y unixodbc-dev


RUN mkdir myUT
# Set working directory
WORKDIR /myUT
# install Project dependancies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# add QA frame as an entry point
COPY . ./
RUN mkdir junit_reports

# Provide read, write and execute permissions for entrypoint.sh and also take care of '\r' error which raised when someone uses notepad or note++ for editing in Windows.
RUN chmod 755 /myUT/entrypoint.sh \
    && sed -i 's/\r$//' /myUT/entrypoint.sh

#Expose port 5920 to view display using VNC Viewer
EXPOSE 5920

#Expose port 5000 for Flask callback server
EXPOSE 5000

#USER 1200
#Execute entrypoint.sh at start of container
ENTRYPOINT ["/myUT/entrypoint.sh"]

