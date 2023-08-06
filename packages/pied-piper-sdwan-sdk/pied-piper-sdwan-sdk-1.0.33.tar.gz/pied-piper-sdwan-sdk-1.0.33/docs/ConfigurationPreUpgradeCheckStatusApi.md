# openapi_client.ConfigurationPreUpgradeCheckStatusApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_pre_upgrade_check_status**](ConfigurationPreUpgradeCheckStatusApi.md#update_pre_upgrade_check_status) | **PUT** /device/action/status/preupgrade/check | 


# **update_pre_upgrade_check_status**
> update_pre_upgrade_check_status()



Update pre upgrade check status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_pre_upgrade_check_status_api
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request import GetO365PreferredPathFromVAnalyticsRequest
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_pre_upgrade_check_status_api.ConfigurationPreUpgradeCheckStatusApi(api_client)
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_pre_upgrade_check_status(get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPreUpgradeCheckStatusApi->update_pre_upgrade_check_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

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

