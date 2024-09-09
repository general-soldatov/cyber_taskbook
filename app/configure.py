from dotenv import load_dotenv
from os import getenv

class Config:
    def __init__(self) -> None:
        load_dotenv()

    def get_task(self, category: str):
        hyper_text = {
            'mechanic': getenv('MECHANIC'),
            'termodynamic': getenv('TERMODYNAMIC'),
            'mkt': getenv('MKT'),
            'electrostatic': getenv('ELECTROSTATIC'),
            'electrodynamic': getenv('ELECTRODYNAMIC'),
            'electromagnetism': getenv('ELECTROMAGNETISM'),
            'optics': getenv('OPTICS')
        }
        try:
            return hyper_text[category]
        except KeyError:
            return None