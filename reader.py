class Reader:
    def read_code(path):
        readed_code = []
        with open(path, encoding='utf8') as f:
            for i in f:
                readed_code.append(i) # прочитали весь код построчно
        return readed_code