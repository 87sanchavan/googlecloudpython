from google.cloud import bigquery

bigquery_client= bigquery.Client()

# list of datasets
datasetsObj = bigquery_client.list_datasets();
datasetList = datasetsObj[0];
for dataset in datasetList:
    print(dataset.name)

# list of tables in a dataset

dataset = bigquery_client.dataset("mydataset")
tablesObj = dataset.list_tables()
tableList = tablesObj[0]
for table in tableList:
    print(table.name)


# Table Opearations

table = dataset.table("comments")
print(table.num_rows)
print( table.view_query)


print("Hiiii Tables")
print("Hiiii Tables 2")