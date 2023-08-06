# openapi_client.ConfigurationDeviceInventoryApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_self_signed_cert**](ConfigurationDeviceInventoryApi.md#check_self_signed_cert) | **GET** /system/device/selfsignedcert/iscreated | 
[**claim_devices**](ConfigurationDeviceInventoryApi.md#claim_devices) | **POST** /system/device/claimDevices | 
[**create_device**](ConfigurationDeviceInventoryApi.md#create_device) | **POST** /system/device | 
[**decommission_vedge_cloud**](ConfigurationDeviceInventoryApi.md#decommission_vedge_cloud) | **PUT** /system/device/decommission/{uuid} | 
[**delete_device**](ConfigurationDeviceInventoryApi.md#delete_device) | **DELETE** /system/device/{uuid} | 
[**devices_without_subject_sudi**](ConfigurationDeviceInventoryApi.md#devices_without_subject_sudi) | **GET** /system/device/devicesWithoutSubjectSudi | 
[**edit_device**](ConfigurationDeviceInventoryApi.md#edit_device) | **PUT** /system/device/{uuid} | 
[**form_post**](ConfigurationDeviceInventoryApi.md#form_post) | **POST** /system/device/fileupload | 
[**generate_bootstrap_config_for_vedge**](ConfigurationDeviceInventoryApi.md#generate_bootstrap_config_for_vedge) | **GET** /system/device/bootstrap/device/{uuid} | 
[**generate_bootstrap_config_for_vedges**](ConfigurationDeviceInventoryApi.md#generate_bootstrap_config_for_vedges) | **POST** /system/device/bootstrap/devices | 
[**generate_generic_bootstrap_config_for_vedges**](ConfigurationDeviceInventoryApi.md#generate_generic_bootstrap_config_for_vedges) | **GET** /system/device/bootstrap/generic/devices | 
[**get_all_unclaimed_devices**](ConfigurationDeviceInventoryApi.md#get_all_unclaimed_devices) | **GET** /system/device/unclaimedDevices | 
[**get_bootstrap_config_zip**](ConfigurationDeviceInventoryApi.md#get_bootstrap_config_zip) | **GET** /system/device/bootstrap/download/{id} | 
[**get_cloud_dock_data_based_on_device_type**](ConfigurationDeviceInventoryApi.md#get_cloud_dock_data_based_on_device_type) | **GET** /system/device/type/{deviceCategory} | 
[**get_cloud_dock_default_config_based_on_device_type**](ConfigurationDeviceInventoryApi.md#get_cloud_dock_default_config_based_on_device_type) | **GET** /system/device/type/{deviceCategory}/defaultConfig | 
[**get_controller_v_edge_sync_status**](ConfigurationDeviceInventoryApi.md#get_controller_v_edge_sync_status) | **GET** /system/device/controllers/vedge/status | 
[**get_devices_details**](ConfigurationDeviceInventoryApi.md#get_devices_details) | **GET** /system/device/{deviceCategory} | 
[**get_management_system_ip_info**](ConfigurationDeviceInventoryApi.md#get_management_system_ip_info) | **GET** /system/device/management/systemip | 
[**get_rma_candidates**](ConfigurationDeviceInventoryApi.md#get_rma_candidates) | **GET** /system/device/rma/candidates/{deviceType} | 
[**get_root_cert_status_all**](ConfigurationDeviceInventoryApi.md#get_root_cert_status_all) | **GET** /system/device/rootcertchain/status | 
[**get_tenant_management_system_ips**](ConfigurationDeviceInventoryApi.md#get_tenant_management_system_ips) | **GET** /system/device/tenant/management/systemip | 
[**invalidate_vmanage_root_ca**](ConfigurationDeviceInventoryApi.md#invalidate_vmanage_root_ca) | **DELETE** /system/device/vmanagerootca/{uuid} | 
[**migrate_device**](ConfigurationDeviceInventoryApi.md#migrate_device) | **PUT** /system/device/migrateDevice/{uuid} | 
[**reset_vedge_cloud**](ConfigurationDeviceInventoryApi.md#reset_vedge_cloud) | **PUT** /system/device/reset/{uuid} | 
[**set_life_cycle**](ConfigurationDeviceInventoryApi.md#set_life_cycle) | **POST** /system/device/lifecycle/management/{uuid} | 
[**sync_devices**](ConfigurationDeviceInventoryApi.md#sync_devices) | **POST** /system/device/smartaccount/sync | 
[**sync_root_cert_chain**](ConfigurationDeviceInventoryApi.md#sync_root_cert_chain) | **GET** /system/device/sync/rootcertchain | 
[**update_device_subject_sudi**](ConfigurationDeviceInventoryApi.md#update_device_subject_sudi) | **PUT** /system/device/updateDeviceSubjectSUDI/{uuid} | 
[**validate_user**](ConfigurationDeviceInventoryApi.md#validate_user) | **POST** /system/device/smartaccount/authenticate | 
[**validate_user1**](ConfigurationDeviceInventoryApi.md#validate_user1) | **POST** /system/device/generate-payg | 


# **check_self_signed_cert**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} check_self_signed_cert()



Whether self signed certificate created

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.check_self_signed_cert()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->check_self_signed_cert: %s\n" % e)
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

# **claim_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] claim_devices()



Claim the selected unclaimed devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Claim device request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.claim_devices(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->claim_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Claim device request | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **create_device**
> create_device()



Create new device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Create device request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_device(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->create_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Create device request | [optional]

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

# **decommission_vedge_cloud**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} decommission_vedge_cloud(uuid)



Decomission vEdge device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.decommission_vedge_cloud(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->decommission_vedge_cloud: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **delete_device**
> delete_device(uuid)



Delete vEdges

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_device(uuid)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->delete_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **devices_without_subject_sudi**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] devices_without_subject_sudi()



retrieve devices without subject sudi

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.devices_without_subject_sudi()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->devices_without_subject_sudi: %s\n" % e)
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

# **edit_device**
> edit_device(uuid)



Edit device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Device uuid
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device config (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.edit_device(uuid)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->edit_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_device(uuid, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->edit_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device config | [optional]

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

# **form_post**
> form_post()



Upload file to vEdge

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.form_post()
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->form_post: %s\n" % e)
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

# **generate_bootstrap_config_for_vedge**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_bootstrap_config_for_vedge(uuid, configtype, )



Create vEdge device config

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Device uuid
    configtype = "configtype_example" # str | Device config type
    version = "v1" # str | cloud-init format version (optional) if omitted the server will use the default value of "v1"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_bootstrap_config_for_vedge(uuid, configtype, )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->generate_bootstrap_config_for_vedge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_bootstrap_config_for_vedge(uuid, configtype, version=version)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->generate_bootstrap_config_for_vedge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |
 **configtype** | **str**| Device config type |
 **incl_def_root_cert** | **bool**| Include default root certs flag | defaults to True
 **version** | **str**| cloud-init format version | [optional] if omitted the server will use the default value of "v1"

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

# **generate_bootstrap_config_for_vedges**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_bootstrap_config_for_vedges()



Create bootstrap config for software vEdges

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device bootstrap type and id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_bootstrap_config_for_vedges(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->generate_bootstrap_config_for_vedges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device bootstrap type and id | [optional]

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

# **generate_generic_bootstrap_config_for_vedges**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_generic_bootstrap_config_for_vedges()



Create bootstrap config for software vEdges

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    wanif = "wanif_example" # str | Device WAN interface (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_generic_bootstrap_config_for_vedges(wanif=wanif)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->generate_generic_bootstrap_config_for_vedges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wanif** | **str**| Device WAN interface | [optional]

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

# **get_all_unclaimed_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_all_unclaimed_devices()



Get list of all unclaimed devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_all_unclaimed_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_all_unclaimed_devices: %s\n" % e)
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

# **get_bootstrap_config_zip**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bootstrap_config_zip(id)



Download vEdge device config

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    id = "id_example" # str | Bootstrap config id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_bootstrap_config_zip(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_bootstrap_config_zip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bootstrap config id |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_dock_data_based_on_device_type**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cloud_dock_data_based_on_device_type(device_category)



Get devices details

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    device_category = "vedges" # str | Device category

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_dock_data_based_on_device_type(device_category)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_cloud_dock_data_based_on_device_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_category** | **str**| Device category |

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

# **get_cloud_dock_default_config_based_on_device_type**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cloud_dock_default_config_based_on_device_type(device_category)



Get devices default config

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    device_category = "vedges" # str | Device category

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_dock_default_config_based_on_device_type(device_category)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_cloud_dock_default_config_based_on_device_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_category** | **str**| Device category |

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

# **get_controller_v_edge_sync_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_controller_v_edge_sync_status()



Get controllers vEdge sync status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_controller_v_edge_sync_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_controller_v_edge_sync_status: %s\n" % e)
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

# **get_devices_details**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_devices_details(device_category)



Get devices details. When {deviceCategory = controllers}, it returns vEdge sync status, vBond, vManage and vSmart. When {deviceCategory = vedges}, it returns all available vEdge routers

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from openapi_client.model.device_ip import DeviceIP
from openapi_client.model.device_uuid import DeviceUuid
from openapi_client.model.certificate_states import CertificateStates
from openapi_client.model.certificate_validity import CertificateValidity
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    device_category = "deviceCategory_example" # str | Device category
    model = "vedge-cloud" # str | Device model (optional)
    state = [
        CertificateStates(
            certificate_types="certificate_types_example",
        ),
    ] # [CertificateStates] | List of states (optional)
    uuid = [
        DeviceUuid(
            device_uuid="device_uuid_example",
        ),
    ] # [DeviceUuid] | List of device uuid (optional)
    device_ip = [
        DeviceIP(
            device_ip="device_ip_example",
        ),
    ] # [DeviceIP] | List of device system IP (optional)
    validity = [
        CertificateValidity(
            certificate_validity="certificate_validity_example",
        ),
    ] # [CertificateValidity] | List of device validity (optional)
    family = "aon" # str | The platform family to filter for (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_devices_details(device_category)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_devices_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_devices_details(device_category, model=model, state=state, uuid=uuid, device_ip=device_ip, validity=validity, family=family)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_devices_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_category** | **str**| Device category |
 **model** | **str**| Device model | [optional]
 **state** | [**[CertificateStates]**](CertificateStates.md)| List of states | [optional]
 **uuid** | [**[DeviceUuid]**](DeviceUuid.md)| List of device uuid | [optional]
 **device_ip** | [**[DeviceIP]**](DeviceIP.md)| List of device system IP | [optional]
 **validity** | [**[CertificateValidity]**](CertificateValidity.md)| List of device validity | [optional]
 **family** | **str**| The platform family to filter for | [optional]

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

# **get_management_system_ip_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_management_system_ip_info()



Get management system IP mapping

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_management_system_ip_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_management_system_ip_info: %s\n" % e)
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

# **get_rma_candidates**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_rma_candidates()



Get RMA candidates by device type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Excluded currently selected uuid (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_rma_candidates()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_rma_candidates: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_rma_candidates(uuid=uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_rma_candidates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type** | **str**| Device Type | defaults to "vsmart"
 **uuid** | **str**| Excluded currently selected uuid | [optional]

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

# **get_root_cert_status_all**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_root_cert_status_all(state)



Get controllers vEdge sync status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    state = "pending" # str | Root certificate state

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_root_cert_status_all(state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_root_cert_status_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Root certificate state |

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

# **get_tenant_management_system_ips**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_tenant_management_system_ips()



Get management system IP<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_tenant_management_system_ips()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->get_tenant_management_system_ips: %s\n" % e)
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

# **invalidate_vmanage_root_ca**
> invalidate_vmanage_root_ca(uuid)



Invalidate vManage root CA

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_instance.invalidate_vmanage_root_ca(uuid)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->invalidate_vmanage_root_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **migrate_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} migrate_device(uuid)



Migrate device software to vedge/cedge

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.migrate_device(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->migrate_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **reset_vedge_cloud**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} reset_vedge_cloud(uuid)



Reset vEdge device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.reset_vedge_cloud(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->reset_vedge_cloud: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **set_life_cycle**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_life_cycle(uuid)



Set device lifecycle needed flag

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Device uuid
    enable = True # bool | lifecycle needed flag (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_life_cycle(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->set_life_cycle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_life_cycle(uuid, enable=enable)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->set_life_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |
 **enable** | **bool**| lifecycle needed flag | [optional]

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

# **sync_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sync_devices()



Sync devices from Smart-Account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from openapi_client.model.smart_account_model import SmartAccountModel
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    smart_account_model = SmartAccountModel(
        env="env_example",
        organization_name="organization_name_example",
        password="password_example",
        username="username_example",
        validity_string="validity_string_example",
    ) # SmartAccountModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sync_devices(smart_account_model=smart_account_model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->sync_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_account_model** | [**SmartAccountModel**](SmartAccountModel.md)|  | [optional]

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

# **sync_root_cert_chain**
> sync_root_cert_chain()



Sync root certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.sync_root_cert_chain()
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->sync_root_cert_chain: %s\n" % e)
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

# **update_device_subject_sudi**
> update_device_subject_sudi(uuid)



update subject sudi value of given device uuid

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_device_subject_sudi(uuid)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->update_device_subject_sudi: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **validate_user**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} validate_user()



Authenticate vSmart user account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
from openapi_client.model.smart_account_model import SmartAccountModel
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    smart_account_model = SmartAccountModel(
        env="env_example",
        organization_name="organization_name_example",
        password="password_example",
        username="username_example",
        validity_string="validity_string_example",
    ) # SmartAccountModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.validate_user(smart_account_model=smart_account_model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->validate_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_account_model** | [**SmartAccountModel**](SmartAccountModel.md)|  | [optional]

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

# **validate_user1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} validate_user1()



Authenticate vSmart user account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_inventory_api
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
    api_instance = configuration_device_inventory_api.ConfigurationDeviceInventoryApi(api_client)
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.validate_user1(get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceInventoryApi->validate_user1: %s\n" % e)
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

