# openapi_client.ScheduledBackupRestoreApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_schduled_backup**](ScheduledBackupRestoreApi.md#delete_schduled_backup) | **DELETE** /backup/backupinfo | 
[**delete_schedule**](ScheduledBackupRestoreApi.md#delete_schedule) | **DELETE** /schedule/{schedulerId} | 
[**download_backup_file**](ScheduledBackupRestoreApi.md#download_backup_file) | **GET** /backup/download/{path} | 
[**export_backup**](ScheduledBackupRestoreApi.md#export_backup) | **POST** /backup/export | 
[**get_local_backup_info**](ScheduledBackupRestoreApi.md#get_local_backup_info) | **GET** /backup/backupinfo/{localBackupInfoId} | 
[**get_schedule_record_for_backup**](ScheduledBackupRestoreApi.md#get_schedule_record_for_backup) | **GET** /schedule/{schedulerId} | 
[**import_scheduled_backup**](ScheduledBackupRestoreApi.md#import_scheduled_backup) | **POST** /restore/import | 
[**list_backup**](ScheduledBackupRestoreApi.md#list_backup) | **GET** /backup/list | 
[**list_schedules**](ScheduledBackupRestoreApi.md#list_schedules) | **GET** /schedule/list | 
[**remote_import_backup**](ScheduledBackupRestoreApi.md#remote_import_backup) | **POST** /restore/remoteimport | 
[**schedule_backup**](ScheduledBackupRestoreApi.md#schedule_backup) | **POST** /schedule/create | 


# **delete_schduled_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_schduled_backup()



Delete all or a specific backup file stored in vManage

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    task_id = "taskId_example" # str | task id (optional)
    backup_info_id = "backupInfoId_example" # str | Local Backup Info Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_schduled_backup(task_id=task_id, backup_info_id=backup_info_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->delete_schduled_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| task id | [optional]
 **backup_info_id** | **str**| Local Backup Info Id | [optional]

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

# **delete_schedule**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_schedule(scheduler_id)



Delete a schedule record for backup in vManage by scheduler id

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    scheduler_id = "schedulerId_example" # str | scheduler id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_schedule(scheduler_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->delete_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduler_id** | **str**| scheduler id |

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

# **download_backup_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} download_backup_file(path)



Download a Backup File that is already stored in vManage

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    path = "path_example" # str | File path

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.download_backup_file(path)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->download_backup_file: %s\n" % e)
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

# **export_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} export_backup()



Trigger a backup of configuration database and statstics database and store it in vManage

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | backup request information (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.export_backup(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->export_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| backup request information | [optional]

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

# **get_local_backup_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_local_backup_info(local_backup_info_id)



Get a localBackupInfo record by localBackupInfoId

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    local_backup_info_id = "localBackupInfoId_example" # str | localBackupInfo Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_local_backup_info(local_backup_info_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->get_local_backup_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_backup_info_id** | **str**| localBackupInfo Id |

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

# **get_schedule_record_for_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_schedule_record_for_backup(scheduler_id)



Get a schedule record for backup by scheduler id

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    scheduler_id = "schedulerId_example" # str | scheduler id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_schedule_record_for_backup(scheduler_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->get_schedule_record_for_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduler_id** | **str**| scheduler id |

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

# **import_scheduled_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} import_scheduled_backup()



Submit a previously backed up file and import the data and apply it to the configuraion database

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.import_scheduled_backup()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->import_scheduled_backup: %s\n" % e)
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

# **list_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_backup()



List all backup files of a tenant stored in vManage

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    size = "size_example" # str | size (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_backup(size=size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->list_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **str**| size | [optional]

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

# **list_schedules**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_schedules()



Get a schedule record for backup by scheduler id

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    limit = 100 # int | size (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_schedules(limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->list_schedules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| size | [optional] if omitted the server will use the default value of 100

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

# **remote_import_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} remote_import_backup()



Remote import backup from a remote URL and import the data and apply it to the configuraion database

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.remote_import_backup(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->remote_import_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **schedule_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} schedule_backup()



create  backup scheduler config-db and statstics database with startDateTime and persist to config-db

### Example


```python
import time
import openapi_client
from openapi_client.api import scheduled_backup_restore_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_backup_restore_api.ScheduledBackupRestoreApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | schedule request information (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.schedule_backup(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScheduledBackupRestoreApi->schedule_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| schedule request information | [optional]

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

