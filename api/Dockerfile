# Define Python version
FROM python:3

# Define timezone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

# Install system dependencies
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y

# define the directory on container
WORKDIR /app

# copy pipenv files from local project to container
COPY Pipfile Pipfile.lock ./

# Install Python dependencies
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --deploy --system --dev

# copy the directory
COPY /src ./
#COPY /db ./db


ENTRYPOINT ["python", "app.py"]