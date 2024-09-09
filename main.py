from app.configure import Config

task = Config().get_task(category='mechanic')
print(task)