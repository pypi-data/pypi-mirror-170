# openapi_client.MDPConfigObjectApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_mdp_config_object**](MDPConfigObjectApi.md#retrieve_mdp_config_object) | **GET** /mdp/policies/mdpconfig/{deviceId} | 


# **retrieve_mdp_config_object**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] retrieve_mdp_config_object(device_id)



Retrieve MDP ConfigObject

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_config_object_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_config_object_api.MDPConfigObjectApi(api_client)
    device_id = "deviceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_mdp_config_object(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPConfigObjectApi->retrieve_mdp_config_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  |

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

