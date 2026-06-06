FROM python:3.12
  
WORKDIR <directory path where the app code is stored

WORKDIR /Users/sachi/Desktop/Calculator-Azure-Web-App-main
  
RUN mkdir -p testapp
  
RUN pip install flask
  
RUN pip install MSAL
  
COPY . /testapp
  
CMD [ "python", "/testapp/app.py" ]
