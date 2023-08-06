# openapi_client.DefaultApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tier**](DefaultApi.md#add_tier) | **POST** /device/tier | 
[**delete_tier**](DefaultApi.md#delete_tier) | **DELETE** /device/tier/{tierName} | 
[**get_o365_preferred_path_from_v_analytics**](DefaultApi.md#get_o365_preferred_path_from_v_analytics) | **POST** /cloudservices/m365/preferredpath | 
[**get_tiers**](DefaultApi.md#get_tiers) | **GET** /device/tier | 
[**update_device_action_status**](DefaultApi.md#update_device_action_status) | **PUT** /device/action/status | 


# **add_tier**
> add_tier(add_tier)



add tier

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    add_tier = "addTier_example" # str | addTier

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_tier(add_tier)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_tier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_tier** | **str**| addTier |

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

# **delete_tier**
> delete_tier(tier_name)



deleteTier

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    tier_name = "tierName_example" # str | deletetier

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tier(tier_name)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_tier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_name** | **str**| deletetier |

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

# **get_o365_preferred_path_from_v_analytics**
> get_o365_preferred_path_from_v_analytics()



Get vAnalytics Preferred Path for Office365 over time. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_o365_preferred_path_from_v_analytics(get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_o365_preferred_path_from_v_analytics: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tiers**
> get_tiers()



getTiers

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_tiers()
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_tiers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **update_device_action_status**
> update_device_action_status()



Update device action status.

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Update device action status (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_device_action_status(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_device_action_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Update device action status | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

