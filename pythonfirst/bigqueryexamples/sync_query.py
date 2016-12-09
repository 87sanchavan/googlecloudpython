import argparse

# [START sync_query]
from google.cloud import bigquery

client1 = bigquery.Client()

results= client1.run_sync_query("select * from mydatasets.comments")
results.run()


def sync_query(query):
    client = bigquery.Client()


    query_results = client.run_sync_query(query)


    # Use standard SQL syntax for queries.
    # See: https://cloud.google.com/bigquery/sql-reference/
    query_results.use_legacy_sql = False

    query_results.run()

    # Drain the query results by requesting a page at a time.
    page_token = None

    while True:
        rows, total_rows, page_token = query_results.fetch_data(
            max_results=10,
            page_token=page_token)

        for row in rows:
            print(row)

        if not page_token:
            break
# [END sync_query]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('query', help='BigQuery SQL Query.')

  #  args = parser.parse_args()
    query ='SELECT corpus FROM `publicdata.samples.shakespeare` GROUP BY corpus'

    sync_query(query)