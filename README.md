# yake-lambda
YAKE web API using AWS Lambda

### Requirements

* [Python 3.6](https://www.python.org/)
 
## Install dependecies

Install python dependencies using pip and virtualenv:

```sh 
pip install venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Using conda:

```sh  
conda install --file requirements.txt
```

## Running local mode

This project is based on a microframework called [Chalice](https://github.com/aws/chalice/), a Python Serverless Microframework for AWS. Chalice allows you to quickly create and deploy applications that use [Amazon Lambda](https://aws.amazon.com/lambda/). For more information on how to setup and deploy this project to Amazon AWS please check [Chalice Documentation](https://github.com/aws/chalice/). 

In order to run it locally just type:

```sh
chalice local
```

Check http://localhost:8000

### Trying out

Trying out using cURL

```sh
curl --request POST \
  --url https://localhost:8000/yake/extract_keywords \
  --header 'content-type: application/json' \
  --data '{
	"text":"Sources tell us that Google is acquiring Kaggle, a platform that hosts data science and machine learning competitions. Details about the transaction remain somewhat vague , but given that Google is hosting its Cloud Next conference in San Francisco this week, the official announcement could come as early as tomorrow.  Reached by phone, Kaggle co-founder CEO Anthony Goldbloom declined to deny that the acquisition is happening. Google itself declined '\''to comment on rumors'\''.",
	"language":"lan",
	"max_ngram_size":3
	
}'
```