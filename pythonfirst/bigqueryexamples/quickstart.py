def run_quickstart():
    # [START bigquery_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import bigquery

    # Instantiates a client
    bigquery_client = bigquery.Client()

    # The name for the new dataset
    dataset_name = 'my_new_dataset1'

    # Prepares the new dataset
    dataset = bigquery_client.dataset(dataset_name)

    # Creates the new dataset
    dataset.create()

    print('Dataset {} created.'.format(dataset.name))
    # [END bigquery_quickstart]


if __name__ == '__main__':
    run_quickstart()