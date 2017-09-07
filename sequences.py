from abc import ABC, abstractmethod
import settings

class BaseSequence(ABC):
    def __init__(self, seq):
        self.seq = list(seq)
        self._verify_seq()

    def __repr__(self):
        return("{class_name}('{seq}')"
               .format(class_name=self.__class__.__name__,
                       seq=''.join(self.seq)))

    def __str__(self):
        if len(self.seq) > 22:
            return ''.join(self.seq[:10] + '...' + self.seq[-10:])
        else:
            return ''.join(self.seq)

    def __eq__(self, other):
        return self.seq == other.seq

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, key):
        return self.seq[key]

    def __setitem__(self, key, value):
        self.seq[key] = value

    def __iter__(self):
        for i in self.seq:
            yield i

    def __contains__(self, item):
        return item in self.seq
        
    @abstractmethod
    def _verify_seq(self):
        pass


class DNASequence(BaseSequence):

    def _verify_seq(self):
        allowed = set('ATCG')
        if not set(self.seq) <= allowed:
            unallowed = set(self.seq) - allowed
            raise ValueError('Seq contains unallowed chars: {unallowed}'
                             .format(unallowed=unallowed))
        


class ProteinSequence(BaseSequence):
    def _verify_seq(self):
        allowed = set(settings.ACIDS.values())
        if not set(self.seq) <= allowed:
            unallowed = set(self.seq) - allowed
            raise ValueError('Seq contains unallowed chars: {unallowed}'
                             .format(unallowed=unallowed))
