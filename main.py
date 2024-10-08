import logging
from app.configure import Config
from app.task_solver import TaskSolver
import requests
import json
from pprint import pprint
from os import getenv

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

text = """F1 = F2 = randint(3, 10)
alpha = choice([30, 45, 60])
text = f'Определить модуль равнодействующей двух равных по модулю сходящихся сил F1 = F2 = {F1} Н, образующих между собой угол α = {alpha}°. Ответ округлить до сотых.'
alpha = rad(alpha)
result = round((F1**2 + F2**2 + 2 * F1 * F2 * cos(alpha))**0.5, 2)"""

# task = Config().get_task(category='mechanic')

# print(task(0)['data'])

pprint(text)
