# jaaxman-lambda
Lambda functions for [jaaxman](https://github.com/shirakiya/jaaxman)  
  
Using [Zappa](https://github.com/Miserlou/Zappa) flamework.


## Environment
- Python >= 3.6


## SetUp
```
$ pip install -r requirements.txt
```


## Run
```
$ python fetchrss.py
```


## Deploy
### Preparing
```
$ cp lambda_function_env.sample.json lambda_function_env.json

$ vi lambda_function_env.json  #=> write credentials

$ aws s3 cp lambda_function_env.json <Amazon S3 path>
```


### Run deploy
```
$ cd <repository root>

$ zappa deploy
# or Once deployed
$ zappa update
```
