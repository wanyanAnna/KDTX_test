# KDTX_test
## 接口测试自动化项目-----客达天下（销售管理系统）
### 本项目基于黑马程序员教程创建,主要测试网站(http://kdtx-test.itheima.net)中的登录和课程管理功能的接口
* 接口自动化测试框架：pytest
* http请求发送：requests
* 测试报告：allure-pytest
#### kdtx_xmind
此文件夹包含测试点（.xmind）和测试用例（.xls）,以及接口文档
#### ApiTest
接口自动化测试脚本
* `#..config`文件夹下的data.yaml 对测试数据进行管理，通过读取yaml的数据后当做接口的参数进行传参；settings.ini 存放测试网站的域名，便于后续更改。
* `#..test_case`文件下存放的测试用例，包括`.login_center`登录接口,`.add_center`增加课程接口,`.del_center`删除课程接口,`.modify_center`修改课程接口，`.search_center`查询课程接口。
