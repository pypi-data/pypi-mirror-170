# openapi_client.PartnerWCMConfigsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**push_netconf_configs**](PartnerWCMConfigsApi.md#push_netconf_configs) | **POST** /partner/wcm/netconf/{nmsId} | 


# **push_netconf_configs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} push_netconf_configs(nms_id)



Push device configs

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_wcm_configs_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_wcm_configs_api.PartnerWCMConfigsApi(api_client)
    nms_id = "nmsId_example" # str | NMS Id
    request_body = [] # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] | Netconf configuration (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.push_netconf_configs(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerWCMConfigsApi->push_netconf_configs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.push_netconf_configs(nms_id, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerWCMConfigsApi->push_netconf_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**| NMS Id |
 **request_body** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**| Netconf configuration | [optional]

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

