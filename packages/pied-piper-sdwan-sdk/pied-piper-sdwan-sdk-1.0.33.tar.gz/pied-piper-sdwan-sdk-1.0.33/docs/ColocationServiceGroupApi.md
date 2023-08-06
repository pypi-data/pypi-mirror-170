# openapi_client.ColocationServiceGroupApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_group_cluster**](ColocationServiceGroupApi.md#create_service_group_cluster) | **POST** /colocation/servicegroup | 
[**delete_service_group_cluster**](ColocationServiceGroupApi.md#delete_service_group_cluster) | **DELETE** /colocation/servicegroup/{name} | 
[**get_available_chains**](ColocationServiceGroupApi.md#get_available_chains) | **GET** /colocation/servicegroup/servicechains | 
[**get_default_chain**](ColocationServiceGroupApi.md#get_default_chain) | **GET** /colocation/servicegroup/servicechain/default | 
[**get_service_chain**](ColocationServiceGroupApi.md#get_service_chain) | **GET** /colocation/servicegroup | 
[**get_service_group_in_cluster**](ColocationServiceGroupApi.md#get_service_group_in_cluster) | **GET** /colocation/servicegroup/attached | 
[**update_service_group_cluster**](ColocationServiceGroupApi.md#update_service_group_cluster) | **PUT** /colocation/servicegroup | 


# **create_service_group_cluster**
> create_service_group_cluster()



Add new service group

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_group_api.ColocationServiceGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Service group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_service_group_cluster(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceGroupApi->create_service_group_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Service group | [optional]

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

# **delete_service_group_cluster**
> delete_service_group_cluster(name)



Delete service group

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_group_api.ColocationServiceGroupApi(api_client)
    name = "name_example" # str | Service group name

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_service_group_cluster(name)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceGroupApi->delete_service_group_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service group name |

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

# **get_available_chains**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_available_chains()



Get all service chains

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_group_api.ColocationServiceGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_available_chains()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceGroupApi->get_available_chains: %s\n" % e)
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

# **get_default_chain**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_default_chain()



Get default service chains

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_group_api.ColocationServiceGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_default_chain()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceGroupApi->get_default_chain: %s\n" % e)
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

# **get_service_chain**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_service_chain(service_group_name)



Get service chain by name

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_group_api.ColocationServiceGroupApi(api_client)
    service_group_name = "serviceGroupName_example" # str | Service group name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_service_chain(service_group_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceGroupApi->get_service_chain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_group_name** | **str**| Service group name |

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

# **get_service_group_in_cluster**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_service_group_in_cluster()



Get service chains in cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_group_api.ColocationServiceGroupApi(api_client)
    cluster_id = "ClusterId_example" # str | Cluster Id (optional)
    user_group_name = "UserGroupName_example" # str | UserGroup Name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_service_group_in_cluster(cluster_id=cluster_id, user_group_name=user_group_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceGroupApi->get_service_group_in_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id | [optional]
 **user_group_name** | **str**| UserGroup Name | [optional]

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

# **update_service_group_cluster**
> update_service_group_cluster()



Update service group

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_group_api.ColocationServiceGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Service group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_service_group_cluster(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceGroupApi->update_service_group_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Service group | [optional]

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

