#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = 'news'

db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# Query 1
query = \
    """
SELECT title,
       Count(*) AS Views
FROM   articles
       INNER JOIN log
               ON path LIKE Concat('%%', slug)
GROUP  BY title
ORDER  BY views DESC
LIMIT  3;
"""
c.execute(query)
rows = c.fetchall()

print ''
print 'The most popular three articles of all time:'
for row in rows:
    print '  ', u'\u2022 ' + row[0] + ' -- ' + str(row[1]) + ' views'


# Query 2
query = \
    """

SELECT name,
       VIEWS
FROM   authors
       inner join (SELECT author,
                          Count(slug) AS VIEWS
                   FROM   articles
                          inner join log
                                  ON path LIKE Concat('%%', slug)
                   GROUP  BY author)VIEWS
               ON authors.id = author;
"""
c.execute(query)
rows = c.fetchall()

print ''
print 'The most popular article authors of all time:'
for row in rows:
    print '  ', u'\u2022 ' + row[0] + ' -- ' + str(row[1]) + ' views'


# Query 3
query = \
    """
SELECT TEST.DATE, TEST.result
FROM   (SELECT ( Cast(( Cast (failed_requests.errors AS FLOAT) / Cast(
                                         all_requests.requests AS FLOAT)
                      ) AS DECIMAL(16, 4)) * 100 ) AS result,
               failed_requests.date
        FROM   (SELECT Date(time),
                       Count(*) AS errors
                FROM   log
                WHERE  status = '404 NOT FOUND'
                GROUP  BY date) failed_requests
               JOIN (SELECT Date(time),
                            Count(*) AS requests
                     FROM   log
                     GROUP  BY date) all_requests
                 ON failed_requests.date = all_requests.date) AS TEST
WHERE  TEST.result > 1;
"""

c.execute(query)
rows = c.fetchall()

print ''
print 'Days where more than 1% of requests lead to errors:'
for row in rows:
    print '  ', u'\u2022 ' + str(row[0]) + ' -- ' + str(row[1]) \
        + ' % errors'
print ''

db.close()
