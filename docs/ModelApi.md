# swagger_client.ModelApi

All URIs are relative to *https://localhost/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**model_get**](ModelApi.md#model_get) | **GET** /model/ | Get all models of user
[**model_model_id_get**](ModelApi.md#model_model_id_get) | **GET** /model/{model_id} | Get meta information about a trained model
[**model_prediction_post**](ModelApi.md#model_prediction_post) | **POST** /model/prediction | Get prediction for a provided text based on the best model for source/tagset
[**model_search_post**](ModelApi.md#model_search_post) | **POST** /model/search | Get meta information about a trained model
[**model_train_post**](ModelApi.md#model_train_post) | **POST** /model/train | Train a new model for a tagset


# **model_get**
> ModelList model_get()

Get all models of user

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
api_instance = swagger_client.ModelApi()

try: 
    # Get all models of user
    api_response = api_instance.model_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->model_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelList**](ModelList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_model_id_get**
> Model model_model_id_get(model_id)

Get meta information about a trained model

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
api_instance = swagger_client.ModelApi()
model_id = 'model_id_example' # str | The id of this model

try: 
    # Get meta information about a trained model
    api_response = api_instance.model_model_id_get(model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->model_model_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| The id of this model | 

### Return type

[**Model**](Model.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_prediction_post**
> TextPrediction model_prediction_post(body, model_id=model_id)

Get prediction for a provided text based on the best model for source/tagset

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
api_instance = swagger_client.ModelApi()
body = swagger_client.TextPredictionQuery() # TextPredictionQuery | 
model_id = 'model_id_example' # str | The id of this model (optional)

try: 
    # Get prediction for a provided text based on the best model for source/tagset
    api_response = api_instance.model_prediction_post(body, model_id=model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->model_prediction_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TextPredictionQuery**](TextPredictionQuery.md)|  | 
 **model_id** | **str**| The id of this model | [optional] 

### Return type

[**TextPrediction**](TextPrediction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_search_post**
> Model model_search_post(body)

Get meta information about a trained model

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
api_instance = swagger_client.ModelApi()
body = swagger_client.ModelQuery() # ModelQuery | 

try: 
    # Get meta information about a trained model
    api_response = api_instance.model_search_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->model_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelQuery**](ModelQuery.md)|  | 

### Return type

[**Model**](Model.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_train_post**
> Job model_train_post(body, fast=fast)

Train a new model for a tagset

If now sources are specified it will be trained on all sources

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
api_instance = swagger_client.ModelApi()
body = swagger_client.ModelTrainJob() # ModelTrainJob | 
fast = true # bool | Reuse model parameters and only use data (optional) (default to true)

try: 
    # Train a new model for a tagset
    api_response = api_instance.model_train_post(body, fast=fast)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->model_train_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelTrainJob**](ModelTrainJob.md)|  | 
 **fast** | **bool**| Reuse model parameters and only use data | [optional] [default to true]

### Return type

[**Job**](Job.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

