import os
from configs import settings


class CPF(object):

    """docstring for CPF"""

    def __init__(self, cpf):
        self.cpf = cpf

    def is_valid(self):
        return True

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
