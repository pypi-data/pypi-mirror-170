# openapi_client.PartnerDNACSDAAPIApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sda_config**](PartnerDNACSDAAPIApi.md#create_sda_config) | **POST** /partner/dnac/sda/config/{partnerId} | 
[**create_sda_config_from_netconf**](PartnerDNACSDAAPIApi.md#create_sda_config_from_netconf) | **POST** /partner/dnac/sda/netconfconfig/{partnerId} | 
[**get_device_details**](PartnerDNACSDAAPIApi.md#get_device_details) | **GET** /partner/dnac/sda/device/{partnerId}/{uuid} | 
[**get_overlay_vpn_list**](PartnerDNACSDAAPIApi.md#get_overlay_vpn_list) | **GET** /partner/dnac/sda/vpn | 
[**get_sda_enabled_devices**](PartnerDNACSDAAPIApi.md#get_sda_enabled_devices) | **GET** /partner/dnac/sda/device/{partnerId} | 
[**get_sites_for_partner**](PartnerDNACSDAAPIApi.md#get_sites_for_partner) | **GET** /partner/dnac/sda/site/{partnerId} | 


# **create_sda_config**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_sda_config(partner_id)



Create SDA enabled device

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_dnacsdaapi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_dnacsdaapi_api.PartnerDNACSDAAPIApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device SDA configuration (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sda_config(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerDNACSDAAPIApi->create_sda_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sda_config(partner_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerDNACSDAAPIApi->create_sda_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device SDA configuration | [optional]

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

# **create_sda_config_from_netconf**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_sda_config_from_netconf(partner_id)



Create SDA enabled device from Netconf

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_dnacsdaapi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_dnacsdaapi_api.PartnerDNACSDAAPIApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device SDA configuration (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sda_config_from_netconf(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerDNACSDAAPIApi->create_sda_config_from_netconf: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sda_config_from_netconf(partner_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerDNACSDAAPIApi->create_sda_config_from_netconf: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device SDA configuration | [optional]

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

# **get_device_details**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_device_details(partner_id, uuid)



Get SDA enabled devices detail

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_dnacsdaapi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_dnacsdaapi_api.PartnerDNACSDAAPIApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_details(partner_id, uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerDNACSDAAPIApi->get_device_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |
 **uuid** | **str**| Device uuid |

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

# **get_overlay_vpn_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_overlay_vpn_list()



Get Overlay VPN list

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_dnacsdaapi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_dnacsdaapi_api.PartnerDNACSDAAPIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_overlay_vpn_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerDNACSDAAPIApi->get_overlay_vpn_list: %s\n" % e)
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

# **get_sda_enabled_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_sda_enabled_devices(partner_id)



Get SDA enabled devices

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_dnacsdaapi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_dnacsdaapi_api.PartnerDNACSDAAPIApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sda_enabled_devices(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerDNACSDAAPIApi->get_sda_enabled_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |

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

# **get_sites_for_partner**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_sites_for_partner(partner_id)



Get SDA enabled devices

### Example


```python
import time
import openapi_client
from openapi_client.api import partner_dnacsdaapi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = partner_dnacsdaapi_api.PartnerDNACSDAAPIApi(api_client)
    partner_id = "partnerId_example" # str | Partner Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sites_for_partner(partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerDNACSDAAPIApi->get_sites_for_partner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Partner Id |

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

