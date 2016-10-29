#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_04."""


import data


D = data.BANDS


D['Buckingham Nicks'] = {'Lindsey Buckingham': ['guitar', 'vocals'],
                         'Stevie Nicks': ['vocals', 'tambourine']}
D['Fleetwood Mac'].update(D['Buckingham Nicks'])
