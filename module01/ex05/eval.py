class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if type(coefs) != list or any(type(coef) != float for coef in coefs):
            return -1
        if type(words) != list or any(type(word) != str for word in words):
            return -1
        if len(coefs) != len(words):
            return -1
        itr = zip(words, coefs)
        ret = 0
        for tpl in itr:
            ret += len(tpl[0]) * tpl[1]
        return ret

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if type(coefs) != list or any(type(coef) != float for coef in coefs):
            return -1
        if type(words) != list or any(type(word) != str for word in words):
            return -1
        if len(coefs) != len(words):
            return -1
        if len(coefs) != len(words):
            return -1
        ret = 0
        for count, word in enumerate(words):
            ret += len(word) * coefs[count]
        return ret
