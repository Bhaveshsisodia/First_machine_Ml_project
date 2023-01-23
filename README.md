# First_machine_Ml_project

Requirements
1. [Github Account](http://github.com) :
2. [Heroku Account](http://dashboard.heroku.com/login) :
3. [Vs code IDE](http://code.visualstudio.com/download) :
4. [Git CLI](http://git-scm.com/downloads)
```
git commands
```
```
git clone _____________ #fill github link in code section
cd __________ # fill repository name
code . # it will open default ide in your local system
git add . ## adding to github
git commit -m "added software and account requirement"  
git push origin main ## connecting local system to github 
```


creating conda environment

```
conda create -p venv python==3.7 -y
```
```
-p # virtual environment directory in project folder
```
activate  environment
```
conda activate mlproject/ 
```
install requirements.txt
```
pip install -r requirements.txt
```
it will add file to github  according to version control system

```
git add filename 
```
it will add all file to github
```
git add . 
```
gitignore will remove some files which you don't want  we have to mention them in that
```
git status 
``` 
creating and saving the version
```
git commit 
```
to see all version previous or latest
```
git log 
```

to send version /changes to github
```
git push origin main
```

to check remote url

```
git remote -v
```

To Setup CI/CD pipeline in heroku we need three information

Heroku_email/

Heroku_API_KEY

HEROKU_APP_NAME

Build Docker Image
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```
To check running containers in docker
```
docker ps
```
 To stop docker container
 ```
 docker stop <container_id>
 ```
  
```
main.yml file helps to do continuous Integration/Development in the system
```
```
python setup.py install
```





