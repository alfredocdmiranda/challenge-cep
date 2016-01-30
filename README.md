# Challenge Cep

That is just a challenge. It is a Rest API which should return information about 
Brazilian Zipcodes(CEP).

## Installing

You can see all libs are required inside the requirements file and you might 
use pip to install them.

    pip install -r requirements.txt

You are not required to install the project.

## Running

You can run the project with this command:

    python server.py

## Using

You can use a browser or use any other software to use this API. I will use
`curl` as example.

Get a list of all CEPs and their information:

    curl http://localhost:8888/cep/

You also can limit how many CEPs will be shown to you.

    curl -H "Content-Type: application/json" -d '{"limit": "10"}' http://localhost:8888/cep/

Get information about a specific CEP:

    curl http://localhost:8888/cep/60325600

Ask to insert information about a CEP which is not included yet. See, if you try 
to insert a CEP which is not valid, it will return an 404 ERROR.

     curl -X POST -H "Content-Type: application/json" -d '{"cep": "60325600"}' http://localhost:8888/cep/

Update any information about a specific CEP.

    curl -X PUT -H "Content-Type: application/json" -d '{"cidade": "Sao Paulo"}' http://localhost:8888/cep/60325600

Delete a CEP from our database.

    curl -X DELETE http://localhost:8888/cep/60325600
