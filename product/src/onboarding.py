# Databricks notebook source
# MAGIC %pip install "/Volumes/dihpoc/testing/configurations/dih_meta-0.1.0-py3-none-any.whl" --quiet

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import yaml

# COMMAND ----------

from src.onboard_dataflowspec import OnboardDataflowspec

onboarding_params_map: dict = {
                      "onboarding_file_path": "/Volumes/dihpoc/testing/configurations/onboarding.yml",
                      "catalog": "dihpoc",
                      "schema": "dataflow_specs",
                      "raw_dataflowspec_table":"mara_raw_dataflowspec",
                      "trusted_dataflowspec_table":"mara_trusted_dataflowspec",
                      "ssot_dataflowspec_table": "mara_ssot_dataflow_spec",
                      "overwrite":"True",
                      "version":"v1",
                      "import_author":"skyler.myers@databricks.com",
}

OnboardDataflowspec(spark, onboarding_params_map).onboard_dataflow_specs()
