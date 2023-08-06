# openapi_client.MSLAApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_template**](MSLAApi.md#get_all_template) | **GET** /msla/template | 
[**get_license_and_device_count**](MSLAApi.md#get_license_and_device_count) | **GET** /msla/monitoring/licensedDeviceCount | 
[**get_license_and_device_count1**](MSLAApi.md#get_license_and_device_count1) | **GET** /msla/monitoring/licensedDistributionDetails | 
[**get_msla_devices**](MSLAApi.md#get_msla_devices) | **GET** /msla/devices | 
[**get_packaging_distribution_details**](MSLAApi.md#get_packaging_distribution_details) | **GET** /msla/monitoring/packagingDistributionDetails | 
[**get_subscriptions**](MSLAApi.md#get_subscriptions) | **GET** /msla/va/License | 
[**get_subscriptions1**](MSLAApi.md#get_subscriptions1) | **POST** /msla/template/licenses | 
[**sync_licenses2**](MSLAApi.md#sync_licenses2) | **POST** /msla/licenses/sync | 


# **get_all_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_template()



Retrieve all MSLA template

### Example


```python
import time
import openapi_client
from openapi_client.api import msla_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = msla_api.MSLAApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_all_template()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MSLAApi->get_all_template: %s\n" % e)
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

# **get_license_and_device_count**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_license_and_device_count()



get license and device count

### Example


```python
import time
import openapi_client
from openapi_client.api import msla_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = msla_api.MSLAApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_license_and_device_count()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MSLAApi->get_license_and_device_count: %s\n" % e)
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

# **get_license_and_device_count1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_license_and_device_count1()



get license and device count

### Example


```python
import time
import openapi_client
from openapi_client.api import msla_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = msla_api.MSLAApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_license_and_device_count1()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MSLAApi->get_license_and_device_count1: %s\n" % e)
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

# **get_msla_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_msla_devices()



Retrieve devices subscription

### Example


```python
import time
import openapi_client
from openapi_client.api import msla_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = msla_api.MSLAApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_msla_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MSLAApi->get_msla_devices: %s\n" % e)
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

# **get_packaging_distribution_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_packaging_distribution_details()



get packaging distribution details

### Example


```python
import time
import openapi_client
from openapi_client.api import msla_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = msla_api.MSLAApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_packaging_distribution_details()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MSLAApi->get_packaging_distribution_details: %s\n" % e)
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

# **get_subscriptions**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_subscriptions()



Retrieve MSLA subscription/licenses

### Example


```python
import time
import openapi_client
from openapi_client.api import msla_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = msla_api.MSLAApi(api_client)
    virtual_account_id = "virtual_account_id_example" # str | virtual_account_id (optional)
    license_type = "licenseType_example" # str | licenseType (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_subscriptions(virtual_account_id=virtual_account_id, license_type=license_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MSLAApi->get_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_account_id** | **str**| virtual_account_id | [optional]
 **license_type** | **str**| licenseType | [optional]

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

# **get_subscriptions1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_subscriptions1()



Retrieve MSLA subscription/licenses

### Example


```python
import time
import openapi_client
from openapi_client.api import msla_api
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
    api_instance = msla_api.MSLAApi(api_client)
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_subscriptions1(get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MSLAApi->get_subscriptions1: %s\n" % e)
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

# **sync_licenses2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sync_licenses2()



Retrieve MSLA subscription/licenses

### Example


```python
import time
import openapi_client
from openapi_client.api import msla_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = msla_api.MSLAApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Sync license (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sync_licenses2(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MSLAApi->sync_licenses2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Sync license | [optional]

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

