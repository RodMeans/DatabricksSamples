# Databricks notebook source
# MAGIC %md
# MAGIC Azure ML & Azure Databricks notebooks by Parashar Shah.
# MAGIC 
# MAGIC Copyright (c) Microsoft Corporation. All rights reserved.
# MAGIC 
# MAGIC Licensed under the MIT License. 

# COMMAND ----------

# DBTITLE 1,Install SDK as a library (Mandatory)
# MAGIC %md
# MAGIC We support installing AML SDK as library from GUI. When attaching a library follow this https://docs.databricks.com/user-guide/libraries.html and add the below string as your PyPi package. You can select the option to attach the library to all clusters or just one cluster.
# MAGIC 
# MAGIC **azureml-sdk**
# MAGIC * Source: Upload Python Egg or PyPi
# MAGIC * PyPi Name: `azureml-sdk[databricks]`
# MAGIC * Select Install Library

# COMMAND ----------

# DBTITLE 1,Check SDK version 
import azureml.core

# Check core SDK version number - based on build number of preview/master.
print("SDK version:", azureml.core.VERSION)

# COMMAND ----------

# MAGIC %md
# MAGIC ![04ACI](files/tables/image2b.JPG)

# COMMAND ----------

# MAGIC %md
# MAGIC Please specify the Azure subscription Id, resource group name, workspace name, and the region in which you want to create the Azure Machine Learning Workspace.
# MAGIC 
# MAGIC You can get the value of your Azure subscription ID from the Azure Portal, and then selecting Subscriptions from the menu on the left.
# MAGIC 
# MAGIC For the resource_group, use the name of the resource group that contains your Azure Databricks Workspace.
# MAGIC 
# MAGIC NOTE: If you provide a resource group name that does not exist, the resource group will be automatically created. This may or may not succeed in your environment, depending on the permissions you have on your Azure Subscription.

# COMMAND ----------

# DBTITLE 1,Define workspace params
subscription_id = "<Your SubscriptionId>" #you should be owner or contributor
resource_group = "<Resource group - new or existing>" #you should be owner or contributor
workspace_name = "<workspace to be created>" #your workspace name
workspace_region = "<azureregion>" #your region

# COMMAND ----------

# DBTITLE 1,Authenticate Azure subscription & Create workspace
# import the Workspace class and check the azureml SDK version
# exist_ok checks if workspace exists or not.

from azureml.core import Workspace

ws = Workspace.create(name = workspace_name,
                      subscription_id = subscription_id,
                      resource_group = resource_group, 
                      location = workspace_region,
                      exist_ok=True)

# COMMAND ----------

# DBTITLE 1,Workspace details (physical)
#get workspace details
ws.get_details()

# COMMAND ----------

# DBTITLE 1,Write workspace info to config
ws = Workspace(workspace_name = workspace_name,
               subscription_id = subscription_id,
               resource_group = resource_group)

# persist the subscription id, resource group name, and workspace name in aml_config/config.json.
ws.write_config()

#if you want to use a different name
#write_config(path="/databricks/driver/aml_config/",file_name=<alias_conf.cfg>)

# COMMAND ----------

# DBTITLE 1,Use this in any of your notebook
# import the Workspace class and check the azureml SDK version
from azureml.core import Workspace

ws = Workspace.from_config()

#if you use a different file name
#ws = Workspace.from_config(<full path>)

print('Workspace name: ' + ws.name, 
      'Azure region: ' + ws.location, 
      'Subscription id: ' + ws.subscription_id, 
      'Resource group: ' + ws.resource_group, sep = '\n')

# COMMAND ----------

