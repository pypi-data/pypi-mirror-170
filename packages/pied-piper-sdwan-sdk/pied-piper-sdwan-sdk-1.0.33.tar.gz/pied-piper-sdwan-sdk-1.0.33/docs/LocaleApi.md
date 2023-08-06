# openapi_client.LocaleApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supported_locales**](LocaleApi.md#get_supported_locales) | **GET** /localization/supportedLocales | 


# **get_supported_locales**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_supported_locales()



Get Supported locales

### Example


```python
import time
import openapi_client
from openapi_client.api import locale_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = locale_api.LocaleApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_supported_locales()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocaleApi->get_supported_locales: %s\n" % e)
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

