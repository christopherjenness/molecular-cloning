from collections import defaultdict
import scrapeNEB

CODONS = {"TTT": "Phe", "TCT": "Ser", "TAT": "Tyr", "TGT": "Cys",
          "TTC": "Phe", "TCC": "Ser", "TAC": "Tyr", "TGC": "Cys",
          "TTA": "Leu", "TCA": "Ser", "TAA": "TER", "TGA": "TER",
          "TTG": "Leu", "TCG": "Ser", "TAG": "TER", "TGG": "Trp",
          "CTT": "Leu", "CCT": "Pro", "CAT": "His", "CGT": "Arg",
          "CTC": "Leu", "CCC": "Pro", "CAC": "His", "CGC": "Arg",
          "CTA": "Leu", "CCA": "Pro", "CAA": "Gln", "CGA": "Arg",
          "CTG": "Leu", "CCG": "Pro", "CAG": "Gln", "CGG": "Arg",
          "ATT": "Ile", "ACT": "Thr", "AAT": "Asn", "AGT": "Ser",
          "ATC": "Ile", "ACC": "Thr", "AAC": "Asn", "AGC": "Ser",
          "ATA": "Ile", "ACA": "Thr", "AAA": "Lys", "AGA": "Arg",
          "ATG": "Met", "ACG": "Thr", "AAG": "Lys", "AGG": "Arg",
          "GTT": "Val", "GCT": "Ala", "GAT": "Asp", "GGT": "Gly",
          "GTC": "Val", "GCC": "Ala", "GAC": "Asp", "GGC": "Gly",
          "GTA": "Val", "GCA": "Ala", "GAA": "Glu", "GGA": "Gly",
          "GTG": "Val", "GCG": "Ala", "GAG": "Glu", "GGG": "Gly"}

ACIDS = {"Phe": "F", "Ser": "S", "Tyr": "Y", "Cys": "C", "Leu": "L",
         "TER": "-", "Trp": "W", "Pro": "P", "His": "H", "Arg": "R",
         "Ala": "A", "Glu": "E", "Gly": "G", "Gln": "Q", "Asn": "N",
         "Val": "V", "Ile": "L", "Met": "M", "Asp": "D", "Thr": "T",
         "Lys": "K"}

WEIGHTS = {'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1, 'C': 121.2,
           'E': 147.1, 'Q': 146.2, 'G': 75.1, 'H': 155.2, 'I': 131.2,
           'L': 131.2, 'K': 146.2, 'M': 149.2, 'F': 165.2, 'P': 115.1,
           'S': 105.1, 'T': 119.1, 'W': 204.2, 'Y': 181.2, 'V': 117.1,
           '-': 0.0}

ABSORBANCES = {'W': 5500, 'Y': 1490}

CUTSITES = scrapeNEB.generate_regex_dict()
