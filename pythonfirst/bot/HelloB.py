import boto3

client = boto3.client("")

def build_model(data_s3_url, schema_fn, recipe_fn, name, train_percent=70):
    """Creates all the objects needed to build an ML Model & evaluate its quality.
    """
    ml = boto3.client('machinelearning')
    (train_ds_id, test_ds_id) = create_data_sources(ml, data_s3_url, schema_fn,
                                                    train_percent, name)
    ml_model_id = create_model(ml, train_ds_id, recipe_fn, name)
    eval_id = create_evaluation(ml, ml_model_id, test_ds_id, name)

    return ml_model_id


