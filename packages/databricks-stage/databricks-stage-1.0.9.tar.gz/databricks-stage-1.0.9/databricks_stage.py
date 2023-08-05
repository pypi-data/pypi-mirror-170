import argparse
from pyspark.sql import SparkSession

def run():
    parser = argparse.ArgumentParser(description='Stage data for fast ingest.')
    parser.add_argument('--compression_format', required=False)
    parser.add_argument('--data_format', required=False)
    parser.add_argument('--sql_query', required=False)
    parser.add_argument('--stage_destination_uri', required=False)

    parser.add_argument('--csv_delimiter', required=False, default="\x1e")
    parser.add_argument('--csv_null_value', required=False, default='_SISU_NULL')

    # deprecated args
    parser.add_argument('--access_key_id', required=False)
    parser.add_argument('--secret_access_key', required=False)
    parser.add_argument('--stage_output_bucket', required=False)
    parser.add_argument('--stage_output_prefix', required=False)

    args = parser.parse_args()

    spark = SparkSession.builder.getOrCreate()

    if args.access_key_id is not None:
        # deprecated path
        df = spark.sql(f"""{args.sql_query}""")
        df.write \
            .format("csv") \
            .option("compression", "gzip") \
            .option("nullValue", "_SISU_NULL") \
            .option("delimiter", "\x1e") \
            .mode("overwrite") \
            .save(f"s3a://{args.access_key_id}:{args.secret_access_key}@{args.stage_output_bucket}/{args.stage_output_prefix}")
    else:
        df = spark.sql(f"""{args.sql_query}""")
        df.write \
            .format(args.data_format) \
            .option("compression", args.compression_format) \
            .option("delimiter", args.csv_delimiter) \
            .option("nullValue", args.csv_null_value) \
            .mode("overwrite") \
            .save(args.stage_destination_uri)
