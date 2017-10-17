# swagger_client.ImportApi

All URIs are relative to *https://localhost/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_post**](ImportApi.md#root_post) | **POST** / | Import a bulk of activities
[**source_id_activity_id_delete**](ImportApi.md#source_id_activity_id_delete) | **DELETE** /{source_id}/{activity_id} | Delete this activity
[**source_id_activity_id_put**](ImportApi.md#source_id_activity_id_put) | **PUT** /{source_id}/{activity_id} | Create or update this activity


# **root_post**
> ActivityList root_post(import_activities)

Import a bulk of activities

The data field format is source dependent

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ImportApi()
import_activities = swagger_client.ImportList() # ImportList | 

try: 
    # Import a bulk of activities
    api_response = api_instance.root_post(import_activities)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->root_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_activities** | [**ImportList**](ImportList.md)|  | 

### Return type

[**ActivityList**](ActivityList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_activity_id_delete**
> Ok source_id_activity_id_delete(source_id, activity_id)

Delete this activity

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ImportApi()
source_id = 56 # int | 
activity_id = 'activity_id_example' # str | 

try: 
    # Delete this activity
    api_response = api_instance.source_id_activity_id_delete(source_id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->source_id_activity_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**|  | 
 **activity_id** | **str**|  | 

### Return type

[**Ok**](Ok.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_activity_id_put**
> Ok source_id_activity_id_put(source_id, activity_id, activity_import)

Create or update this activity

The data field format is source dependent

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ImportApi()
source_id = 56 # int | 
activity_id = 'activity_id_example' # str | 
activity_import = swagger_client.ModelImport() # ModelImport | 

try: 
    # Create or update this activity
    api_response = api_instance.source_id_activity_id_put(source_id, activity_id, activity_import)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->source_id_activity_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**|  | 
 **activity_id** | **str**|  | 
 **activity_import** | [**ModelImport**](ModelImport.md)|  | 

### Return type

[**Ok**](Ok.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

