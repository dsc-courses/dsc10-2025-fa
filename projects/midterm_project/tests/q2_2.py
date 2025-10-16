test = {   'name': 'q2_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> result = get_feature_values(favorite_uri, billions_club, ['Danceability', 'Energy'])\n"
                                               '>>> isinstance(result, np.ndarray) and isinstance(result[0], float) \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> 'float' in str(get_feature_values(favorite_uri, billions_club, ['Danceability', 'Energy']).dtype) # Make sure you use `.loc` on a DataFrame where "
                                               'all columns contain data of the same type.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> get_feature_values('abcde', billions_club, ['Danceability', 'Energy']) is None\nThis URI was not found.\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> result = get_feature_values('1dGr1c8CrMLDpV6mPbImSI', billions_club, ['Danceability', 'Energy'])\n>>> np.allclose(result, [0.359, 0.543])\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
