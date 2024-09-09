import math
from random import randint, choice

lst = [1, 2, 3, 4]

class TaskSolver:
    def __init__(self, category: str, level: int):
        self.category: str = category
        self.level: int = level

    def __call__(self, number: int) -> dict:
        if number <= max(lst):
            text: str = 'Your task miht'
            image: bool | str = False
            result: int | float = 3555

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