class couch:

    sheng_mu = ['b','p','m','f','d',
                't', 'n', 'l', 'g', 'k',
                'h', 'j', 'q', 'x', 'zh',
                'ch', 'sh', 'r', 'z', 'c',
                's', 'y', 'w']
    yun_mu = ['ua','ei','e','ou','iu','ve','u','i','o','uo','ie',
              'a','ong','iong','ai','ing','uai','ang','uan','an','en','ia','iang','uang',
              'eng','in','ao','v','ui','un','iao','ian']

    codes = {
        'natural' : {
            'sheng_mu': ['b','p','m','f','d',
                         't', 'n', 'l', 'g', 'k',
                         'h', 'j', 'q', 'x', 'zh',
                         'ch', 'sh', 'r', 'z', 'c',
                         's', 'y', 'w'],
            'yun_mu': ['ua','ei','e','ou','iu','ve','u','i','o','uo','ie',
                        'a','ong','iong','ai','ing','uai','ang','uan','an','en','ia','iang','uang',
                        'eng','in','ao','v','ui','un','iao','ian'],
        }
    }

    code_selected = []

    def choose_code(self):
        print('choose your code :')
        for k in self.codes:
            print('---', k)
        code = input('which code?')
        while not self.codes.__contains__(code):
            code = input('no code found, switch one?')
        self.code_selected = self.codes[code]

    def test(self):
        self.choose_code()
        print(self.code_selected)


if __name__ == '__main__':
    couch().test()