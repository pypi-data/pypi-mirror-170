# openapi_client.ConfigurationDeviceActionsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filter_vpn_list**](ConfigurationDeviceActionsApi.md#create_filter_vpn_list) | **GET** /device/action/filter/vpn | 
[**create_unique_vpn_list**](ConfigurationDeviceActionsApi.md#create_unique_vpn_list) | **POST** /device/action/uniquevpnlist | 
[**create_vpn_list**](ConfigurationDeviceActionsApi.md#create_vpn_list) | **GET** /device/action/vpn | 
[**generate_change_partition_info**](ConfigurationDeviceActionsApi.md#generate_change_partition_info) | **GET** /device/action/changepartition | 
[**generate_deactivate_info**](ConfigurationDeviceActionsApi.md#generate_deactivate_info) | **GET** /device/action/deactivate | 
[**generate_device_action_list**](ConfigurationDeviceActionsApi.md#generate_device_action_list) | **GET** /device/action/list | 
[**generate_device_list**](ConfigurationDeviceActionsApi.md#generate_device_list) | **GET** /device/action/install/devices/{deviceType} | 
[**generate_install_info**](ConfigurationDeviceActionsApi.md#generate_install_info) | **GET** /device/action/install | 
[**generate_reboot_device_list**](ConfigurationDeviceActionsApi.md#generate_reboot_device_list) | **GET** /device/action/reboot/devices/{deviceType} | 
[**generate_reboot_info**](ConfigurationDeviceActionsApi.md#generate_reboot_info) | **GET** /device/action/reboot | 
[**generate_rediscover_info**](ConfigurationDeviceActionsApi.md#generate_rediscover_info) | **GET** /device/action/rediscover | 
[**generate_remove_partition_info**](ConfigurationDeviceActionsApi.md#generate_remove_partition_info) | **GET** /device/action/removepartition | 
[**generate_security_devices_list**](ConfigurationDeviceActionsApi.md#generate_security_devices_list) | **GET** /device/action/security/devices/{policyType} | 
[**get_ztp_upgrade_config**](ConfigurationDeviceActionsApi.md#get_ztp_upgrade_config) | **GET** /device/action/ztp/upgrade | 
[**get_ztp_upgrade_config_setting**](ConfigurationDeviceActionsApi.md#get_ztp_upgrade_config_setting) | **GET** /device/action/ztp/upgrade/setting | 
[**initiate_image_download**](ConfigurationDeviceActionsApi.md#initiate_image_download) | **POST** /device/action/image-download | 
[**process_amp_api_re_key**](ConfigurationDeviceActionsApi.md#process_amp_api_re_key) | **POST** /device/action/security/amp/rekey | 
[**process_change_partition**](ConfigurationDeviceActionsApi.md#process_change_partition) | **POST** /device/action/changepartition | 
[**process_deactivate_smu**](ConfigurationDeviceActionsApi.md#process_deactivate_smu) | **POST** /device/action/deactivate | 
[**process_default_partition**](ConfigurationDeviceActionsApi.md#process_default_partition) | **POST** /device/action/defaultpartition | 
[**process_delete_amp_api_key**](ConfigurationDeviceActionsApi.md#process_delete_amp_api_key) | **DELETE** /device/action/security/amp/apikey/{uuid} | 
[**process_install**](ConfigurationDeviceActionsApi.md#process_install) | **POST** /device/action/install | 
[**process_lxc_activate**](ConfigurationDeviceActionsApi.md#process_lxc_activate) | **POST** /device/action/lxcactivate | 
[**process_lxc_delete**](ConfigurationDeviceActionsApi.md#process_lxc_delete) | **POST** /device/action/lxcdelete | 
[**process_lxc_install**](ConfigurationDeviceActionsApi.md#process_lxc_install) | **POST** /device/action/lxcinstall | 
[**process_lxc_reload**](ConfigurationDeviceActionsApi.md#process_lxc_reload) | **POST** /device/action/lxcreload | 
[**process_lxc_reset**](ConfigurationDeviceActionsApi.md#process_lxc_reset) | **POST** /device/action/lxcreset | 
[**process_lxc_upgrade**](ConfigurationDeviceActionsApi.md#process_lxc_upgrade) | **POST** /device/action/lxcupgrade | 
[**process_reboot**](ConfigurationDeviceActionsApi.md#process_reboot) | **POST** /device/action/reboot | 
[**process_remove_partition**](ConfigurationDeviceActionsApi.md#process_remove_partition) | **POST** /device/action/removepartition | 
[**process_remove_software_image**](ConfigurationDeviceActionsApi.md#process_remove_software_image) | **POST** /device/action/image-remove | 
[**process_vnf_install**](ConfigurationDeviceActionsApi.md#process_vnf_install) | **POST** /device/action/vnfinstall | 
[**process_ztp_upgrade_config**](ConfigurationDeviceActionsApi.md#process_ztp_upgrade_config) | **POST** /device/action/ztp/upgrade | 
[**process_ztp_upgrade_config_setting**](ConfigurationDeviceActionsApi.md#process_ztp_upgrade_config_setting) | **POST** /device/action/ztp/upgrade/setting | 
[**re_discover_all_device**](ConfigurationDeviceActionsApi.md#re_discover_all_device) | **POST** /device/action/rediscoverall | 
[**re_discover_devices**](ConfigurationDeviceActionsApi.md#re_discover_devices) | **POST** /device/action/rediscover | 
[**test_api_key**](ConfigurationDeviceActionsApi.md#test_api_key) | **GET** /device/action/security/apikey/{uuid} | 
[**test_iox_config**](ConfigurationDeviceActionsApi.md#test_iox_config) | **GET** /device/action/test/ioxconfig/{deviceIP} | 
[**trigger_pending_tasks_monitoring**](ConfigurationDeviceActionsApi.md#trigger_pending_tasks_monitoring) | **GET** /device/action/startmonitor | 


# **create_filter_vpn_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_filter_vpn_list()



Get filter VPN list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_filter_vpn_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->create_filter_vpn_list: %s\n" % e)
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

# **create_unique_vpn_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_unique_vpn_list()



Create unique VPN list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device IPs (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_unique_vpn_list(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->create_unique_vpn_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device IPs | [optional]

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

# **create_vpn_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_vpn_list()



Create VPN list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_vpn_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->create_vpn_list: %s\n" % e)
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

# **generate_change_partition_info**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_change_partition_info(device_id)



Get change partition information

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from openapi_client.model.device_ip import DeviceIP
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    device_id = [
        DeviceIP(
            device_ip="device_ip_example",
        ),
    ] # [DeviceIP] | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_change_partition_info(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_change_partition_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**[DeviceIP]**](DeviceIP.md)| Device Id |

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

# **generate_deactivate_info**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_deactivate_info(device_id)



Get deactivate partition information

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from openapi_client.model.device_ip import DeviceIP
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    device_id = [
        DeviceIP(
            device_ip="device_ip_example",
        ),
    ] # [DeviceIP] | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_deactivate_info(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_deactivate_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**[DeviceIP]**](DeviceIP.md)| Device Id |

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

# **generate_device_action_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_device_action_list()



Get device action list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_device_action_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_device_action_list: %s\n" % e)
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

# **generate_device_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_device_list(device_type, group_id)



Get list of installed devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from openapi_client.model.group_id import GroupId
from openapi_client.model.device_type import DeviceType
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    device_type = DeviceType(
        device_type="device_type_example",
    ) # DeviceType | Device type
    group_id = GroupId(
        group_id="group_id_example",
    ) # GroupId | Group Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_device_list(device_type, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_device_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type** | **DeviceType**| Device type |
 **group_id** | **GroupId**| Group Id |

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

# **generate_install_info**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_install_info(device_id)



Generate install info

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from openapi_client.model.device_ip import DeviceIP
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    device_id = [
        DeviceIP(
            device_ip="device_ip_example",
        ),
    ] # [DeviceIP] | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_install_info(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_install_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**[DeviceIP]**](DeviceIP.md)| Device Id |

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

# **generate_reboot_device_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_reboot_device_list(device_type, device_id)



Get list of rebooted devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from openapi_client.model.group_id import GroupId
from openapi_client.model.device_type import DeviceType
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    device_type = DeviceType(
        device_type="device_type_example",
    ) # DeviceType | Device type
    device_id = GroupId(
        group_id="group_id_example",
    ) # GroupId | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_reboot_device_list(device_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_reboot_device_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type** | **DeviceType**| Device type |
 **device_id** | **GroupId**| Device Id |

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

# **generate_reboot_info**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_reboot_info(device_id)



Get device reboot information

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from openapi_client.model.device_ip import DeviceIP
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    device_id = [
        DeviceIP(
            device_ip="device_ip_example",
        ),
    ] # [DeviceIP] | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_reboot_info(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_reboot_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**[DeviceIP]**](DeviceIP.md)| Device Id |

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

# **generate_rediscover_info**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_rediscover_info()



Get rediscover operation information

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_rediscover_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_rediscover_info: %s\n" % e)
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

# **generate_remove_partition_info**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_remove_partition_info(device_id)



Get remove partition information

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_remove_partition_info(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_remove_partition_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

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

# **generate_security_devices_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_security_devices_list(policy_type, group_id)



Get list of devices by security policy type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from openapi_client.model.group_id import GroupId
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    policy_type = "zoneBasedFW" # str | Policy type
    group_id = GroupId(
        group_id="group_id_example",
    ) # GroupId | Group Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_security_devices_list(policy_type, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->generate_security_devices_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_type** | **str**| Policy type |
 **group_id** | **GroupId**| Group Id |

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

# **get_ztp_upgrade_config**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ztp_upgrade_config()



Get ZTP upgrade configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_ztp_upgrade_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->get_ztp_upgrade_config: %s\n" % e)
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

# **get_ztp_upgrade_config_setting**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ztp_upgrade_config_setting()



Get ZTP upgrade configuration setting

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_ztp_upgrade_config_setting()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->get_ztp_upgrade_config_setting: %s\n" % e)
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

# **initiate_image_download**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} initiate_image_download()



Intitate image download on the given device.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Image download request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.initiate_image_download(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->initiate_image_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Image download request | [optional]

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

# **process_amp_api_re_key**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_amp_api_re_key()



Process amp api re-key operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | AMP API re-key request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_amp_api_re_key(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_amp_api_re_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| AMP API re-key request payload | [optional]

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

# **process_change_partition**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_change_partition()



Process change partition operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device change partition request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_change_partition(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_change_partition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device change partition request payload | [optional]

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

# **process_deactivate_smu**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_deactivate_smu()



Process deactivate operation for smu image

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device smu image deactivate request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_deactivate_smu(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_deactivate_smu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device smu image deactivate request | [optional]

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

# **process_default_partition**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_default_partition()



Process marking default partition operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Marking default partition request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_default_partition(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_default_partition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Marking default partition request | [optional]

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

# **process_delete_amp_api_key**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_delete_amp_api_key(uuid)



Process amp api key deletion operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    uuid = "uuid_example" # str | Uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.process_delete_amp_api_key(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_delete_amp_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Uuid |

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

# **process_install**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_install()



Process an installation operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Installation payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_install(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_install: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Installation payload | [optional]

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

# **process_lxc_activate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_lxc_activate()



Process an activation operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Activation request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_lxc_activate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_lxc_activate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Activation request payload | [optional]

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

# **process_lxc_delete**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_lxc_delete()



Process a delete operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Delete request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_lxc_delete(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_lxc_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Delete request payload | [optional]

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

# **process_lxc_install**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_lxc_install()



Process an installation operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Installation request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_lxc_install(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_lxc_install: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Installation request payload | [optional]

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

# **process_lxc_reload**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_lxc_reload()



Process a reload operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Reload request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_lxc_reload(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_lxc_reload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Reload request payload | [optional]

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

# **process_lxc_reset**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_lxc_reset()



Process a reset operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Reset request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_lxc_reset(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_lxc_reset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Reset request payload | [optional]

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

# **process_lxc_upgrade**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_lxc_upgrade()



Process an upgrade operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Upgrade request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_lxc_upgrade(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_lxc_upgrade: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Upgrade request payload | [optional]

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

# **process_reboot**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_reboot()



Process a reboot operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device reboot request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_reboot(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_reboot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device reboot request payload | [optional]

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

# **process_remove_partition**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_remove_partition()



Process remove partition operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device remove partition request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_remove_partition(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_remove_partition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device remove partition request payload | [optional]

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

# **process_remove_software_image**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_remove_software_image()



Process remove software image operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device remove software image request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_remove_software_image(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_remove_software_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device remove software image request payload | [optional]

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

# **process_vnf_install**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_vnf_install()



Process an installation operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Installation request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.process_vnf_install(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_vnf_install: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Installation request payload | [optional]

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

# **process_ztp_upgrade_config**
> process_ztp_upgrade_config()



Process ZTP upgrade configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | ZTP upgrade config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.process_ztp_upgrade_config(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_ztp_upgrade_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| ZTP upgrade config | [optional]

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

# **process_ztp_upgrade_config_setting**
> process_ztp_upgrade_config_setting()



Process ZTP upgrade configuration setting

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | ZTP upgrade setting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.process_ztp_upgrade_config_setting(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->process_ztp_upgrade_config_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| ZTP upgrade setting | [optional]

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

# **re_discover_all_device**
> re_discover_all_device()



Rediscover all devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Rediscover device request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.re_discover_all_device(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->re_discover_all_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Rediscover device request payload | [optional]

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

# **re_discover_devices**
> re_discover_devices()



Rediscover device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Rediscover device request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.re_discover_devices(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->re_discover_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Rediscover device request payload | [optional]

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

# **test_api_key**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} test_api_key(uuid)



Get API key from device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.test_api_key(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->test_api_key: %s\n" % e)
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

# **test_iox_config**
> test_iox_config(device_ip)



testIoxConfig

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from openapi_client.model.device_ip import DeviceIP
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)
    device_ip = DeviceIP(
        device_ip="device_ip_example",
    ) # DeviceIP | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_instance.test_iox_config(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->test_iox_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **DeviceIP**| Device IP |

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

# **trigger_pending_tasks_monitoring**
> trigger_pending_tasks_monitoring()



Triggers global monitoring thread

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_actions_api.ConfigurationDeviceActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.trigger_pending_tasks_monitoring()
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceActionsApi->trigger_pending_tasks_monitoring: %s\n" % e)
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

