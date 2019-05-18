class MorseTree:
    root = {}
    End = '/'
    def add(self,wordlist):
        node = self.root
        for code in wordlist:
            node = node.setdefault(re.sub('x', '.', code),{})