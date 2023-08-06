# openapi_client.ConfigurationPolicyCloudApplicationBuilderApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cloud_discovered_apps**](ConfigurationPolicyCloudApplicationBuilderApi.md#get_cloud_discovered_apps) | **GET** /template/policy/clouddiscoveredapp | 


# **get_cloud_discovered_apps**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cloud_discovered_apps()



Get all cloud discovered applications

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_cloud_application_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_cloud_application_builder_api.ConfigurationPolicyCloudApplicationBuilderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_discovered_apps()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyCloudApplicationBuilderApi->get_cloud_discovered_apps: %s\n" % e)
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

