# openapi_client.SDAVCCloudConnectorApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_cloud_connector**](SDAVCCloudConnectorApi.md#disable_cloud_connector) | **PUT** /sdavc/cloudconnector | 
[**enable_cloud_connector**](SDAVCCloudConnectorApi.md#enable_cloud_connector) | **POST** /sdavc/cloudconnector | 
[**get_cloud_connector**](SDAVCCloudConnectorApi.md#get_cloud_connector) | **GET** /sdavc/cloudconnector | 
[**get_cloud_connector_status**](SDAVCCloudConnectorApi.md#get_cloud_connector_status) | **GET** /sdavc/cloudconnector/status | 


# **disable_cloud_connector**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} disable_cloud_connector()



Disable SD_AVC Cloud Connector

### Example


```python
import time
import openapi_client
from openapi_client.api import sdavc_cloud_connector_api
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
    api_instance = sdavc_cloud_connector_api.SDAVCCloudConnectorApi(api_client)
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.disable_cloud_connector(get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDAVCCloudConnectorApi->disable_cloud_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

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

# **enable_cloud_connector**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} enable_cloud_connector()



Enable SD_AVC Cloud Connector

### Example


```python
import time
import openapi_client
from openapi_client.api import sdavc_cloud_connector_api
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
    api_instance = sdavc_cloud_connector_api.SDAVCCloudConnectorApi(api_client)
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.enable_cloud_connector(get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDAVCCloudConnectorApi->enable_cloud_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

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

# **get_cloud_connector**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_connector()



Get SD_AVC Cloud Connector Config

### Example


```python
import time
import openapi_client
from openapi_client.api import sdavc_cloud_connector_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdavc_cloud_connector_api.SDAVCCloudConnectorApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_connector()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDAVCCloudConnectorApi->get_cloud_connector: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_cloud_connector_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_connector_status()



Get SD_AVC Cloud Connector Status

### Example


```python
import time
import openapi_client
from openapi_client.api import sdavc_cloud_connector_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdavc_cloud_connector_api.SDAVCCloudConnectorApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_connector_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDAVCCloudConnectorApi->get_cloud_connector_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

