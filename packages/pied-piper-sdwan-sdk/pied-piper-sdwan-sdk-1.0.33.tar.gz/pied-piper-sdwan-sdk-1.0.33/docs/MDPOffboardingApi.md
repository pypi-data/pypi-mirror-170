# openapi_client.MDPOffboardingApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disconnect_from_mdp**](MDPOffboardingApi.md#disconnect_from_mdp) | **GET** /mdp/disconnect/{nmsId} | 
[**offboard**](MDPOffboardingApi.md#offboard) | **DELETE** /mdp/onboard/{nmsId} | 


# **disconnect_from_mdp**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] disconnect_from_mdp(nms_id)



disconnect from mpd controller

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_offboarding_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_offboarding_api.MDPOffboardingApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.disconnect_from_mdp(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPOffboardingApi->disconnect_from_mdp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |

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

# **offboard**
> offboard(nms_id)



offboard the mdp application

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_offboarding_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_offboarding_api.MDPOffboardingApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.offboard(nms_id)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPOffboardingApi->offboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |

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

