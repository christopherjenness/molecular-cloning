import pandas as pd

URL = 'https://www.neb.com/tools-and-resources/selection-charts/alphabetized-list-of-recognition-specificities'


def import_NEB(url=URL):
    """imports all of NEBs restriction sites

        Args:
            url (str): Site where restriction sites are hosted

        Returns:
            dict: Dict of {Recognition Sequence: NEB enzyme}
    """
    df = pd.read_html(url)[0]
    df = pd.DataFrame(df['Enzyme'].str.split(' ').tolist(),
                      index=df['Recognition Sequence']).stack()
    df = df.reset_index()[[0, 'Recognition Sequence']]
    df.columns = ['Enzyme', 'Recognition Sequence']
    df = df[~df['Recognition Sequence'].str.contains("\(")]
    df = df[df['Recognition Sequence'].str.contains("/")]
    series = pd.Series(df['Enzyme'].values,
                       index=df['Recognition Sequence'])
    restriction_sites = series.to_dict()
    return restriction_sites


def convert_to_regex(restriction_site, NEB_dict):
    enzyme = NEB_dict[restriction_site]
    regex = restriction_site
    regex = regex.replace('N', '[ATCG]')
    regex = regex.replace('Y', '[CT]')
    regex = regex.replace('M', '[CA]')
    regex = regex.replace('R', '[AG]')
    regex = regex.replace('K', '[TC]')
    regex = regex.replace('S', '[GC]')
    regex = regex.replace('W', '[AT]')
    regex = regex.replace('D', '[AGT]')
    regex = regex.replace('V', '[ACG]')
    regex = regex.replace('H', '[ACT]')
    regex = regex.replace('B', '[CGT]')
    cutsite = regex.index('/')
    regex = regex.replace('/', '')
    return regex, enzyme, cutsite


def generate_regex_dict():
    sites = import_NEB()
    regex_dict = {}
    for site in sites:
        regex, enzyme, cutsite = convert_to_regex(site, sites)
        regex_dict[regex] = (enzyme, cutsite)
    return regex_dict
