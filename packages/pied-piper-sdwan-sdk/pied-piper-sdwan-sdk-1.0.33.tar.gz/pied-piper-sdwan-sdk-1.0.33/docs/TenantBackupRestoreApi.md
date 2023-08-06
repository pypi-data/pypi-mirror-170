# openapi_client.TenantBackupRestoreApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tenant_backup**](TenantBackupRestoreApi.md#delete_tenant_backup) | **DELETE** /tenantbackup/delete | 
[**download_existing_backup_file**](TenantBackupRestoreApi.md#download_existing_backup_file) | **GET** /tenantbackup/download/{path} | 
[**export_tenant_backup**](TenantBackupRestoreApi.md#export_tenant_backup) | **GET** /tenantbackup/export | 
[**import_tenant_backup**](TenantBackupRestoreApi.md#import_tenant_backup) | **POST** /tenantbackup/import | 
[**list_tenant_backup**](TenantBackupRestoreApi.md#list_tenant_backup) | **GET** /tenantbackup/list | 


# **delete_tenant_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_tenant_backup(file_name)



Delete all or a specific backup file stored in vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_backup_restore_api.TenantBackupRestoreApi(api_client)
    file_name = "fileName_example" # str | File name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_tenant_backup(file_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantBackupRestoreApi->delete_tenant_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name |

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

# **download_existing_backup_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} download_existing_backup_file(path)



Download a Backup File that is already stored in vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_backup_restore_api.TenantBackupRestoreApi(api_client)
    path = "path_example" # str | File path

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.download_existing_backup_file(path)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantBackupRestoreApi->download_existing_backup_file: %s\n" % e)
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

# **export_tenant_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} export_tenant_backup()



Trigger a backup of configuration database and store it in vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_backup_restore_api.TenantBackupRestoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.export_tenant_backup()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantBackupRestoreApi->export_tenant_backup: %s\n" % e)
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

# **import_tenant_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} import_tenant_backup()



Submit a previously backed up file and import the data and apply it to the configuraion database<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_backup_restore_api.TenantBackupRestoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.import_tenant_backup()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantBackupRestoreApi->import_tenant_backup: %s\n" % e)
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

# **list_tenant_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_tenant_backup()



List all backup files of a tenant stored in vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import tenant_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenant_backup_restore_api.TenantBackupRestoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_tenant_backup()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantBackupRestoreApi->list_tenant_backup: %s\n" % e)
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

