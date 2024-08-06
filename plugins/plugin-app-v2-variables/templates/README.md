## StackSpot Plugin

## Jinja

You can use jinja to make a template-data folder more dynamic.

complete documentation of jinja: https://jinja.palletsprojects.com/en/3.0.x/templates/

### Example Inputs:
- Resource: {{ resource }}
- Method: {{ method }}

### Variables V1
stk_project_name:  {{ stk_project_name }}
stk_stack: {{ stk_stack }}
stk_studio: {{ stk_studio }}
stk_workspace: {{ stk_workspace }}
stk_manifest_type: {{ stk_manifest_type }}
stk_plugin_type: {{ stk_plugin_type }}
stk_plugin_name: {{ stk_plugin_name }}
stk_plugin_version: {{ stk_plugin_version }}
stk_plugin_qualifier: {{ stk_plugin_qualifier }}
stk_account_name: {{ stk_account_name }}
stk_username: {{ stk_username }}
stk_email: {{ stk_email }}

### Variables V2
var.STK_PROJECT_NAME: {{ var.STK_PROJECT_NAME }}
var.STK_STACK: {{ var.STK_STACK }}
var.STK_STUDIO: {{ var.STK_STUDIO }}
var.STK_WORKSPACE: {{ var.STK_WORKSPACE }}
var.STK_MANIFEST_TYPE: {{ var.STK_MANIFEST_TYPE }}
var.STK_PLUGIN_TYPE: {{ var.STK_PLUGIN_TYPE }}
var.STK_PLUGIN_NAME: {{ var.STK_PLUGIN_NAME }}
var.STK_PLUGIN_VERSION: {{ var.STK_PLUGIN_VERSION }}
var.STK_PLUGIN_QUALIFIER: {{ var.STK_PLUGIN_QUALIFIER }}
var.STK_ACCOUNT_NAME: {{ var.STK_ACCOUNT_NAME }}
var.STK_USERNAME: {{ var.STK_USERNAME }}
var.STK_EMAIL: {{ var.STK_EMAIL }}

### Cloud Variables
STK_CLOUD_ACCOUNT_PROVIDER_DEVELOPMENT: {{ var.STK_CLOUD_ACCOUNT_PROVIDER_DEVELOPMENT }}
STK_CLOUD_ACCOUNT_ID_DEVELOPMENT: {{ var.STK_CLOUD_ACCOUNT_ID_DEVELOPMENT }}
STK_CLOUD_ACCOUNT_PROVIDER_PRODUCTION: {{ var.STK_CLOUD_ACCOUNT_PROVIDER_PRODUCTION }}
STK_CLOUD_ACCOUNT_ID_PRODUCTION: {{ var.STK_CLOUD_ACCOUNT_ID_PRODUCTION }}
STK_CLOUD_ACCOUNT_PROVIDER_STAGING: {{ var.STK_CLOUD_ACCOUNT_PROVIDER_STAGING }}
STK_CLOUD_ACCOUNT_ID_STAGING: {{ var.STK_CLOUD_ACCOUNT_ID_STAGING }}

### Custom Variables
var.EMAIL_OWNER_WS: {{ var.EMAIL_OWNER_WS }}
var.SIGLA: {{ var.SIGLA }}

