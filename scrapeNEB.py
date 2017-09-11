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
    series = pd.Series(df['Enzyme'].values,
                       index=df['Recognition Sequence'])
    restriction_sites = series.to_dict()
    return restriction_sites
