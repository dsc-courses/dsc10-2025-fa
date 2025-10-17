test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> isinstance(avg_age,bpd.DataFrame) and avg_age.shape == (2650, 3) and 'Average_Age' in avg_age.columns and baby.shape == (398437, 5) # Don't change "
                                               'the original baby DataFrame.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.isclose(avg_age[(avg_age.get('Name') == 'Kevin') & (avg_age.get('Gender') == 'F')].get('Average_Age').iloc[0], 48.571596244131456)\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
