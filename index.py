import json
from app.task_solver import TaskSolver

def handler(event, context):
    """Yandex.Cloud functions handler."""

    if event['httpMethod'] == 'GET':
        # Bot and dispatcher initialization
        data = event['pathParams']
        task = TaskSolver(category=data['category'], level=data['level'])
        body = {
            'statusCode': 200,
            'body': task(data['num'])
            }
        return json.dumps(body, indent=4, ensure_ascii=False)

    return {'statusCode': 405}