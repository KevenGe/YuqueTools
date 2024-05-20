# V2Book

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  知识库 ID | [optional] 
**type** | **str** |  类型 (Book:文档, Design:图集, Sheet:表格, Resource:资源) | [optional] 
**slug** | **str** |  路径 | [optional] 
**name** | **str** |  名称 | [optional] 
**user_id** | **int** |  归属用户/团队 ID | [optional] 
**description** | **str** |  简介 | [optional] 
**creator_id** | **int** |  创建者 ID | [optional] 
**public** | **int** |  公开性 (0:私密, 1:公开, 2:企业内公开) | [optional] 
**items_count** | **int** |  文档数量 | [optional] 
**likes_count** | **int** |  点赞数量 | [optional] 
**watches_count** | **int** |  订阅数量 | [optional] 
**content_updated_at** | **datetime** |  知识库 META 更新时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**created_at** | **datetime** |  创建时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**updated_at** | **datetime** |  更新时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**user** | [**V2User**](V2User.md) |  | [optional] 
**namespace** | **str** |  完整路径 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

