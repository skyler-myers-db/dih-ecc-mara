# Databricks notebook source
# MAGIC %pip install /Workspace/Users/skyler.myers@sobeys.com/sobeys/dlt_meta-0.0.3-py3-none-any.whl --force-reinstall --quiet

# COMMAND ----------

layer = spark.conf.get("layer", None)
from src.dataflow_pipeline import DataflowPipeline
DataflowPipeline.invoke_dlt_pipeline(spark, layer)