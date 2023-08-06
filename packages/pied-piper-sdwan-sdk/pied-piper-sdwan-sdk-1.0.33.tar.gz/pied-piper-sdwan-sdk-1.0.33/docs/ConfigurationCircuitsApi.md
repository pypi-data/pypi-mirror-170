# openapi_client.ConfigurationCircuitsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_circuit**](ConfigurationCircuitsApi.md#create_circuit) | **POST** /networkdesign/circuit | 
[**delete_circuit**](ConfigurationCircuitsApi.md#delete_circuit) | **DELETE** /networkdesign/circuit/{id} | 
[**edit_circuit**](ConfigurationCircuitsApi.md#edit_circuit) | **PUT** /networkdesign/circuit/{id} | 
[**get_circuits**](ConfigurationCircuitsApi.md#get_circuits) | **GET** /networkdesign/circuit | 


# **create_circuit**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_circuit()



Create network circuits

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_circuits_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_circuits_api.ConfigurationCircuitsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Network circuit (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_circuit(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCircuitsApi->create_circuit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Network circuit | [optional]

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

# **delete_circuit**
> delete_circuit(id)



Delete network circuits

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_circuits_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_circuits_api.ConfigurationCircuitsApi(api_client)
    id = "id_example" # str | Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_circuit(id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCircuitsApi->delete_circuit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id |

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

# **edit_circuit**
> edit_circuit(id)



Edit network circuits

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_circuits_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_circuits_api.ConfigurationCircuitsApi(api_client)
    id = "id_example" # str | Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Network circuit (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.edit_circuit(id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCircuitsApi->edit_circuit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_circuit(id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCircuitsApi->edit_circuit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Network circuit | [optional]

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

# **get_circuits**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_circuits()



Get network circuits

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_circuits_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_circuits_api.ConfigurationCircuitsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_circuits()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCircuitsApi->get_circuits: %s\n" % e)
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

