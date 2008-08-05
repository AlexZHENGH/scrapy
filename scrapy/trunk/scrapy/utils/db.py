"""
Function for dealing with databases
"""
import re
from scrapy.conf import settings

def mysql_connect(db_uri, **kwargs):
    """
    Connects to a MySQL DB given a mysql URI
    """
    import MySQLdb

    if not db_uri or not db_uri.startswith('mysql://'):
        raise Exception("Incorrect MySQL URI: %s" % db_uri)
    m = re.search(r"mysql:\/\/(?P<user>[^:]+)(:(?P<passwd>[^@]+))?@(?P<host>[^/]+)/(?P<db>.*)$", db_uri)
    if m:
        d = m.groupdict()
        if d['passwd'] is None:
            del(d['passwd'])

        d.update(settings.get("MYSQL_CONNECTION_SETTINGS"))
        d.update(kwargs)
        return MySQLdb.connect(**d)
