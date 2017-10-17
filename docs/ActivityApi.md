# swagger_client.ActivityApi

All URIs are relative to *https://localhost/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](ActivityApi.md#root_get) | **GET** / | Get a list of activities.
[**source_id_activity_id_delete**](ActivityApi.md#source_id_activity_id_delete) | **DELETE** /{source_id}/{activity_id} | Delete this activity
[**source_id_activity_id_get**](ActivityApi.md#source_id_activity_id_get) | **GET** /{source_id}/{activity_id} | Get this activity
[**source_id_activity_id_put**](ActivityApi.md#source_id_activity_id_put) | **PUT** /{source_id}/{activity_id} | Create or update this activity
[**source_id_activity_id_tags_patch**](ActivityApi.md#source_id_activity_id_tags_patch) | **PATCH** /{source_id}/{activity_id}/tags | Modify tags of activity


# **root_get**
> ActivityList root_get(source_ids=source_ids, tagset_ids=tagset_ids, tags=tags, languages=languages, count=count, max_id=max_id, since=since, until=until, random=random)

Get a list of activities.

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
api_instance = swagger_client.ActivityApi()
source_ids = [56] # list[int] |  (optional)
tagset_ids = [56] # list[int] |  (optional)
tags = ['tags_example'] # list[str] |  (optional)
languages = ['en'] # list[str] | Inferred language of text (optional) (default to en)
count = 8 # int | number of activities to fetch (optional) (default to 8)
max_id = 'max_id_example' # str | used for cursoring (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | DateTime of oldest entry (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | DateTime of newest entry (optional)
random = false # bool | should a random sample be drawn (optional) (default to false)

try: 
    # Get a list of activities.
    api_response = api_instance.root_get(source_ids=source_ids, tagset_ids=tagset_ids, tags=tags, languages=languages, count=count, max_id=max_id, since=since, until=until, random=random)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->root_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_ids** | [**list[int]**](int.md)|  | [optional] 
 **tagset_ids** | [**list[int]**](int.md)|  | [optional] 
 **tags** | [**list[str]**](str.md)|  | [optional] 
 **languages** | [**list[str]**](str.md)| Inferred language of text | [optional] [default to en]
 **count** | **int**| number of activities to fetch | [optional] [default to 8]
 **max_id** | **str**| used for cursoring | [optional] 
 **since** | **datetime**| DateTime of oldest entry | [optional] 
 **until** | **datetime**| DateTime of newest entry | [optional] 
 **random** | **bool**| should a random sample be drawn | [optional] [default to false]

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
api_instance = swagger_client.ActivityApi()
source_id = 56 # int | 
activity_id = 'activity_id_example' # str | 

try: 
    # Delete this activity
    api_response = api_instance.source_id_activity_id_delete(source_id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->source_id_activity_id_delete: %s\n" % e)
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

# **source_id_activity_id_get**
> Activity source_id_activity_id_get(source_id, activity_id)

Get this activity

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
api_instance = swagger_client.ActivityApi()
source_id = 56 # int | 
activity_id = 'activity_id_example' # str | 

try: 
    # Get this activity
    api_response = api_instance.source_id_activity_id_get(source_id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->source_id_activity_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**|  | 
 **activity_id** | **str**|  | 

### Return type

[**Activity**](Activity.md)

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
api_instance = swagger_client.ActivityApi()
source_id = 56 # int | 
activity_id = 'activity_id_example' # str | 
activity_import = swagger_client.ModelImport() # ModelImport | 

try: 
    # Create or update this activity
    api_response = api_instance.source_id_activity_id_put(source_id, activity_id, activity_import)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->source_id_activity_id_put: %s\n" % e)
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

# **source_id_activity_id_tags_patch**
> Activity source_id_activity_id_tags_patch(source_id, activity_id, body)

Modify tags of activity

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
api_instance = swagger_client.ActivityApi()
source_id = 56 # int | 
activity_id = 'activity_id_example' # str | 
body = swagger_client.TagChangeSet() # TagChangeSet | 

try: 
    # Modify tags of activity
    api_response = api_instance.source_id_activity_id_tags_patch(source_id, activity_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->source_id_activity_id_tags_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**|  | 
 **activity_id** | **str**|  | 
 **body** | [**TagChangeSet**](TagChangeSet.md)|  | 

### Return type

[**Activity**](Activity.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

