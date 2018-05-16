#!/usr/bin/python
# -*- coding: utf-8 -*-

# 将常量集中在一个文件中


class _const:

    class ConsError(TypeError): pass
    class ConsCaseError(ConsError): pass

    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise self.ConsError, "Can't change const.%s" % key

        if not key.isupper():
            raise self.ConsCaseError,  'const key "%s" is not all suppercase' % key

        self.__dict__[key] = value


import sys
sys.modules[__name__] = _const()


##把常量集中在此类中,调用时导入

import const

const.MY_FIRST_CONST = 'aBC'
const.MY_SECOND_CONST = 'AbC'
const.MY_THIRD_CONST = 'aBC'
