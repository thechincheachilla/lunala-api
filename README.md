# lunala-api

### Running on Heroku
Easy way: impport this GitHub repo to a Heroku repo 
Manual way: \
Install the Heroku CLI, run ```heroku login``` and login\
Run: ```heroku create NAME_HERE --buildpack heroku/python```\
Run: ```git init```\
Run: ```git add .```\
Run: ```git commit -m "Commit message thingy"```\
Run: ```heroku git:remote -a NAME_FROM_STEP_2```\
Run: ```git push heroku master```\
App deployed at https://NAME.herokuapp.com/
