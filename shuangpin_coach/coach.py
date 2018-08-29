import random
from Logger import Logger
# 刚到家，十一点五十了，水一个卡吧
class couch:
    codes = {
        'natural': {
            'sheng_mu': {
                'q': 'q', 'w': 'w',
                'r': 'r',
                't': 't', 'y': 'y',
                'sh': 'u', 'ch': 'i', 'un': 'p',
                's': 's',
                'd': 'd',
                'f': 'f', 'g': 'g',
                'h': 'h', 'j': 'j',
                'k': 'k', 'l': 'l',
                'z': 'z', 'x': 'x',
                'c': 'c', 'zh': 'v',
                'b': 'b', 'n': 'n',
                'm': 'm'
            },
            'yun_mu': {
                'iu': 'q', 'ua': 'w', 'ia': 'w',
                'e': 'e', 'uan': 'r', 'van': 'r',
                'ue': 't', 've': 't', 'uai': 'y', 'ing': 'y',
                'u': 'u', 'i': 'i',
                'uo': 'o', 'o': 'o', 'un': 'p', 'vn': 'p',
                'a': 'a', 'iong': 's', 'ong': 's',
                'uang': 'd', 'iang': 'd',
                'en': 'f', 'eng': 'g',
                'ang': 'h', 'an': 'j',
                'ao': 'k', 'ai': 'l',
                'ei': 'z', 'ie': 'x',
                'iao': 'c', 'v': 'v', 'ui': 'v',
                'ou': 'b', 'in': 'n',
                'ian': 'm'
            },
        }
    }

    code_selected = []

    def __init__(self):
        pass

    def choose_code(self):
        print('choose your code :')
        for k in self.codes:
            print('---', k)
        code = input('which code?')
        while not self.codes.__contains__(code):
            code = input('no code found, switch one?')
        self.code_selected = self.codes[code]
        self.logger = Logger(code)

    def test(self):
        self.choose_code()
        while True:
            answer = random.sample(self.code_selected['yun_mu'].keys(), 1)[0]
            print('please insert code for : ',answer)
            a = input()
            while a != self.code_selected['yun_mu'][answer]:
                if a == 'exit':
                    self._exit()
                elif a == 'help':
                    self.help(answer)
                else:
                    self.logger.log(answer + ',' + self.code_selected['yun_mu'][answer] + ',wrong')
                    print('wrong! try again : ')
                a = input()
            print('good job!')
            self.logger.log(answer + ',' + self.code_selected['yun_mu'][answer] + ',right')

    def help(self, code):
        print('the answer is ', self.code_selected['yun_mu'][code])

    def _exit(self):
        print('Bye!')
        exit(0)


if __name__ == '__main__':
    couch().test()
