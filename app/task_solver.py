import json
import logging
import math
import requests

from random import randint, choice

from .configure import Config

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

class TaskSolver:
    def __init__(self, category: str, level: str):
        self._category = category
        self.level: str = level
        self.data = self.get_json(category=self._category)

    def __call__(self, number: str) -> dict:
        if not self.data.get(self.level, False):
            return {
            'process': 'error',
            'data': {
                'text': 'Not nedding level'
                }
            }
        task = self.data[self.level].get(number, False)
        if task:
            image: bool | str = task['image']
            text, result = self.task_cod(task['code'])
            return {
                'process': 'succesful',
                'data': {
                    'text': text,
                    'image': image,
                    'result': result
                }
            }

        return {
            'process': 'error',
            'data': {
                'text': 'Max number of task'
                }
            }

    def add_task(self, text: str, image=False):
        data: dict = self.get_json(self._category)
        if not data.get(self.level, False):
            data[self.level] = dict()

        num = len(data[self.level])
        data[self.level][num] = {
            'code': text,
            'image': image
        }
        self.set_json(self._category, data)
        logger.info('Task append succesfully')

    @staticmethod
    def get_json(category: str, folder='task') -> dict:
        try:
            with open(f'{folder}/{category}.json', 'r', encoding='utf-8') as data_file:
                data = json.load(data_file)
        except Exception as e:
            logger.error(e)
            data = dict()
        return data

    @staticmethod
    def set_json(category: str, data: dict, folder='task'):
        with open(f'{folder}/{category}.json', 'w', encoding='utf-8') as data_file:
              json.dump(data, data_file, ensure_ascii=False, indent=4)

    @staticmethod
    def task_cod(txt_task):
        rad = lambda x: x * math.pi / 180
        grad = lambda x: 180 * x / math.pi
        lcls = locals()
        glbl = {
            'pi': math.pi,
            'cos': math.cos,
            'sin': math.sin,
            'tan': math.tan,
            'arctan': math.atan,
            'randint': randint,
            'choice': choice
        }
        exec(txt_task, glbl, lcls)
        return lcls['text'], lcls['result']


class TaskSolverURL(TaskSolver):

    @staticmethod
    def get_json(category: str) -> dict:
        url = Config().get_task(category)
        response = requests.get(url)
        return response.json()