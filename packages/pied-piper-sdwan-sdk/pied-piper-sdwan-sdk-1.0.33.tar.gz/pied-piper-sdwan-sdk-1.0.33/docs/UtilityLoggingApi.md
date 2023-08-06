# openapi_client.UtilityLoggingApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**debug_log**](UtilityLoggingApi.md#debug_log) | **POST** /util/logging/debuglog | 
[**list_log_file_details**](UtilityLoggingApi.md#list_log_file_details) | **GET** /util/logfile/appserver | 
[**list_loggers**](UtilityLoggingApi.md#list_loggers) | **GET** /util/logging/loggers | 
[**list_v_manage_server_log_last_n_lines**](UtilityLoggingApi.md#list_v_manage_server_log_last_n_lines) | **GET** /util/logfile/appserver/lastnlines | 
[**set_log_level**](UtilityLoggingApi.md#set_log_level) | **POST** /util/logging/level | 


# **debug_log**
> debug_log(logger_name, log_message)



Test whether logging works

### Example


```python
import time
import openapi_client
from openapi_client.api import utility_logging_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utility_logging_api.UtilityLoggingApi(api_client)
    logger_name = "logger_name_example" # str | 
    log_message = "log_message_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.debug_log(logger_name, log_message)
    except openapi_client.ApiException as e:
        print("Exception when calling UtilityLoggingApi->debug_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logger_name** | **str**|  |
 **log_message** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_log_file_details**
> str list_log_file_details()



Lists content of log file. This API accepts content type as text/plain. It is mandatory to provide response content type.  Any other content type would result in empty response.

### Example


```python
import time
import openapi_client
from openapi_client.api import utility_logging_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utility_logging_api.UtilityLoggingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_log_file_details()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UtilityLoggingApi->list_log_file_details: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **list_loggers**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_loggers()



List loggers

### Example


```python
import time
import openapi_client
from openapi_client.api import utility_logging_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utility_logging_api.UtilityLoggingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_loggers()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UtilityLoggingApi->list_loggers: %s\n" % e)
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

# **list_v_manage_server_log_last_n_lines**
> str list_v_manage_server_log_last_n_lines()



List last N lines of log file. This API accepts content type as text/plain. It is mandatory to provide response content type.  Any other content type would result in empty response.

### Example


```python
import time
import openapi_client
from openapi_client.api import utility_logging_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utility_logging_api.UtilityLoggingApi(api_client)
    lines = 100 # int | Number of lines (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_v_manage_server_log_last_n_lines(lines=lines)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UtilityLoggingApi->list_v_manage_server_log_last_n_lines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lines** | **int**| Number of lines | [optional] if omitted the server will use the default value of 100

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

# **set_log_level**
> set_log_level(logger_name, log_level)



Set log level for logger

### Example


```python
import time
import openapi_client
from openapi_client.api import utility_logging_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utility_logging_api.UtilityLoggingApi(api_client)
    logger_name = "logger_name_example" # str | 
    log_level = "log_level_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_log_level(logger_name, log_level)
    except openapi_client.ApiException as e:
        print("Exception when calling UtilityLoggingApi->set_log_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logger_name** | **str**|  |
 **log_level** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

