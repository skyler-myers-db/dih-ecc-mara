# Databricks notebook source
# MAGIC %pip install /Workspace/Users/skyler.myers@sobeys.com/sobeys/dlt_meta-0.0.3-py3-none-any.whl --force-reinstall --quiet

# COMMAND ----------

onboarding_params_map: dict = {
		"database": "dihpoc.dataflowspec_tables",
		"onboarding_file_path": "../configs/onboarding_spec.json",
		"bronze_dataflowspec_table": "raw_dataflowspec_table_mara", 
		"bronze_dataflowspec_path": "dbfs:/onboarding_tables_cdc/bronze",
		"silver_dataflowspec_table": "trusted_dataflowspec_table_mara",
		"silver_dataflowspec_path": "dbfs:/onboarding_tables_cdc/silver",
		"overwrite": "True",
		"env": "dev",
		"version": "v1",
		"import_author": "skyler.myers@databricks.com",
	}

from src.onboard_dataflowspec import OnboardDataflowspec
OnboardDataflowspec(spark, onboarding_params_map).onboard_dataflow_specs()