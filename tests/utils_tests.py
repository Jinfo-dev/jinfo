import os
import sys
import unittest

# Explicit path modification to import jinfo from the higher level folder, from: docs.python-guide.org/writing/structure
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from jinfo.utils.one_hot_dna import one_hot_dna
from jinfo.utils.random_DNASeq import random_DNASeq
from jinfo.utils.DNASeq_from_NCBI import DNASeq_from_NCBI
from jinfo.utils.seq_list_to_fasta import seq_list_to_fasta
from jinfo.utils.seq_list_from_fasta import seq_list_from_fasta
from jinfo.utils.seq_from_fasta import seq_from_fasta
from jinfo.utils.alignment_from_fasta import alignment_from_fasta
from jinfo.utils.multialign import multialign
from jinfo.utils.calc_phylo_tree import calc_phylo_tree
from jinfo.utils.percentage_identity import percentage_identity
from jinfo.utils.remove_degenerate_seqs import remove_degenerate_seqs
