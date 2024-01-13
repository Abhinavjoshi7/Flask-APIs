# The image works as a blueprint 
# To create the image use the command docker build -t "name of app" .
# To run the image use docker run "image name"

FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]