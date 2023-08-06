# openapi_client.ConfigurationPolicySecureInternetGatewayDataCentersBuilderApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sig_data_center_list**](ConfigurationPolicySecureInternetGatewayDataCentersBuilderApi.md#get_sig_data_center_list) | **GET** /sig/datacenters/{type} | 


# **get_sig_data_center_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sig_data_center_list(type)



Get list of data centers for zscaler or umbrella

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_secure_internet_gateway_data_centers_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_secure_internet_gateway_data_centers_builder_api.ConfigurationPolicySecureInternetGatewayDataCentersBuilderApi(api_client)
    type = "type_example" # str | Provider type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sig_data_center_list(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicySecureInternetGatewayDataCentersBuilderApi->get_sig_data_center_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Provider type |

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

