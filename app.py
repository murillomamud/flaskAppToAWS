from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World from AWS ECS</h1> <a href='https://medium.com/@murillomamud/deploy-flask-app-to-aws-ecs-service-80d96ee14254'> Link to Tutorial </a>" 


if __name__ == '__main__':
    app.run()    
