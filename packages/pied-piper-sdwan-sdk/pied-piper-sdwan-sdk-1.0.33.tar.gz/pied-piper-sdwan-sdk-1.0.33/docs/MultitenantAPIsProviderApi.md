# openapi_client.MultitenantAPIsProviderApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](MultitenantAPIsProviderApi.md#create_tenant) | **POST** /tenant | 
[**create_tenant_async**](MultitenantAPIsProviderApi.md#create_tenant_async) | **POST** /tenant/async | 
[**create_tenant_async_bulk**](MultitenantAPIsProviderApi.md#create_tenant_async_bulk) | **POST** /tenant/bulk/async | 
[**delete_tenant**](MultitenantAPIsProviderApi.md#delete_tenant) | **POST** /tenant/{tenantId}/delete | 
[**delete_tenant_async_bulk**](MultitenantAPIsProviderApi.md#delete_tenant_async_bulk) | **DELETE** /tenant/bulk/async | 
[**delete_tenant_backup**](MultitenantAPIsProviderApi.md#delete_tenant_backup) | **DELETE** /tenantbackup/delete | 
[**download_existing_backup_file**](MultitenantAPIsProviderApi.md#download_existing_backup_file) | **GET** /tenantbackup/download/{path} | 
[**export_tenant_backup**](MultitenantAPIsProviderApi.md#export_tenant_backup) | **GET** /tenantbackup/export | 
[**force_status_collection**](MultitenantAPIsProviderApi.md#force_status_collection) | **POST** /tenantstatus/force | 
[**get_all_tenant_statuses**](MultitenantAPIsProviderApi.md#get_all_tenant_statuses) | **GET** /tenantstatus | 
[**get_all_tenants**](MultitenantAPIsProviderApi.md#get_all_tenants) | **GET** /tenant | 
[**get_tenant**](MultitenantAPIsProviderApi.md#get_tenant) | **GET** /tenant/{tenantId} | 
[**get_tenant_hosting_capacity_onv_smarts**](MultitenantAPIsProviderApi.md#get_tenant_hosting_capacity_onv_smarts) | **GET** /tenant/vsmart/capacity | 
[**get_tenantv_smart_mapping**](MultitenantAPIsProviderApi.md#get_tenantv_smart_mapping) | **GET** /tenant/vsmart | 
[**import_tenant_backup**](MultitenantAPIsProviderApi.md#import_tenant_backup) | **POST** /tenantbackup/import | 
[**list_tenant_backup**](MultitenantAPIsProviderApi.md#list_tenant_backup) | **GET** /tenantbackup/list | 
[**switch_tenant**](MultitenantAPIsProviderApi.md#switch_tenant) | **POST** /tenant/{tenantId}/switch | 
[**tenantv_smart_mt_migrate**](MultitenantAPIsProviderApi.md#tenantv_smart_mt_migrate) | **POST** /tenant/vsmart-mt/migrate | 
[**update_tenant**](MultitenantAPIsProviderApi.md#update_tenant) | **PUT** /tenant/{tenantId} | 
[**v_session_id**](MultitenantAPIsProviderApi.md#v_session_id) | **POST** /tenant/{tenantId}/vsessionid | 


# **create_tenant**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_tenant()



Create a new tenant in Multi-Tenant vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Tenant model (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_tenant(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->create_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Tenant model | [optional]

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

# **create_tenant_async**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_tenant_async()



Create a new tenant in Multi-Tenant vManage asynchronously<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Tenant model (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_tenant_async(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->create_tenant_async: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Tenant model | [optional]

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

# **create_tenant_async_bulk**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_tenant_async_bulk()



Create multiple tenants on vManage asynchronously<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Tenant model (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_tenant_async_bulk(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->create_tenant_async_bulk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Tenant model | [optional]

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

# **delete_tenant**
> delete_tenant(tenant_id)



Delete a tenant by Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    tenant_id = "tenantId_example" # str | Tenant Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Tenant model (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tenant(tenant_id)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->delete_tenant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_tenant(tenant_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->delete_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Tenant model | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant_async_bulk**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_tenant_async_bulk()



Delete multiple tenants on vManage asynchronously<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Tenant model (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_tenant_async_bulk(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->delete_tenant_async_bulk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Tenant model | [optional]

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

# **delete_tenant_backup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_tenant_backup(file_name)



Delete all or a specific backup file stored in vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    file_name = "fileName_example" # str | File name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_tenant_backup(file_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->delete_tenant_backup: %s\n" % e)
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
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    path = "path_example" # str | File path

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.download_existing_backup_file(path)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->download_existing_backup_file: %s\n" % e)
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
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.export_tenant_backup()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->export_tenant_backup: %s\n" % e)
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

# **force_status_collection**
> force_status_collection()



Force tenant status collection<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.force_status_collection()
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->force_status_collection: %s\n" % e)
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

# **get_all_tenant_statuses**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_all_tenant_statuses()



List all tenant status<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_all_tenant_statuses()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->get_all_tenant_statuses: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_all_tenants**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_all_tenants()



Lists all the tenants on the vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    device_id = "deviceId_example" # str | List all tenants associated with a vSmart (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_tenants(device_id=device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->get_all_tenants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| List all tenants associated with a vSmart | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_tenant**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_tenant(tenant_id)



Get a tenant by Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    tenant_id = "tenantId_example" # str | Tenant Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tenant(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->get_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant Id |

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

# **get_tenant_hosting_capacity_onv_smarts**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_tenant_hosting_capacity_onv_smarts()



Lists all the vsmarts on the vManage and its tenant hosting capacity<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_tenant_hosting_capacity_onv_smarts()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->get_tenant_hosting_capacity_onv_smarts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_tenantv_smart_mapping**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_tenantv_smart_mapping()



Retrieve mapping of tenants to vSmarts<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_tenantv_smart_mapping()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->get_tenantv_smart_mapping: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.import_tenant_backup()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->import_tenant_backup: %s\n" % e)
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
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_tenant_backup()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->list_tenant_backup: %s\n" % e)
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

# **switch_tenant**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} switch_tenant(tenant_id)



Switch to a specific tenant<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    tenant_id = "tenantId_example" # str | Tenant Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.switch_tenant(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->switch_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant Id |

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

# **tenantv_smart_mt_migrate**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] tenantv_smart_mt_migrate()



Migrate tenants from single tenant vSmarts to multi-tenant capable vSmarts<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.tenantv_smart_mt_migrate()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->tenantv_smart_mt_migrate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **update_tenant**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_tenant(tenant_id)



Update a tenant in Multi-Tenant vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    tenant_id = "tenantId_example" # str | Tenant Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Tenant model (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_tenant(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->update_tenant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_tenant(tenant_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->update_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Tenant model | [optional]

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

# **v_session_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v_session_id(tenant_id)



Get VSessionId for a specific tenant<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import multitenant_apis_provider_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multitenant_apis_provider_api.MultitenantAPIsProviderApi(api_client)
    tenant_id = "tenantId_example" # str | Tenant Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.v_session_id(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenantAPIsProviderApi->v_session_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant Id |

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

