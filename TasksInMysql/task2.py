from . import DatabaseContextManager

"""
- fetch total sum of new shares by season
- fetch total sum of new shares during thunderstorms
- fetch the date and hour with the most new shares
"""

seasons = {0: "spring", 1: "summer", 2: "autumn", 3: "winter"}
with DatabaseContextManager() as cursor:
    print("total sum of new shares by season:")
    cursor.execute("SELECT season, sum(cnt) FROM bikesharing GROUP BY season")
    for row in cursor.fetchall():
        print(f"{seasons[row[0]]}: {row[1]}")

    print("total sum of new shares during thunderstorms:")
    cursor.execute("SELECT sum(cnt) FROM bikesharing WHERE weather_code > 2")
    print(cursor.fetchone())

    print("date and hour with the most new shares:")
    cursor.execute("SELECT tstamp, cnt FROM bikesharing ORDER BY cnt DESC")
    date, shares = cursor.fetchone()
    print(f"{date} with {shares} shares")

    cursor.close()




