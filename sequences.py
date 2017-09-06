from abc import ABC, abstractmethod
import settings

class BaseSequence(ABC):
    def __init__(self, seq):
        self.seq = seq
        self._verify_seq()

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
