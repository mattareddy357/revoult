## About the application:
Simple 'Hello world' application that will work with HTTP based APIs to store user name and date of birth into the database also getting the responce based on the user birth date.

## Database used and implementation details:
- Used default database which comes with python flask i.e sqlite3.
- Implemented by using simple flask app and created HTTP end points to store use details and getting the results back from database.

## Routing/endpoints information:
- /home - home page of the application
- /addrec - add record page to POST the user details and storing into database
- /<username> - To get the results back from database.

## How to run the application:
- pip install -r requirements.txt
- After installing requirements, run 'python db.py'
- run 'python app.py' and take default port url, paste in web browser

## Sample Tests:
Test_1:
- Input: Username: Test_uesr1, DOB:1993-07-18(Formate must be YYYY-MM-DD) 
- Output: {
  "message": "Hello, Test_uesr1! your birthday is in 112 day(s)"
  }

Test_2:
- Input: Username: Test_uesr2, DOB:2021-12-18(Formate must be YYYY-MM-DD)
- Output:{
  "message": "Date of birth must be before the today date."
}

Test_3:
- Input: Username: Test_uesr3, DOB:1995-11-07(Formate must be YYYY-MM-DD)
- Output:{
  "message": "Hello, Test_uesr3! Happy birthday!"


## Dockerisation
- run Dockerfile  with 'docker build -t <sample-app> .'
- docker login to your registry 'docker login'
- do the tag for docker image with 'docker tag <sample-app> <name>'
- docker push to store in docker registry 'docker push <name>'


## Produce system diagram to above solution
- Please find the diagram in Flow-diagram.jpg 


## Configuration scripts are added for EKS deployment 
- HPA will help to available pods with more traffic
- added required deployment scripts which helps to deploy app into cloud env with ci/cd pipeline like jenkins or azure devops.
