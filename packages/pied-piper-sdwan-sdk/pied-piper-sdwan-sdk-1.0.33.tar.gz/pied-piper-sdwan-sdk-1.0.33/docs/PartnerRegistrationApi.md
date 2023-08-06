# openapi_client.PartnerRegistrationApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_device_mapping**](PartnerRegistrationApi.md#delete_device_mapping) | **POST** /partner/{partnerType}/unmap/{nmsId} | 
[**delete_partner**](PartnerRegistrationApi.md#delete_partner) | **DELETE** /partner/{partnerType}/{nmsId} | 
[**get_data_change_info**](PartnerRegistrationApi.md#get_data_change_info) | **GET** /serverlongpoll/event/poll/{partnerId} | 
[**get_partner**](PartnerRegistrationApi.md#get_partner) | **GET** /partner/{partnerType}/{nmsId} | 
[**get_partner_devices**](PartnerRegistrationApi.md#get_partner_devices) | **GET** /partner/{partnerType}/map/{nmsId} | 
[**get_partners**](PartnerRegistrationApi.md#get_partners) | **GET** /partner | 
[**get_partners_by_partner_type**](PartnerRegistrationApi.md#get_partners_by_partner_type) | **GET** /partner/{partnerType} | 
[**get_vpn_list**](PartnerRegistrationApi.md#get_vpn_list) | **GET** /partner/vpn | 
[**map_devices**](PartnerRegistrationApi.md#map_devices) | **POST** /partner/{partnerType}/map/{nmsId} | 
[**register_partner**](PartnerRegistrationApi.md#register_partner) | **POST** /partner/{partnerType} | 
[**unmap_devices**](PartnerRegistrationApi.md#unmap_devices) | **DELETE** /partner/{partnerType}/map/{nmsId} | 
[**update_partner**](PartnerRegistrationApi.md#update_partner) | **PUT** /partner/{partnerType}/{nmsId} | 


# **delete_device_mapping**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_device_mapping(partner_type, nms_id)



Unmap a set of devices for the partner

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_type = "partnerType_example" # str | Partner type
    nms_id = "nmsId_example" # str | NMS Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | List of devices (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_device_mapping(partner_type, nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->delete_device_mapping: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_device_mapping(partner_type, nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->delete_device_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_type** | **str**| Partner type |
 **nms_id** | **str**| NMS Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| List of devices | [optional]

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

# **delete_partner**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_partner(partner_type, nms_id)



Delete NMS partner

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from openapi_client.model.partner_type import PartnerType
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_type = PartnerType(
        partner_type="aci",
    ) # PartnerType | Partner type
    nms_id = "nmsId_example" # str | NMS Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_partner(partner_type, nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->delete_partner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_type** | **PartnerType**| Partner type |
 **nms_id** | **str**| NMS Id |

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

# **get_data_change_info**
> get_data_change_info(partner_id)



Retrieve registration change information

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from openapi_client.model.event_name import EventName
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id
    event_id = "event_id_example" # str | Continuation token of ongoing event-polling session (optional)
    event_names = [
        EventName(
            event_name="event_name_example",
        ),
    ] # [EventName] | Names of type of events to filter on (optional)
    wait_time = 0 # int | Maximum polling wait time in seconds (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_data_change_info(partner_id)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->get_data_change_info: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_data_change_info(partner_id, event_id=event_id, event_names=event_names, wait_time=wait_time)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->get_data_change_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |
 **event_id** | **str**| Continuation token of ongoing event-polling session | [optional]
 **event_names** | [**[EventName]**](EventName.md)| Names of type of events to filter on | [optional]
 **wait_time** | **int**| Maximum polling wait time in seconds | [optional] if omitted the server will use the default value of 0

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

# **get_partner**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_partner(partner_type, nms_id)



Get NMS partners by partner type and Id

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_type = "partnerType_example" # str | Partner type
    nms_id = "nmsId_example" # str | NMS Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_partner(partner_type, nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->get_partner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_type** | **str**| Partner type |
 **nms_id** | **str**| NMS Id |

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

# **get_partner_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_partner_devices(partner_type, nms_id)



List mapped devices for the partner

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from openapi_client.model.partner_type import PartnerType
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_type = PartnerType(
        partner_type="aci",
    ) # PartnerType | Partner type
    nms_id = "nmsId_example" # str | NMS Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_partner_devices(partner_type, nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->get_partner_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_type** | **PartnerType**| Partner type |
 **nms_id** | **str**| NMS Id |

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

# **get_partners**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_partners()



Get all NMS partners

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_partners()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->get_partners: %s\n" % e)
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

# **get_partners_by_partner_type**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_partners_by_partner_type(partner_type)



Get NMS partners by partner type

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_type = "partnerType_example" # str | Partner type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_partners_by_partner_type(partner_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->get_partners_by_partner_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_type** | **str**| Partner type |

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

# **get_vpn_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vpn_list()



Get all VPNs

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_vpn_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->get_vpn_list: %s\n" % e)
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

# **map_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} map_devices(partner_type, nms_id)



Map devices for the partner

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_type = "partnerType_example" # str | Partner type
    nms_id = "nmsId_example" # str | NMS Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | List of devices (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.map_devices(partner_type, nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->map_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.map_devices(partner_type, nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->map_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_type** | **str**| Partner type |
 **nms_id** | **str**| NMS Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| List of devices | [optional]

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

# **register_partner**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} register_partner(partner_type)



Register NMS partner

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_type = "partnerType_example" # str | Partner type
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Partner (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.register_partner(partner_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->register_partner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.register_partner(partner_type, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->register_partner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_type** | **str**| Partner type |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Partner | [optional]

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

# **unmap_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unmap_devices(partner_type, nms_id)



Unmap all devices for the partner

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from openapi_client.model.partner_type import PartnerType
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_type = PartnerType(
        partner_type="aci",
    ) # PartnerType | Partner type
    nms_id = "nmsId_example" # str | NMS Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.unmap_devices(partner_type, nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->unmap_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_type** | **PartnerType**| Partner type |
 **nms_id** | **str**| NMS Id |

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

# **update_partner**
> update_partner(partner_type, nms_id)



Update NMS partner details

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_registration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_registration_api.PartnerRegistrationApi(api_client)
    partner_type = "partnerType_example" # str | Partner type
    nms_id = "nmsId_example" # str | NMS Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Partner (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_partner(partner_type, nms_id)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->update_partner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_partner(partner_type, nms_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerRegistrationApi->update_partner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_type** | **str**| Partner type |
 **nms_id** | **str**| NMS Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Partner | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

