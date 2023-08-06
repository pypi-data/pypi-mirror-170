# openapi_client.UtilitySecurityApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_given_ip_list**](UtilitySecurityApi.md#check_given_ip_list) | **POST** /software/compliance/ip/origin/check | 


# **check_given_ip_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] check_given_ip_list()



Block IP based on list

### Example


```python
import time
import openapi_client
from openapi_client.api import utility_security_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utility_security_api.UtilitySecurityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device detail (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.check_given_ip_list(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UtilitySecurityApi->check_given_ip_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device detail | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

