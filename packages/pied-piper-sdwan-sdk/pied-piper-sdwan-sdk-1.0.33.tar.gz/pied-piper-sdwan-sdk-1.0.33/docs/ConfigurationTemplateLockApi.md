# openapi_client.ConfigurationTemplateLockApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_lock**](ConfigurationTemplateLockApi.md#remove_lock) | **DELETE** /template/lock/{processId} | 
[**update_lease_time**](ConfigurationTemplateLockApi.md#update_lease_time) | **PUT** /template/lock/{processId} | 


# **remove_lock**
> remove_lock(process_id)



Remove lock

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_lock_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_lock_api.ConfigurationTemplateLockApi(api_client)
    process_id = "processId_example" # str | Process Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_lock(process_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateLockApi->remove_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| Process Id |

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

# **update_lease_time**
> update_lease_time(process_id)



Update lease

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_lock_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_lock_api.ConfigurationTemplateLockApi(api_client)
    process_id = "processId_example" # str | Process Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_lease_time(process_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateLockApi->update_lease_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| Process Id |

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

