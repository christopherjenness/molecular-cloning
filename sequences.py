import os
import re
from abc import ABC, abstractmethod
from collections import defaultdict
import pickle
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

    def save_seq(self, fname):
        if os.path.splitext(fname)[1] != '.d':
            fname += '.d'
        pickle.dump(self, open(fname, "wb"))


class DNASequence(BaseSequence):

    def _verify_seq(self):
        allowed = set('ATCG')
        if not set(self.seq) <= allowed:
            unallowed = set(self.seq) - allowed
            raise ValueError('Seq contains unallowed chars: {unallowed}'
                             .format(unallowed=unallowed))

    def translate(self):
        codons = map(''.join, zip(*[iter(self.seq)]*3))
        amino_acids = map(settings.CODONS.get, codons)
        amino_acids_abbreviations = map(settings.ACIDS.get, amino_acids)
        print(list(amino_acids_abbreviations))
        return ProteinSequence(amino_acids_abbreviations)

    def detect_cutsite(self, regex):
        match_sites = []
        matches = re.finditer(regex, ''.join(self.seq))
        for match in matches:
            match_sites.append(match.span())
        return match_sites

    def detect_cutsites(self):
        all_cutsites = defaultdict(list)
        for regex in settings.CUTSITES.keys():
            for match in self.detect_cutsite(regex):
                all_cutsites[match].append(settings.CUTSITES[regex])
        return all_cutsites


class ProteinSequence(BaseSequence):

    def _verify_seq(self):
        allowed = set(settings.ACIDS.values())
        if not set(self.seq) <= allowed:
            unallowed = set(self.seq) - allowed
            raise ValueError('Seq contains unallowed chars: {unallowed}'
                             .format(unallowed=unallowed))

    def is_protein(self, start=False):
        """
        Determines if sequence is a protein (ORF)

        Args:
            start (bool): If true, sequence must start with MET

        Returns:
            bool: True if sequence is an ORG
            """
        if '-' not in self.seq[:-1]:
            if start:
                return self.seq[0] == 'M'
            return True
        return False

    def get_mass(self):
        """
        Calculates molecular weight of sequence
        """
        mass = [settings.WEIGHTS[x] for x in self.seq]
        total_mass = sum(mass)
        return total_mass

    def get_absorbance(self):
        """
        Calaculates A280 absorbance
        """
        absorbance = [settings.ABSORBANCES.get(x, 0) for x in self.seq]
        total_absorbance = sum(absorbance)
        return total_absorbance


def load_seq(fname):
    seq = pickle.load(open(fname, "rb"))
    return seq
