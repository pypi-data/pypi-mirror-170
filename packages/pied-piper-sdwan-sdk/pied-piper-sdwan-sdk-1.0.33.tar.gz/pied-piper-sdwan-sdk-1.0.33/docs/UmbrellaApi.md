# openapi_client.UmbrellaApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_keys_from_umbrella**](UmbrellaApi.md#get_all_keys_from_umbrella) | **GET** /umbrella/getkeys | 
[**get_management_keys_from_umbrella**](UmbrellaApi.md#get_management_keys_from_umbrella) | **GET** /umbrella/getkeys/management | 
[**get_network_keys_from_umbrella**](UmbrellaApi.md#get_network_keys_from_umbrella) | **GET** /umbrella/getkeys/networkdevices | 
[**get_reporting_keys_from_umbrella**](UmbrellaApi.md#get_reporting_keys_from_umbrella) | **GET** /umbrella/getkeys/reporting | 


# **get_all_keys_from_umbrella**
> get_all_keys_from_umbrella()



Get keys from Umbrella

### Example


```python
import time
import openapi_client
from openapi_client.api import umbrella_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = umbrella_api.UmbrellaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_all_keys_from_umbrella()
    except openapi_client.ApiException as e:
        print("Exception when calling UmbrellaApi->get_all_keys_from_umbrella: %s\n" % e)
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

# **get_management_keys_from_umbrella**
> get_management_keys_from_umbrella()



Get management keys from Umbrella

### Example


```python
import time
import openapi_client
from openapi_client.api import umbrella_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = umbrella_api.UmbrellaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_management_keys_from_umbrella()
    except openapi_client.ApiException as e:
        print("Exception when calling UmbrellaApi->get_management_keys_from_umbrella: %s\n" % e)
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

# **get_network_keys_from_umbrella**
> get_network_keys_from_umbrella()



Get network devices keys from Umbrella

### Example


```python
import time
import openapi_client
from openapi_client.api import umbrella_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = umbrella_api.UmbrellaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_network_keys_from_umbrella()
    except openapi_client.ApiException as e:
        print("Exception when calling UmbrellaApi->get_network_keys_from_umbrella: %s\n" % e)
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

# **get_reporting_keys_from_umbrella**
> get_reporting_keys_from_umbrella()



Get reporting keys from Umbrella

### Example


```python
import time
import openapi_client
from openapi_client.api import umbrella_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = umbrella_api.UmbrellaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_reporting_keys_from_umbrella()
    except openapi_client.ApiException as e:
        print("Exception when calling UmbrellaApi->get_reporting_keys_from_umbrella: %s\n" % e)
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

