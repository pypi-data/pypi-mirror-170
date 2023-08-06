#!/bin/bash
#########################################################
#                     PARAMETERS                        #
#########################################################
composer_name="txp-composer"
# TODO: put correct parameters here
pending_signal_chunks_collection_name="pending_signal_chunks"
signals_queue_collection="signals_queue"
dataset="telemetry"
model_signals_topic_name="txp-model-serving-signals"
data_lake_bucket_name="tranxpert-mvp-telemetry-data-lake"
topic_id="txp-telemetry-batch"
cloud_function_name="store_telemetry_event_to_data_lake"

composer_bucket=$1
composer_resources_bucket=$2

composer_dags_folder="$composer_bucket/dags/reports_generator/"
composer_resources_batch_pipeline_folder="$composer_resources_bucket/pipelines/reports/batch_pipeline/"

script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $script_dir
cd ../
rm -rf dist
gsutil cp ./pipelines/reports/batch_pipeline/setup.py $composer_dags_folder
gsutil cp ./pipelines/reports/batch_pipeline/batch_pipeline.py $composer_resources_batch_pipeline_folder

location=$3


cd ./composer

echo Deploying reports batch pipeline
gcloud composer environments update $composer_name --update-pypi-packages-from-file requirements.txt --location $location
gcloud composer environments storage dags import --environment $composer_name --location $location --source ./dag_signals_publisher.py \
--project tranxpert-mvp