"""

"""

from oop.adapter import  MySQLAdapter, MongoAdapter


def get_DB(type='mysql'):
    """

    Parameters
    ----------
    type

    Returns
    -------

    """

    if type == 'mysql':
        return  MySQLAdapter
    elif type == 'mongodb':
        return MongoAdapter