# openapi_client.MDPPolicyManagementApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_mdp_policies**](MDPPolicyManagementApi.md#retrieve_mdp_policies) | **GET** /mdp/policies/{nmsId} | 
[**update_policy_status**](MDPPolicyManagementApi.md#update_policy_status) | **PUT** /mdp/policies/{nmsId} | 


# **retrieve_mdp_policies**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] retrieve_mdp_policies(nms_id)



Retrieve MDP policies

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_policy_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_policy_management_api.MDPPolicyManagementApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_mdp_policies(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPPolicyManagementApi->retrieve_mdp_policies: %s\n" % e)
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

# **update_policy_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_policy_status(nms_id)



update policy status

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_policy_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_policy_management_api.MDPPolicyManagementApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | policyList (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_policy_status(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPPolicyManagementApi->update_policy_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_policy_status(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPPolicyManagementApi->update_policy_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| policyList | [optional]

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

