JSON_TEMPLATE_START = """I will give you user input. Based on the input, determine the values of the parameters. Parameter information are listed below with format: 
parameter name; parameter data type; default value; description; example
Here is the parameter information:"""
JSON_TEMPLATE_MIDDLE = "Based on the user input, return a JSON object containing the values of the parameters. Here is an example:"
JSON_TEMPLATE_END = "Note that we return null in the JSON output for the parameters that are not specified in the user input."


SET_ALARM_HISTORY_PARAM = (
    JSON_TEMPLATE_START
    + """
```
index; int; null; 告警序号; 1
status; int; null; 告警状态, 1为已处理, 2为误报, 3为临时撤防; 3
```
"""
    + JSON_TEMPLATE_MIDDLE
    + """
Input: 将1号设置为临时撤防
Output:
{
  "index": 1,
  "status": 3
}
"""
    + JSON_TEMPLATE_END
)

SEARCH_SMART_INSPECTION_PARAM = (
    JSON_TEMPLATE_START
    + """
```
patrolName; string; null; 巡检名称; "火灾演练"
patrolDate; string; null; 巡检日期, 年份默认2023, 时间格式为yyyy-MM-dd; "2023-01-01"
startTime; string; null; 巡检开始时间, 时间格式为HH:mm; "14:00"
finishTime; string; null; 巡检结束时间, 时间格式为HH:mm; "14:30"
personId; string; null; 人员id; "30"
```
Here are some id and name information:
personId; personName
30; 张三
41; 李四
43; 王五
"""
    + JSON_TEMPLATE_MIDDLE
    + """
Input: 搜索张三在六月十号的巡检记录
Output:
{
    "patrolName": null,
    "patrolDate": "2023-06-10",
    "startTime": null,
    "finishTime": null,
    "personId": "30"
"""
    + JSON_TEMPLATE_END
)

ADD_FENCE_STRATEGY_PARAM = (
    JSON_TEMPLATE_START
    + """
```
alarmUser; string; null; 告警人员Id; "152"
config; string; null; 告警配置; "1"
fenceCode; string; null; 有效区域; "636711427704356864"
forbidden; int; null; 策略行为; 0
level; int; null; 告警级别; 1
strategyName; string; null; 策略名称; "会议室区域策略"
remark; string; null; 策略描述; "会议室区域的策略, 特定时间段内禁止进入"
strategyUserId; string; null; 关联人员Id; "200"
startTime; string; null; 开始时间, 时间格式为HH:mm;
finishTime; string; null; 结束时间, 时间格式为HH:mm;
timeValue; string; null; 重复的星期几, 1-6分别代表周一到周六, 0代表周日; "1,2,5"
```
Here are some id and name information:
alarmUser; alarmUserName
4; 超级管理员
7; 张三
151; 乾坤物联
152; 测试

config; configName
1; 声音
2; 弹窗框
3; 震动
4; 视频

fenceCode; fenceName
636711427704356864; 前台
637119776958709760; 会议室

forbidden; forbiddenName
0; 禁止进入
1; 禁止离开

level; levelName
0; 提示
1; 普通
2; 严重

strategyUserId; strategyUserName
100; qk科技
200; 全厂
300; 办公楼区
"""
    + JSON_TEMPLATE_MIDDLE
    + """
Input: 策略名称是会议室区域策略, 设置告警用户是乾坤物联, 告警配置为弹出框告警, 设置策略行为是禁止进入, 告警级别是普通, 关联的用户是办公楼区, 设置有效区域为会议室, 有效时间是早上的8点开始到早上的9点结束, 重复日期为每周一到周五，备注策略描述是会议室区域的策略，特定时间段内禁止进入。
Output:
{
  "alarmUser": "151",
  "config": "2",
  "fenceCode": "637119776958709760",
  "forbidden": 0,
  "level": 1,
  "strategyName": "会议室区域策略",
  "remark": "会议室区域的策略, 特定时间段内禁止进入",
  "strategyUserId": "300",
  "startTime": "08:00",
  "finishTime": "09:00",
  "timeValue": "1,2,3,4,5"
}
"""
    + JSON_TEMPLATE_END
)


ADD_INSPECTION_STRATEGY_PARAM = (
    JSON_TEMPLATE_START
    + """
```
patrolName; string; null; 巡检名称; "晨检"
personIds; string; null; 巡检人员Ids; "1,2,3"
fenceIds; string; null; 巡检区域Ids; "1,2"
passDotCount; int; null; 每个区域打点的数量视为通过; 3
sortFlag; int; null; 是否有序, 1为有序, 0为无序; 1
repeatType; int; null; 是否重复, 1为重复, 0为不重复. 重复时要设置startTime和finishTime, 时间格式HH:mm. 选中不重复时, 有效时间段为: onceStartTime和onceFinishTime, 时间格式为yyyy-MM-dd HH:mm:ss
timeValue; string; null; 只在repeatType为1时有效, 重复的星期几, 1-6分别代表周一到周六, 0代表周日; "1,2,5"
onceStartTime; string; null; 只在repeatType为0时有效, 有效时间段的开始时间, 时间格式为yyyy-MM-dd HH:mm:ss;
onceFinishTime; string; null; 只在repeatType为0时有效, 有效时间段的结束时间, 时间格式为yyyy-MM-dd HH:mm:ss;
startTime; string; null; 只在repeatType为1时有效, 重复的开始时间, 时间格式为HH:mm;
finishTime; string; null; 只在repeatType为1时有效, 重复的结束时间, 时间格式为HH:mm;
```
Here are some id and name information:
personId; personName
30; 张三
41; 李四
43; 王五

fenceId; fenceName
1; 前台
4; 会议室
6; 仓储室
"""
    + JSON_TEMPLATE_MIDDLE
    + """
Input: 名称是夜检, 人员要张三和李四, 巡检区域是仓储和前台. 周一到周四每天晚上八点到九点半重复巡检
Output:
{
  "patrolName": "夜检",
  "personIds": "30,41",
  "fenceIds": "6,1",
  "passDotCount": null,
  "sortFlag": null,
  "repeatType": 1,
  "timeValue": "1,2,3,4",
  "onceStartTime": null,
  "onceFinishTime": null,
  "startTime": "20:00",
  "finishTime": "21:30"
}
"""
    + JSON_TEMPLATE_END
)
