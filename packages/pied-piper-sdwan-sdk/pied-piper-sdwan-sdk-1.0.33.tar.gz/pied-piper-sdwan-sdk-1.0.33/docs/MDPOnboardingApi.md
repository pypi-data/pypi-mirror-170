# openapi_client.MDPOnboardingApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mdp_onboarding_status**](MDPOnboardingApi.md#get_mdp_onboarding_status) | **GET** /mdp/onboard/status | 
[**onboard_mdp**](MDPOnboardingApi.md#onboard_mdp) | **POST** /mdp/onboard | 
[**update_onboarding_payload**](MDPOnboardingApi.md#update_onboarding_payload) | **PUT** /mdp/onboard/{nmsId} | 


# **get_mdp_onboarding_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_mdp_onboarding_status()



Get MDP onboarding status

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_onboarding_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_onboarding_api.MDPOnboardingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_mdp_onboarding_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPOnboardingApi->get_mdp_onboarding_status: %s\n" % e)
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

# **onboard_mdp**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} onboard_mdp()



Start MDP onboarding operation

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_onboarding_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_onboarding_api.MDPOnboardingApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Onboard (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.onboard_mdp(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPOnboardingApi->onboard_mdp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Onboard | [optional]

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

# **update_onboarding_payload**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_onboarding_payload(nms_id)



update MDP onboarding document

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_onboarding_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_onboarding_api.MDPOnboardingApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Onboard (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_onboarding_payload(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPOnboardingApi->update_onboarding_payload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_onboarding_payload(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPOnboardingApi->update_onboarding_payload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Onboard | [optional]

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

