FROM python:3

WORKDIR /tasks

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
RUN pip install --upgrade pip
COPY requirements.txt /tasks/requirements.txt
RUN pip install -r requirements.txt
COPY . /tasks
RUN pip install -e .


# Now copy in our code, and run it
#COPY . /app
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]