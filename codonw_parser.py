from collections import defaultdict
import pandas as pd
import re
import click

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('codonw_table')
@click.option('--output_table', default=None)
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
                    if re.search('[A|T|C|G]{3}', v):
                        d.append({'codon': v,'val1':vec[i + 1],'val2':vec[i+2]})

    dflist = []
    for i in big_dict.keys():
        df = pd.DataFrame(big_dict[i])
        df['orf'] = i
        dflist.append(df)

    out_tbl = pd.concat(dflist)
    out_tbl[['orf','codon','val1','val2']].to_csv(output_table, index=False)


if __name__=='__main__':
    codonw_to_table()
