# V2Doc

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  文档 ID | [optional] 
**type** | **str** |  文档类型 (Doc:普通文档, Sheet:表格, Thread:话题, Board:图集, Table:数据表) | [optional] 
**slug** | **str** |  路径 | [optional] 
**title** | **str** |  标题 | [optional] 
**description** | **str** |  摘要 | [optional] 
**cover** | **str** |  封面 | [optional] 
**user_id** | **int** |  归属用户/团队 ID | [optional] 
**book_id** | **int** |  归属知识库 ID | [optional] 
**last_editor_id** | **int** |  最后编辑者 ID | [optional] 
**public** | **int** |  公开性 (0:私密, 1:公开, 2:企业内公开) | [optional] 
**status** | **str** |  状态 (0:草稿, 1:发布) | [optional] 
**likes_count** | **int** |  点赞数 | [optional] 
**read_count** | **int** |  阅读数   - 需要传入 &#x60;optional_properties&#x3D;hits&#x60; 获取   | [optional] 
**hits** | **int** |  阅读数   - 需要传入 &#x60;optional_properties&#x3D;hits&#x60; 获取   | [optional] 
**comments_count** | **int** |  评论数 | [optional] 
**word_count** | **int** |  内容字数 | [optional] 
**created_at** | **datetime** |  创建时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**updated_at** | **datetime** |  更新时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**content_updated_at** | **datetime** |  内容更新时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**published_at** | **datetime** |  发布时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**first_published_at** | **datetime** |  首次发布时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**book** | [**V2Book**](V2Book.md) |  | [optional] 
**user** | [**V2User**](V2User.md) |  | [optional] 
**last_editor** | [**V2User**](V2User.md) |  | [optional] 
**latest_version_id** | **int** |  最新已发版本 ID   - 需要传入 &#x60;optional_properties&#x3D;latest_version_id&#x60; 获取   | [optional] 
**tags** | [**V2Tag**](V2Tag.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

