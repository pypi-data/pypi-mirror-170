# openapi_client.SystemContainerApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_container**](SystemContainerApi.md#activate_container) | **POST** /sdavc/task/{taskId} | 
[**activate_container_on_remote_host**](SystemContainerApi.md#activate_container_on_remote_host) | **POST** /container-manager/activate/{containerName} | 
[**de_activate_container**](SystemContainerApi.md#de_activate_container) | **POST** /container-manager/deactivate/{containerName} | 
[**does_valid_image_exist**](SystemContainerApi.md#does_valid_image_exist) | **GET** /container-manager/doesValidImageExist/{containerName} | 
[**get_container_inspect_data**](SystemContainerApi.md#get_container_inspect_data) | **GET** /container-manager/inspect/{containerName} | 
[**get_container_settings**](SystemContainerApi.md#get_container_settings) | **GET** /container-manager/settings/{containerName} | 
[**get_custom_app**](SystemContainerApi.md#get_custom_app) | **GET** /sdavc/customapps | 
[**test_load_balancer**](SystemContainerApi.md#test_load_balancer) | **POST** /sdavc/test | 


# **activate_container**
> activate_container(task_id)



Activate container

### Example


```python
import time
import openapi_client
from openapi_client.api import system_container_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_container_api.SystemContainerApi(api_client)
    task_id = "taskId_example" # str | Task Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Container task config (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.activate_container(task_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->activate_container: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.activate_container(task_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->activate_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Task Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Container task config | [optional]

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

# **activate_container_on_remote_host**
> activate_container_on_remote_host(container_name)



Activate container on remote host

### Example


```python
import time
import openapi_client
from openapi_client.api import system_container_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_container_api.SystemContainerApi(api_client)
    container_name = "containerName_example" # str | Container name
    url = "url_example" # str | Container image URL (optional)
    host_ip = "hostIp_example" # str | Container host IP (optional)
    checksum = "checksum_example" # str | Container image checksum (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.activate_container_on_remote_host(container_name)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->activate_container_on_remote_host: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.activate_container_on_remote_host(container_name, url=url, host_ip=host_ip, checksum=checksum)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->activate_container_on_remote_host: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_name** | **str**| Container name |
 **url** | **str**| Container image URL | [optional]
 **host_ip** | **str**| Container host IP | [optional]
 **checksum** | **str**| Container image checksum | [optional]

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

# **de_activate_container**
> de_activate_container(container_name)



Deactivate container on remote host

### Example


```python
import time
import openapi_client
from openapi_client.api import system_container_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_container_api.SystemContainerApi(api_client)
    container_name = "containerName_example" # str | Container name
    host_ip = "hostIp_example" # str | Container host IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.de_activate_container(container_name)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->de_activate_container: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.de_activate_container(container_name, host_ip=host_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->de_activate_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_name** | **str**| Container name |
 **host_ip** | **str**| Container host IP | [optional]

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

# **does_valid_image_exist**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} does_valid_image_exist(container_name)



Get container image checksum

### Example


```python
import time
import openapi_client
from openapi_client.api import system_container_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_container_api.SystemContainerApi(api_client)
    container_name = "containerName_example" # str | Container name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.does_valid_image_exist(container_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->does_valid_image_exist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_name** | **str**| Container name |

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

# **get_container_inspect_data**
> str get_container_inspect_data(container_name)



Get container inspect data

### Example


```python
import time
import openapi_client
from openapi_client.api import system_container_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_container_api.SystemContainerApi(api_client)
    container_name = "containerName_example" # str | Container name
    host_ip = "hostIp_example" # str | Container host IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_container_inspect_data(container_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->get_container_inspect_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_container_inspect_data(container_name, host_ip=host_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->get_container_inspect_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_name** | **str**| Container name |
 **host_ip** | **str**| Container host IP | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_container_settings(container_name)



Get container settings

### Example


```python
import time
import openapi_client
from openapi_client.api import system_container_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_container_api.SystemContainerApi(api_client)
    container_name = "containerName_example" # str | Container name
    host_ip = "hostIp_example" # str | Container host IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_container_settings(container_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->get_container_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_container_settings(container_name, host_ip=host_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->get_container_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_name** | **str**| Container name |
 **host_ip** | **str**| Container host IP | [optional]

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

# **get_custom_app**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_custom_app()



Displays the user-defined applications

### Example


```python
import time
import openapi_client
from openapi_client.api import system_container_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_container_api.SystemContainerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_custom_app()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->get_custom_app: %s\n" % e)
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

# **test_load_balancer**
> test_load_balancer()



Test SD_AVC load balancer

### Example


```python
import time
import openapi_client
from openapi_client.api import system_container_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_container_api.SystemContainerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.test_load_balancer()
    except openapi_client.ApiException as e:
        print("Exception when calling SystemContainerApi->test_load_balancer: %s\n" % e)
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

