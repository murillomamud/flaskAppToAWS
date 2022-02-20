# Flask App to AWS

Flask application to be used in AWS ECS Service.

## Recommendations:

To run this application, I recommend using virtualenv:

```bash

pip install virtualenv

virtualenv .venv

source .venv/bin/activate

pip install -r requirements.txt

```

## Creating a Docker Image:

```bash

docker build -t yourname/yourImageName .

```

## Vefiry your Docker Image:

```bash

docker images

```

## Testing your image locally:

```bash

docker run -p 8000:5000 <full_image_name>

```

You should see the webpage accessing localhost:8000

## Tutorial:

[Medium](https://medium.com/@murillomamud/deploy-flask-app-to-aws-ecs-service-80d96ee14254)