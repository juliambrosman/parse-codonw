from __future__ import print_function

from collections import defaultdict
import pandas as pd
import re
import click

codons = {'AAA': 'Lys',
 'AAC': 'Asn',
 'AAG': 'Lys',
 'AAU': 'Asn',
 'ACA': 'Thr',
 'ACC': 'Thr',
 'ACG': 'Thr',
 'ACU': 'Thr',
 'AGA': 'Arg',
 'AGC': 'Ser',
 'AGG': 'Arg',
 'AGU': 'Ser',
 'AUA': 'Ile',
 'AUC': 'Ile',
 'AUG': 'Met',
 'AUU': 'Ile',
 'CAA': 'Gln',
 'CAC': 'His',
 'CAG': 'Gln',
 'CAU': 'His',
 'CCA': 'Pro',
 'CCC': 'Pro',
 'CCG': 'Pro',
 'CCU': 'Pro',
 'CGA': 'Arg',
 'CGC': 'Arg',
 'CGG': 'Arg',
 'CGU': 'Arg',
 'CUA': 'Leu',
 'CUC': 'Leu',
 'CUG': 'Leu',
 'CUU': 'Leu',
 'GAA': 'Glu',
 'GAC': 'Asp',
 'GAG': 'Glu',
 'GAU': 'Asp',
 'GCA': 'Ala',
 'GCC': 'Ala',
 'GCG': 'Ala',
 'GCU': 'Ala',
 'GGA': 'Gly',
 'GGC': 'Gly',
 'GGG': 'Gly',
 'GGU': 'Gly',
 'GUA': 'Val',
 'GUC': 'Val',
 'GUG': 'Val',
 'GUU': 'Val',
 'UAA': 'TER',
 'UAC': 'Tyr',
 'UAG': 'TER',
 'UAU': 'Tyr',
 'UCA': 'Ser',
 'UCC': 'Ser',
 'UCG': 'Ser',
 'UCU': 'Ser',
 'UGA': 'TER',
 'UGC': 'Cys',
 'UGG': 'Trp',
 'UGU': 'Cys',
 'UUA': 'Leu',
 'UUC': 'Phe',
 'UUG': 'Leu',
 'UUU': 'Phe'}

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('codonw-table')
@click.option('--output-table', default=None)
def codonw_to_table(codonw_table, output_table=None):

    if not output_table:
        output_table = "./parsed_codonw.csv"

    big_dict = defaultdict(lambda:[])

    with open(codonw_table) as ih:
        d = []
        for l in ih:
            if "codons in" in l:
                orf = "_".join(l.split()[3].split("_")[0:2])
                big_dict[orf] += d
                d = []
            else:
                vec = l.strip().split()
                for i, v in enumerate(vec):
                    if re.search('[A|T|C|G|U]{3}', v):
                        d.append({'codon': v,'AA':codons[v],'val1':vec[i + 1],'val2':vec[i+2]})

    dflist = []
    for i in big_dict.keys():
        df = pd.DataFrame(big_dict[i])
        df['orf'] = i
        dflist.append(df)

    out_tbl = pd.concat(dflist)
    #out_tbl = out_tbl.merge(pd.DataFrame(codons), on='codon', how='outer')[['orf','codon','aa','val1','val2']]
    out_tbl[['orf','AA','codon','val1','val2']].to_csv(output_table, index=False)


if __name__=='__main__':
    codonw_to_table()
