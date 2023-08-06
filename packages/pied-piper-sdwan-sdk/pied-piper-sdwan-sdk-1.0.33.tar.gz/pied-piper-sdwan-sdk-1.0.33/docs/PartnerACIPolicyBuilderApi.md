# openapi_client.PartnerACIPolicyBuilderApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dscp_mappings**](PartnerACIPolicyBuilderApi.md#create_dscp_mappings) | **POST** /partner/aci/policy/dscpmapping/{partnerId} | 
[**delete_dscp_mappings**](PartnerACIPolicyBuilderApi.md#delete_dscp_mappings) | **DELETE** /partner/aci/policy/dscpmapping/{partnerId} | 
[**get_aci_definitions**](PartnerACIPolicyBuilderApi.md#get_aci_definitions) | **GET** /partner/aci/policy | 
[**get_data_prefix_mappings**](PartnerACIPolicyBuilderApi.md#get_data_prefix_mappings) | **GET** /partner/aci/policy/prefixmapping/{partnerId} | 
[**get_data_prefix_sequences**](PartnerACIPolicyBuilderApi.md#get_data_prefix_sequences) | **GET** /partner/aci/policy/sequences | 
[**get_dscp_mappings**](PartnerACIPolicyBuilderApi.md#get_dscp_mappings) | **GET** /partner/aci/policy/dscpmapping/{partnerId} | 
[**get_events**](PartnerACIPolicyBuilderApi.md#get_events) | **GET** /partner/aci/policy/events/{partnerId} | 
[**set_data_prefix_mappings**](PartnerACIPolicyBuilderApi.md#set_data_prefix_mappings) | **POST** /partner/aci/policy/prefixmapping/{partnerId} | 


# **create_dscp_mappings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_dscp_mappings(partner_id)



Create an ACI definition entry

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_aci_policy_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_aci_policy_builder_api.PartnerACIPolicyBuilderApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | ACI definition (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dscp_mappings(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->create_dscp_mappings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_dscp_mappings(partner_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->create_dscp_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| ACI definition | [optional]

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

# **delete_dscp_mappings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_dscp_mappings(partner_id)



Delete DSCP mapping

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_aci_policy_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_aci_policy_builder_api.PartnerACIPolicyBuilderApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_dscp_mappings(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->delete_dscp_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |

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

# **get_aci_definitions**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aci_definitions()



Get ACI definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_aci_policy_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_aci_policy_builder_api.PartnerACIPolicyBuilderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_aci_definitions()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->get_aci_definitions: %s\n" % e)
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

# **get_data_prefix_mappings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_data_prefix_mappings(partner_id)



Get prefix mapping

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_aci_policy_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_aci_policy_builder_api.PartnerACIPolicyBuilderApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_data_prefix_mappings(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->get_data_prefix_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |

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

# **get_data_prefix_sequences**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_data_prefix_sequences()



Get data prefix sequence

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_aci_policy_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_aci_policy_builder_api.PartnerACIPolicyBuilderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_data_prefix_sequences()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->get_data_prefix_sequences: %s\n" % e)
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

# **get_dscp_mappings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dscp_mappings(partner_id)



Get DSCP policy

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_aci_policy_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_aci_policy_builder_api.PartnerACIPolicyBuilderApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dscp_mappings(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->get_dscp_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |

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

# **get_events**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_events(partner_id)



Get ACI events

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_aci_policy_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_aci_policy_builder_api.PartnerACIPolicyBuilderApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id
    starttime = 1 # int | Start time (optional)
    endtime = 1 # int | End time (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_events(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->get_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_events(partner_id, starttime=starttime, endtime=endtime)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->get_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |
 **starttime** | **int**| Start time | [optional]
 **endtime** | **int**| End time | [optional]

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

# **set_data_prefix_mappings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_data_prefix_mappings(partner_id)



Create data prefix mapping

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_aci_policy_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_aci_policy_builder_api.PartnerACIPolicyBuilderApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Prefix definition (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_data_prefix_mappings(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->set_data_prefix_mappings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_data_prefix_mappings(partner_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerACIPolicyBuilderApi->set_data_prefix_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Prefix definition | [optional]

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

