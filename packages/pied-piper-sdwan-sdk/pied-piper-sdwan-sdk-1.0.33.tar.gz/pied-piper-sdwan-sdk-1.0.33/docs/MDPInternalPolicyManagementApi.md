# openapi_client.MDPInternalPolicyManagementApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_internal_policy**](MDPInternalPolicyManagementApi.md#add_internal_policy) | **PUT** /mdp/policies/mdpconfig | 


# **add_internal_policy**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} add_internal_policy()



Add internal policy from vmanage

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_internal_policy_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_internal_policy_management_api.MDPInternalPolicyManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | addInternalPolicy (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_internal_policy(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPInternalPolicyManagementApi->add_internal_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| addInternalPolicy | [optional]

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

