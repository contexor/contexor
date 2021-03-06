import string


class Ascify:

    '''
    USE EXAMPLE:

        out = asc.Ascify(df.text).ascify()

    '''
    def __init__(self, s):

        self.s = s
        self.printable = set(string.printable)
        self.iterable = self._is_iterable()

    def _is_iterable(self):

        out = hasattr(self.s, '__iter__')

        if out is True:

            self.length = len(self.s)

        return out

    def _printable(self):

        out = filter(lambda x: x in self.printable, self.s)

        return out

    def _stringify(self):

        out = ''

        o = Ascify(self.s)
        out += o._printable()
        out = out.encode('ascii')

        return out

    def _stringify_iter(self):

        out = []

        for i in range(self.length):

            temp = filter(lambda x: x in self.printable, self.s[i])
            temp = temp.encode('ascii')
            out.append(temp)

        return out

    def ascify(self):

        if self.iterable is False:

            out = self._stringify()

        else:

            out = self._stringify_iter()

        return out

# OUTPUT: a list with strings
