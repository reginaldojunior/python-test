import os
import re
from configs import settings

# /^\d{3}\.\d{3}\.\d{3}\-\d{2}$/


class CPF(object):

    """docstring for CPF"""

    def __init__(self, cpf):
        self.cpf = cpf

    def is_blacklist(self):
        return self.cpf_is_blacklist()

    def cpf_is_blacklist(self):
        with open(os.path.join(settings.BASE_DIR, 'blacklist.txt')) as f:
            cpfs = f.readlines()

            for cpf_txt in cpfs:
                cpf_clear = cpf_txt.replace('.', '').replace('-', '')

                if self.cpf == "".join(cpf_clear.split()):
                    return False

        return True
