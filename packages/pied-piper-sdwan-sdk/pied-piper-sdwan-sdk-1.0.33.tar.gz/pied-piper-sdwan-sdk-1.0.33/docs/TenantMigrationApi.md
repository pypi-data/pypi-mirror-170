# openapi_client.TenantMigrationApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_tenant_data**](TenantMigrationApi.md#download_tenant_data) | **GET** /tenantmigration/download/{path} | 
[**export_tenant_data**](TenantMigrationApi.md#export_tenant_data) | **POST** /tenantmigration/export | 
[**get_migration_token**](TenantMigrationApi.md#get_migration_token) | **GET** /tenantmigration/migrationToken | 
[**import_tenant_data**](TenantMigrationApi.md#import_tenant_data) | **POST** /tenantmigration/import | 
[**migrate_network**](TenantMigrationApi.md#migrate_network) | **POST** /tenantmigration/networkMigration | 
[**re_trigger_network_migration**](TenantMigrationApi.md#re_trigger_network_migration) | **GET** /tenantmigration/networkMigration | 


# **download_tenant_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} download_tenant_data(path)



Download tenant data

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_migration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_migration_api.TenantMigrationApi(api_client)
    path = "path_example" # str | File path

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.download_tenant_data(path)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantMigrationApi->download_tenant_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_tenant_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} export_tenant_data()



Export tenant data

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_migration_api
from openapi_client.model.create_tenant_model import CreateTenantModel
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_migration_api.TenantMigrationApi(api_client)
    create_tenant_model = CreateTenantModel(
        desc="desc_example",
        getv_bond_address="getv_bond_address_example",
        idp_metadata="idp_metadata_example",
        mode="mode_example",
        name="name_example",
        old_idp_metadata="old_idp_metadata_example",
        org_name="org_name_example",
        sp_metadata="sp_metadata_example",
        sub_domain="sub_domain_example",
        wan_edge_forecast="wan_edge_forecast_example",
    ) # CreateTenantModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.export_tenant_data(create_tenant_model=create_tenant_model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantMigrationApi->export_tenant_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_model** | [**CreateTenantModel**](CreateTenantModel.md)|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_token**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_migration_token(migration_id)



Get migration token

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_migration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_migration_api.TenantMigrationApi(api_client)
    migration_id = "migrationId_example" # str | Migration Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_migration_token(migration_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantMigrationApi->get_migration_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **str**| Migration Id |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_tenant_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} import_tenant_data()



Import tenant data

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_migration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_migration_api.TenantMigrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.import_tenant_data()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantMigrationApi->import_tenant_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_network**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} migrate_network()



Migrate network

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_migration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_migration_api.TenantMigrationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Network migration (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.migrate_network(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantMigrationApi->migrate_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Network migration | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_trigger_network_migration**
> re_trigger_network_migration()



Re-trigger network migration

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_migration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_migration_api.TenantMigrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.re_trigger_network_migration()
    except openapi_client.ApiException as e:
        print("Exception when calling TenantMigrationApi->re_trigger_network_migration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

