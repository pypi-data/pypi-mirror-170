## py_wechat_tools简介

集成微信小程序/公众号自用接口功能库

打造一个更简洁，更好用的微信SDK


## 快速使用

首先实例化

    from py_wechat_tools import MPTools

    wx = MPTools(
        appid="appid",
        secret="secret",
    )

以登录授权接口为例，一行代码搞定登录接口

    # js_code为小程序调用wx.login()获取的code
    wx.code2session(js_code="0936ry000b8c4O1S5f300RnDwB06ry0x")

获取手机号码的简单用法

    # 注意：此code是手机号码授权获取的code，不是wx.loginx()获取的code
    wx.get_phone_number(code)

用过微信获取手机号码这个接口的同学一定知道，微信接口里，我们需要获取access_token，然后才能调用get_phone_number接口，
然而这里直接省略了access_token，是因为MPTools类内部实现了access_token缓存机制，
当access_token不存在或过期时，会自动从微信接口中更新access_token，并且缓存起来。当然，如果你不需要这个功能，可以通过配置
passive_access_token=False 配置关闭。

* 提示：如果关掉自动更新access_token功能，您就必须自己维护access_token的有效状态，可通过 [get_access_token()](#获取AccessToken) 方法获取，通过
[set_access_token()](wx.set_access_token()) 方法设置access_token

* 小心access_token打架：如果是多环境或者多服务的情况下，不推荐托管access_token，因为两个以上的环境同时使用会导致access_token冲突。举个例子，比如dev环境获取了access_token。test环境发现自己没有access_token（两个环境数据隔离的情况下），会重新获取，test这么一取不要紧，可是得罪了dev。因为重新access_token获取会导致旧的access_token失效。dev也不甘示弱，发现他自己的access_token过期了，立马就获取新的access_token，这么一来二去不就打起来了吗。

* 解决acceess_token冲突方案：做一个集中获取access_token的途径，比如其中一个环境/服务专门管理access_token，其他环境/服务从它那里获取。

需要注意的是，这里使用的是cacheout缓存，cacheout缓存是缓存在内存中的，就是说重启之后缓存失效。
MPTools也提供了修改缓存方式的方法，用法请移步：[修改缓存方式](#修改缓存方式)


## MPTools初始化参数解释

    wx = MPTools(
        # 填写小程序或公众号appid以及secret
        appid="appid",
        secret="secret",

        # debug模式，默认False，为True时日志输出为debug级别，也可在日志的配置项中配置
        debug=False,

        # access_token失效(缓存过期)后是否自动更新，开启后，如果遇到42001(调用接口凭证已过期)就会重新调get_access_token接口获取
        # 如果关闭该功能，必须要从实例化传入access_token或者使用wx.set_access_token(access_token)方法设置，获取access_token方法请往下看
        passive_access_token=True,

        # 优先级最高，如果传入access_token，MPTools将会使用该access_token
        access_token=None
    )


## 内部方法

### wx.set_access_token()

通过该方法给MPTools传入一个access_token

passive_access_token=False时，使用小程序接口前必须先设置access_token

    wx.set_access_token(access_token)


### wx.set_cache_obj(cache_obj)

通过该方法传入一个缓存的实例化对象/方法，简单的修改MPTools默认缓存方式
该方式修改的缓存方法必须包含.get()获取缓存和.set()设置缓存方法。
    
    # 如，修改为Django的缓存
    from django.core.cache import cache
    wx.set_cache_obj(cache)




## MPTools高级用法

通过重写MPTools定制更多功能

### 1.修改缓存方式
如果你不想使用cacheout缓存方式，可以修改其他缓存方式，如Django的缓存，继承MPTools类，重写get_cache()方法即可，但需要注意的是，
设置缓存和获取缓存时默认使用的是cache.set()和cache.get()方法，如果你使用的缓存没有这两个方法，
就必须要重写get_access_token_cache()方法了，具体请看[重写缓存方法](#2.重写缓存方法)。

如：改为Django的缓存方法

    from py_wechat_tools import MPTools
    from django.core.cache import cache
    
    class MyWxTools(MPTools):
        def get_cache(self):
            return cache  # 必须返回缓存对象的实例，能调用cache.get()方法


### 2.重写缓存方法
更深度定制缓存方法，重写这个方法可以自定义缓存，最后返回一个获取到的access_token即可
如果重写get_access_token_cache()方法，就没必要重写get_cache()方法了

依然用Ddjango缓存为例，

    from py_wechat_tools import MPTools
    from django.core.cache import cache

    class MyWxTools(MPTools):

        def get_access_token_cache(self):
            """ 实现获取access_token --> 缓存access_token过程 """ 

            access_token = cache.get("access_token")
            if not access_token:
                access_token = self.get_access_token()
                cache.set("access_token", access_token, 2 * 60 * 60)

            # 必须返回 access_token
            return access_token




### 3.重写日志输出方法

日志使用的是logging，日志功能仅实现了基础功能。

    from py_wechat_tools import MPTools
    from py_wechat_tools.libs.tools import LogsConf

    class MyWxTools(MPTools):

        def get_logs_conf(self):
            return LogsConf(
                name="project_log",  # 日志输出的名称
                level=DEBUG,  # 日志级别，默认LogsConf.DEBUG级别，可设置LogsConf.INFO等级别
                file_path=None,  # 日志输出到文件的路径(绝对路径/相对路径,相对项目)，为None不输出日志，
                # 日志输出的格式， 可参考logging的格式
                formatter="'%(asctime)s - %(name)s..%(filename)s.%(lineno)d - %(levelname)s: %(message)s'",
                stream_handler=True  # 是否输出到终端，默认True， file_path和stream_handler必须选一个以上
            )

## 小程序接口

可参考 [微信官方文档](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/login/auth.code2Session.html)

#### WeChatDate类型说明：
所有WeChatDate类型的数据都包含以下参数，后面不再声明

    WeChatDate都可以调用以下参数：
        属性              类型              说明
        errcode         number          错误码，正常时返回0
        errmsg          string          错误描述，正常时返回ok


### 授权相关

#### code2Session（登录）
通过code换取session、openid、unionid

    we_chat_data = wx.code2session(js_code)
    
    传参：
        属性              类型              说明
        js_code         string          通过小程序调用wx.login()获取的code

    返回(WeChatDate类型)：
        属性              类型              说明
        openid          string          微信唯一id
        session_key     string          会话密钥
        unionid         string          用户在开放平台的唯一标识符，若当前小程序已绑定到微信开放平台帐号下会返回


#### 获取AccessToken
获取access_token(调用接口凭证)

    we_chat_data = wx.get_access_token()

    返回(WeChatDate类型)：
        属性                  类型              说明
        access_token        string          获取到的调用接口凭证
        expires_in          string          有效时长




#### checkEncryptedData（检查加密信息是否由微信生成）
检查加密信息是否由微信生成（当前只支持手机号加密数据），只能检测最近3天生成的加密数据

    we_chat_data = wx.check_encrypted_data(encrypted_msg_hash)

    传参：
        属性                      类型              说明
        encrypted_msg_hash      string          加密数据的sha256，通过Hex（Base16）编码后的字符串

    返回(WeChatDate类型)：
        属性                      类型              说明
        vaild                   string          是否是合法的数据
        create_time             number	        加密数据生成的时间戳



#### getPaidUnionId（用户支付完成后，获取该用户的 UnionId）
用户支付完成后，获取该用户的 UnionId，无需用户授权。本接口支持第三方平台代理查询。

    we_chat_data = wx.get_paid_union_id(openid, transaction_id=None, mch_id=None, out_trade_no=None)

    以下两种方式任选其一。
    1、微信支付订单号（transaction_id）
    2、微信支付商户订单号和微信支付商户号（out_trade_no 及 mch_id）

    传参：
        属性                      类型              说明
        openid                  string          支付用户唯一标识
        transaction_id          string          微信支付订单号（方法1必填）
        mch_id                  string          微信支付分配的商户号，和商户订单号配合使用（方法2必填）
        out_trade_no            string          微信支付商户订单号，和商户号配合使用（方法2必填）


    返回(WeChatDate类型)：
        属性                      类型              说明
        vaild                   string          是否是合法的数据
        create_time             number	        加密数据生成的时间戳




#### getPluginOpenPId（换取插件用户的唯一标识 openpid）
通过 wx.pluginLogin 接口获得插件用户标志凭证 code 后传到开发者服务器，开发者服务器调用此接口换取插件用户的唯一标识 openpid。

    we_chat_data = wx.get_plugin_open_pid(code)

    传参：
        属性                      类型              说明
        code                    string          通过 wx.pluginLogin 接口获得插件用户标志凭证 code


    返回(WeChatDate类型)：
        属性                      类型              说明
        vaild                   string          是否是合法的数据
        create_time             number	        加密数据生成的时间戳



#### getPhoneNumber
获取用户手机号码

    we_chat_data = wx.get_phone_number(code)

    传参：
        属性                      类型              说明
        code                    string          通过getPhoneNumber方法获取的手机号码专用code

    返回(WeChatDate类型)：
        属性                  类型              说明
        errcode             number	        错误码
        errmsg              string	        错误提示信息
        phone_info          WeChatDate      用户手机号信息

    phone_info: 用户手机号信息
        属性                  类型              说明
        phoneNumber	        string	        用户绑定的手机号（国外手机号会有区号）
        purePhoneNumber	    string	        没有区号的手机号
        countryCode	        string	        区号
        watermark	        WeChatDate	    数据水印
    
    watermark：数据水印
        属性                  类型              说明
        appid	            string	        小程序appid
        timestamp	        number	        用户获取手机号操作的时间戳


### 数据分析

#### getDailyRetain
获取用户访问小程序日留存

    we_chat_data = wx.get_daily_retain(begin_date, end_date=None)

    传参：
        属性                  类型              说明
        begin_date          string          开始日期 格式：yyyymmdd
        end_date            string          [选填]结束日期，限定查询1天数据，允许设置的最大值为昨日 格式：yyyymmdd。不传时默认与开始日期相同

    返回(WeChatDate类型)：
        属性                  类型              说明
        ref_date	        string          日期
        visit_uv_new	    WeChatDate      新增用户留存
        visit_uv	        WeChatDate      活跃用户留存
    
    visit_uv_new 的结构
        属性	                  类型	           说明
        key                 number	        标识，0开始，表示当天，1表示1天后。依此类推，key取值分别是：0,1,2,3,4,5,6,7,14,30
        value	            number	        key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）
    
    visit_uv 的结构    
        属性	                类型	                说明
        key	                number	        标识，0开始，表示当天，1表示1天后。依此类推，key取值分别是：0,1,2,3,4,5,6,7,14,30
        value	            number          key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）



#### getMonthlyRetain
获取用户访问小程序月留存

    we_chat_data = wx.get_monthly_retain(begin_date, end_date=None)

    传参：
        属性                  类型              说明
        begin_date          string          开始日期，必须为每个月的第一天，格式：yyyymmdd 
        end_date            string          [选填]结束日期，必须为每个月的最后一天，默认为月份最后一天，格式：yyyymmdd 

    返回(WeChatDate类型)：
        属性                  类型              说明
        ref_date	        string          日期
        visit_uv_new	    WeChatDate      新增用户留存
        visit_uv	        WeChatDate      活跃用户留存
    
    visit_uv_new 的结构
        属性	                  类型	           说明
        key                 number	        标识，0开始，表示当月，1表示1月后。key取值分别是：0,1
        value	            number	        key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）
    
    visit_uv 的结构    
        属性	                类型	                说明
        key	                number	        标识，0开始，表示当月，1表示1月后。key取值分别是：0,1
        value	            number          key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）



#### getWeeklyRetain
获取用户访问小程序周留存

    we_chat_data = wx.get_weekly_retain(begin_date, end_date=None)

    传参：
        属性                  类型              说明
        begin_date          string          开始日期，必须为周一的日期。 格式：yyyymmdd
        end_date            string          [选填]结束日期，为周日日期，限定查询一周数据。默认周日 格式：yyyymmdd

    返回(WeChatDate类型)：
        属性                  类型              说明
        ref_date	        string          日期
        visit_uv_new	    WeChatDate      新增用户留存
        visit_uv	        WeChatDate      活跃用户留存
    
    visit_uv_new 的结构
        属性	                  类型	           说明
        key                 number	        标识，0开始，表示当周，1表示1周后。依此类推，取值分别是：0,1,2,3,4
        value	            number	        key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）
    
    visit_uv 的结构    
        属性	                类型	                说明
        key	                number	        标识，0开始，表示当周，1表示1周后。依此类推，取值分别是：0,1,2,3,4
        value	            number          key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）



#### getDailySummary
获取用户访问小程序数据概况

    we_chat_data = wx.get_daily_summary(begin_date, end_date=None)

    传参：
        属性                  类型              说明
        begin_date          string          开始日期。格式为 yyyymmdd
        end_date            string          [选填]结束日期，限定查询1天数据，允许设置的最大值为昨日。格式yyyymmdd。不传时默认与开始日期相同

    返回(WeChatDate类型)：
        属性                  类型              说明
        list	            Array           数据列表
    
    list 的结构
        属性	                  类型	           说明
        ref_date	        string	        日期，格式为 yyyymmdd
        visit_total	        number	        累计用户数
        share_pv	        number	        转发次数
        share_uv	        number	        转发人数


#### getDailyVisitTrend
获取用户访问小程序数据日趋势

    we_chat_data = wx.get_daily_visit_trend(begin_date, end_date=None)

    传参：
        属性                  类型              说明
        begin_date          string          开始日期，为周一日期。 格式：yyyymmdd
        end_date            string          [选填]结束日期，限定查询1天数据，允许设置的最大值为昨日。格式为yyyymmdd。不传时默认与开始日期相同

    返回(WeChatDate类型)：
        属性                  类型              说明
        list	            Array           数据列表
    
    list 的结构
        属性	                  类型	           说明
        ref_date	        string	        日期，格式为 yyyymmdd
        session_cnt	        number	        打开次数
        visit_pv	        number	        访问次数
        visit_uv	        number	        访问人数
        visit_uv_new	    number	        新用户数
        stay_time_uv	    number	        人均停留时长 (浮点型，单位：秒)
        stay_time_session	number	        次均停留时长 (浮点型，单位：秒)
        visit_depth	        number	        平均访问深度 (浮点型)


#### getMonthlyVisitTrend
获取用户访问小程序数据月趋势(能查询到的最新数据为上一个自然月的数据)

    we_chat_data = wx.get_monthly_visit_trend(begin_date, end_date=None)

    传参：
        属性                  类型              说明
        begin_date          string          开始日期，为周一日期。 格式：yyyymmdd
        end_date            string          [选填]结束日期，必须为每个月的最后一天，默认为月份最后一天，格式：yyyymmdd 

    返回(WeChatDate类型)：
        属性                  类型              说明
        list	            Array           数据列表
    
    list 的结构
        属性	                  类型	           说明
        ref_date	        string	        时间，格式为 yyyymm，如："201702"
        session_cnt	        number	        打开次数（自然月内汇总）
        visit_pv	        number	        访问次数（自然月内汇总）
        visit_uv	        number	        访问人数（自然月内去重）
        visit_uv_new	    number	        新用户数（自然月内去重）
        stay_time_uv	    number	        人均停留时长 (浮点型，单位：秒)
        stay_time_session	number	        次均停留时长 (浮点型，单位：秒)
        visit_depth	        number	        平均访问深度 (浮点型)


#### getWeeklyVisitTrend
获取用户访问小程序数据周趋势

    we_chat_data = wx.get_weekly_visit_trend(begin_date, end_date=None)

    传参：
        属性                  类型              说明
        begin_date          string          开始日期，为周一日期。 格式：yyyymmdd
        end_date            string          [选填]结束日期，限定查询1天数据，允许设置的最大值为昨日。格式为yyyymmdd。不传时默认与开始日期相同

    返回(WeChatDate类型)：
        属性                  类型              说明
        list	            Array           数据列表
    
    list 的结构
        属性	                  类型	           说明
        ref_date	        string	        时间，格式为 yyyymmdd-yyyymmdd，如："20170306-20170312"
        session_cnt	        number	        打开次数（自然周内汇总）
        visit_pv	        number	        访问次数（自然周内汇总）
        visit_uv	        number	        访问人数（自然周内去重）
        visit_uv_new	    number	        新用户数（自然周内去重）
        stay_time_uv	    number	        人均停留时长 (浮点型，单位：秒)
        stay_time_session	number	        次均停留时长 (浮点型，单位：秒)
        visit_depth	        number	        平均访问深度 (浮点型)


### 图像处理

#### aiCrop
本接口提供基于小程序的图片智能裁剪能力。

    we_chat_data = wx.ai_crop(img_url=None, img=None)

    传参：
        属性                  类型              说明
        img_url             string          要检测的图片 url，传这个则不用传 img 参数
        img                 string          form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。

    返回(WeChatDate类型)：
        属性              类型              说明
        results         array           智能裁剪结果
        img_size        objects         图片大小

    results:    智能裁剪结果
        属性              类型              说明
        crop_left       number
        crop_top        number
        crop_right      number
        crop_bottom     number

    img_size:   图片大小
        属性              类型              说明
        w               number
        y               number


#### scanQRCode
本接口提供基于小程序的条码/二维码识别的API。

    we_chat_data = wx.scan_qr_code(img_url=None, img=None)

    传参：
        属性                  类型              说明
        img_url             string          要检测的图片 url，传这个则不用传 img 参数
        img                 string          中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。

    返回(WeChatDate类型)：
        属性              类型              说明
        code_results    array           扫码结果
        img_size        objects         图片大小

    code_results:
        属性              类型              说明
        type_name       QR_CODE         类型，QR_CODE、EAN_13、CODE_128
        data            str             二维码/条形码包含的内容
        pos             WeChatDate      坐标位置，仅二维码包含该字段

    pos:
        属性              类型              说明
        left_top       WeChatDate         左上角
        right_top      WeChatDate         右上角
        right_bottom   WeChatDate         右下角
        left_bottom    WeChatDate         左下角

    left_top、right_top、right_bottom、left_bottom:
        属性              类型              说明
        x               number           x坐标
        y               number           y坐标

    img_size:   图片大小
        属性              类型              说明
        x               number           x坐标
        y               number           y坐标


#### superresolution
本接口提供基于小程序的图片高清化能力。
效果嘛，约等于没处理，贴出对比图供参考

<img src="./docs/diff.png" width="500" alt="图片高清化接口对比图"/>

点击查看大图

    we_chat_data = wx.superresolution(img_url=None, img=None)

    传参：
        属性                  类型              说明
        img_url             string          要检测的图片 url，传这个则不用传 img 参数
        img                 string          中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。

    返回(WeChatDate类型)：
        属性              类型              说明
        media_id        string          用于获取临时素材接口，有效期为3天


#### 获取临时素材接口

    we_chat_data = wx.get_media(media_id, file_path_name=None

    传参：
        属性                  类型              说明
        media_id            string          媒体id
        file_path_name      string          [选填]文件绝对路径和名称，如果传该值，接口会保存图片到该路径

    返回
        1、file_path_name为None时返回图片二进制，
        2、file_path_name不为None时返回"ok"，并将图片输出到file_path_name



### ORC
这部分接口都需要在 [微信服务市场](https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415) 购买，
有免费的100次/天的套餐，测试够用了。


#### bankcard
银行卡 OCR 识别

    we_chat_data = wx.bankcard(img_url=None, img=None)

    传参：
        属性                  类型              说明
        img_url             string          要检测的图片 url，传这个则不用传 img 参数
        img                 string          中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。

    返回(WeChatDate类型)：
        属性              类型              说明
        number	        number	        银行卡号（id）


#### businessLicense
营业执照 OCR 识别

    we_chat_data = wx.business_license(img_url=None, img=None)

    传参：
        属性                  类型              说明
        img_url             string          要检测的图片 url，传这个则不用传 img 参数
        img                 string          中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。

    返回(WeChatDate类型)：
        属性              类型              说明
        reg_num	                string	            注册号
        serial	                string	            编号
        legal_representative    string	            法定代表人姓名
        enterprise_name	        string	            企业名称
        type_of_organization	string	            组成形式
        address	                string	            经营场所/企业住所
        type_of_enterprise	    string	            公司类型
        business_scope	        string	            经营范围
        registered_capital	    string	            注册资本
        paid_in_capital	        string	            实收资本
        valid_period	        string	            营业期限
        registered_date	        string	            注册日期/成立日期
        cert_position	        string	            营业执照位置
        img_size	            string	            图片大小


#### driverLicense
驾驶证 OCR 识别
效果一般，有个别字识别错误。还是比较清晰的文字

    we_chat_data = wx.driver_license(img_url=None, img=None)

    传参：
        属性                  类型              说明
        img_url             string          要检测的图片 url，传这个则不用传 img 参数
        img                 string          中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。

    返回(WeChatDate类型)：
        属性              类型              说明
        id_num	        string	        证号
        name	        string	        姓名
        sex	            string	        性别
        address	        string	        地址
        birth_date	    string	        出生日期
        issue_date	    string	        初次领证日期
        car_class	    string	        准驾车型
        valid_from	    string	        有效期限起始日
        valid_to	    string	        有效期限终止日
        official_seal	string	        印章文构


#### vehicleLicense
行驶证 OCR 识别

    we_chat_data = wx.vehicle_license(img_url=None, img=None)

    传参：
        属性                  类型              说明
        img_url             string          要检测的图片 url，传这个则不用传 img 参数
        img                 string          中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。

    返回(WeChatDate类型)：
        属性              类型              说明
        vehicle_type	                string	        车辆类型
        owner	                        string	        所有人
        addr	                        string	        住址
        use_character	                string	        使用性质
        model	                        string	        品牌型号
        vin	                            string	        车辆识别代
        engine_num	                    string	        发动机号码
        register_date	                string	        注册日期
        issue_date	                    string	        发证日期
        plate_num_b	                    string	        车牌号码
        record	                        string	        号牌
        passengers_num	                string	        核定载人数
        total_quality	                string	        总质量
        totalprepare_quality_quality	string	        整备质量


#### idcard
身份证 OCR 识别

    we_chat_data = wx.idcard(img_url=None, img=None)

    传参：
        属性                  类型              说明
        img_url             string          要检测的图片 url，传这个则不用传 img 参数
        img                 string          中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。

    返回(WeChatDate类型)：
        属性              类型              说明
        type	        string	        正面或背面，Front / Back

        # 背面返回字段
        valid_date	    string	        有效期

        # 正面返回字段
        name	        string	        姓名
        id	            string	        证号
        addr	        string	        地址
        gender	        string	        性别
        nationality	    string	        民族



#### printedText
通用印刷体 OCR 识别

    we_chat_data = wx.idcard(img_url=None, img=None)

    传参：
        属性                  类型              说明
        img_url             string          要检测的图片 url，传这个则不用传 img 参数
        img                 string          中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。

    返回(WeChatDate类型)：
        属性              类型              说明
        items           array           识别结果
        img_size        objects         图片大小

    items:
        属性              类型              说明
        text            string          识别到的文本
        pos             WeChatDate      坐标位置，仅二维码包含该字段

    pos:
        属性              类型              说明
        left_top       WeChatDate         左上角
        right_top      WeChatDate         右上角
        right_bottom   WeChatDate         右下角
        left_bottom    WeChatDate         左下角

    left_top、right_top、right_bottom、left_bottom:
        属性              类型              说明
        x               number           x坐标
        y               number           y坐标

    img_size:   图片大小
        属性              类型              说明
        x               number           x坐标
        y               number           y坐标


### 内容安全


#### mediaCheckAsync
异步校验图片/音频是否含有违法违规内容。

    we_chat_data = wx.media_check_async(media_url, media_type, openid, scene=1)

    传参：
        属性                  类型              说明
        media_url             string          要检测的图片或音频的url，支持图片格式包括 jpg , jepg, png, bmp, gif（取首帧），
                                              支持的音频格式包括mp3, aac, ac3, wma, flac, vorbis, opus, wav
        media_type            number          1:音频;2:图片
        openid                string          用户的openid（用户需在近两小时访问过小程序）
        scene                 number          场景枚举值（1 资料；2 评论；3 论坛；4 社交日志）

    返回(WeChatDate类型)：
        属性	            类型	            说明
        trace_id        string          唯一请求标识，标记单次请求，用于匹配异步推送结果



#### mediaCheckAsync
异步校验图片/音频是否含有违法违规内容。

不建议使用该接口作为可信任的检测，色情图片大致上能识别出来（别问哪来的色情图片），涉政图片很多没法识别。

    we_chat_data = wx.media_check_async(media_url, media_type, openid, scene=1)

    传参：
        属性                  类型              说明
        media_url             string          要检测的图片或音频的url，支持图片格式包括 jpg , jepg, png, bmp, gif（取首帧），
                                              支持的音频格式包括mp3, aac, ac3, wma, flac, vorbis, opus, wav
        media_type            number          1:音频;2:图片
        openid                string          用户的openid（用户需在近两小时访问过小程序）
        scene                 number          场景枚举值（1 资料；2 评论；3 论坛；4 社交日志）

    返回(WeChatDate类型)：
        属性	            类型	            说明
        trace_id        string          唯一请求标识，标记单次请求，用于匹配异步推送结果


#### 异步校验通知方法

    we_chat_data = wx.media_check_async_notify(data)

    传参：
        属性                  类型              说明
        data                string           通知接口接收到的数据

    返回(WeChatDate类型)：
        属性              类型              说明
        ToUserName	    string	        小程序的username
        FromUserName	string	        平台推送服务UserName
        CreateTime	    number	        发送时间
        MsgType	        string	        默认为：Event
        Event	        string	        默认为：wxa_media_check
        appid	        string	        小程序的appid
        trace_id	    string	        任务id
        version	        number	        可用于区分接口版本
        result	        object	        综合结果
        detail	        array	        详细检测结果
        
    detail包含多个策略类型的检测结果，策略类型的检查结果可能存在的属性如下
        属性              类型              说明
        strategy	    string	        策略类型
        errcode	        number	        错误码，仅当该值为0时，该项结果有效
        suggest	        string	        建议，有risky、pass、review三种值
        label	        number	        命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003
                                        辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他
        prob	        number	        0-100，代表置信度，越高代表越有可能属于当前返回的标签（label）
    
    result综合了多个策略的结果给出了建议，包含的属性有
        属性              类型              说明
        suggest	        string	        建议，有risky、pass、review三种值
        label	        string	        命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003
                                        辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他

#### msgSecCheck
检查一段文本是否含有违法违规内容。

不建议使用该接口作为可信任的检测，该接口很多违规关键词都可以通过。

提供一个不通过的关键词，这里不方便展示，可以终端打开python交互解释器执行这条语句即可获取

    # 用python执行该命令即可获取，注：该关键词仅供测试使用，请勿宣传，请忽略其语义
    b'\xe6\xb3\x95\xe8\xbd\xae\xe5\xa4\xa7\xe6\xb3\x95\xe5\xa5\xbd'.decode("utf-8")

用法

    we_chat_data = wx.msg_sec_check(media_url, media_type, openid, scene=1)
        :param openid: 用户的openid（用户需在近两小时访问过小程序）
        :param scene: 场景枚举值（1 资料；2 评论；3 论坛；4 社交日志）
        :param content: 需检测的文本内容，文本字数的上限为2500字，需使用UTF-8编码
        :param nickname: 用户昵称，需使用UTF-8编码
        :param title: 文本标题，需使用UTF-8编码
        :param signature: 个性签名，该参数仅在资料类场景有效(scene=1)，需使用UTF-8编码
    传参：
        属性                  类型              说明
        openid              string          用户的openid（用户需在近两小时访问过小程序）
        scene               number          场景枚举值（1 资料；2 评论；3 论坛；4 社交日志）
        content             string          需检测的文本内容，文本字数的上限为2500字
        nickname            string          [选填]用户昵称
        title               string          [选填]文本标题
        signature           string          [选填]个性签名，该参数仅在资料类场景有效(scene=1)

    返回(WeChatDate类型)：
        属性              类型              说明
        errcode	        number	        错误码
        errmsg	        string	        错误信息
        trace_id	    string	        唯一请求标识，标记单次请求
        result	        object	        综合结果
        detail	        array	        详细检测结果

    result综合了多个策略的结果给出了建议，包含的属性有
        属性              类型              说明
        suggest	        string	        建议，有risky、pass、review三种值
        label	        string	        命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003
                                        辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他

    detail包含多个策略类型的检测结果，策略类型的检查结果可能存在的属性如下
        属性              类型              说明
        strategy	    string	        策略类型
        errcode	        number	        错误码，仅当该值为0时，该项结果有效
        suggest	        string	        建议，有risky、pass、review三种值
        label	        number	        命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003
                                        辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他
        prob	        number	        0-100，代表置信度，越高代表越有可能属于当前返回的标签（label）
        keyword	        string	        命中的自定义关键词


### 动态消息

#### createActivityId
创建被分享动态消息或私密消息的 activity_id 详见[动态消息](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/share/updatable-message.html)

    we_chat_data = wx.create_activity_id(unionid=None, openid=None)
    
    unionid与openid二选一
    传参：
        属性          类型              说明
        unionid     string          为私密消息创建activity_id时，指定分享者为 unionid 用户。其余用户不能用此activity_id分享私密消息
        openid      string          为私密消息创建activity_id时，指定分享者为 openid 用户。其余用户不能用此activity_id分享私密消息

    返回(WeChatDate类型)：
        属性	                类型	            说明
        activity_id	        string	        动态消息的 ID
        expiration_time	    number	        activity_id 的过期时间戳。默认24小时后过期。


#### setUpdatableMsg
修改被分享的动态消息 详见[动态消息](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/share/updatable-message.html)

    we_chat_data = wx.set_updatable_msg(activity_id, target_state, template_info: TemplateInfo)
    传参：
        属性                  类型              说明
        activity_id         string          动态消息的 ID，通过 updatableMessage.createActivityId 接口获取
        target_state        string          动态消息修改后的状态, 合法值: 0 未开始；1 已开始
        template_info       TemplateInfo    动态消息对应的模板信息
        
        TemplateInfo 接受参数：
            参数	            说明
            member_count    target_state = 0 时必填，文字内容模板中 member_count 的值
            room_limit	    target_state = 0 时必填，文字内容模板中 room_limit 的值
            path	        target_state = 1 时必填，点击「进入」启动小程序时使用的路径。对于小游戏，没有页面的概念，可以用于传递查询字符串（query），如 "?foo=bar"
            version_type	target_state = 1 时必填，点击「进入」启动小程序时使用的版本。有效参数值为：develop（开发版），trial（体验版），release（正式版
            **kwgrep        预留
    
        template_info 传参示例：
            from py_wechat_tools.mini_program.updatable_message import TemplateInfo
            template_info = TemplateInfo(
                member_count = 2,
                room_limit = 3,
                # path = 2,
                # version_type = 2,
            )

    返回(WeChatDate类型)：
        属性                  类型              说明


### 安全风控

#### getUserRiskRank
根据提交的用户信息数据获取用户的安全等级 risk_rank，无需用户授权。

    we_chat_data = wx.get_user_risk_rank(openid, scene=0, mobile_no=None, client_ip=None, email_address=None,
                                         extended_info=None, is_test=None)
    传参：
        属性                  类型              说明
        openid              string          用户的openid
        scene               number          [选填]场景值，0:注册，1:营销作弊，默认0
        mobile_no           string          [选填]用户手机号
        client_ip           string          [选填]用户访问源ip
        email_address       string          [选填]用户邮箱地址
        extended_info       string          [选填]额外补充信息
        is_test             boolean         [选填]False：正式调用，True：测试调用


    返回(WeChatDate类型)：
        属性                  类型              说明
        unoin_id        number           唯一请求标识，标记单次请求
        risk_rank       number           用户风险等级


### Short Link

#### generate
根据提交的用户信息数据获取用户的安全等级 risk_rank，无需用户授权。详见[获取 Short Link](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/shortlink.html)

    we_chat_data = wx.generate(page_url, page_title=None, is_permanent=False)
    传参：
        属性                  类型              说明
        page_url            string          通过 Short Link 进入的小程序页面路径，必须是已经发布的小程序存在的页面，可携带 query，最大1024个字符
        page_title          string          [选填]页面标题，不能包含违法信息，超过20字符会用... 截断代替
        is_permanent        boolean         [选填]默认False，生成的 Short Link 类型，短期有效：False，永久有效：True


    返回(WeChatDate类型)：
        属性                  类型              说明
        link                number           短连接


### 生物认证

#### verifySignature
SOTER 生物认证秘钥签名验证

    we_chat_data = wx.verify_signature(openid, json_string, json_signature)
    传参：
        属性                  类型              说明
        openid              string          用户 openid
        json_string         string          通过 wx.startSoterAuthentication 成功回调获得的 resultJSON 字段，注意：必须转str类型
        json_signature      string          通过 wx.startSoterAuthentication 成功回调获得的 resultJSONSignature 字段


    返回(WeChatDate类型)：
        属性                  类型              说明
        is_ok               boolean         验证结果


## 公众号接口


## OAToole配置项

    oa = OAToole(
        # 填写公众号appid以及secret
        appid="appid",
        secret="secret",
        redirect_uri="https://www..."

        # debug模式，默认False，为True时日志输出为debug级别，也可在日志的配置项中配置
        debug=False,
        # access_token失效时是否自动更新，开启后，如果遇到42001(调用接口凭证已过期)就会重新调get_access_token接口获取
        # 如果关闭该功能，必须要从实例化传入access_token或者调用wx.set_access_token(access_token)方法设置，否则访问部分接口返回42001
        passive_access_token=True,

        # 如若设置passive_access_token=False，access_token必填，如果传入access_token，MPTools将会使用该access_token
        access_token=None
    )


#### 集成授权获取用户信息
一个方法弹出授权并且获取用户信息，无需关心如何获取code、access_token等。
也可以自己实现授权逻辑，基础方法都写好了

    data = oa.authorize_userinfo(redirect_uri=None, openid=None, oa_access_token=None, refresh_token=None, 
                                 cache_fun=None, cache_args=None, cache_kwargs=None, scope=None, state=None, 
                                 force_popup=None, force_snap_shot=None, code=None)
    传参：
        属性                  类型              说明
        redirect_uri        string          [选填]授权后重定向的回调链接地址， 请使用 urlEncode 对链接进行处理，需要修改时可传入

        # 可以对以下三个参数做缓存，每次请求可以从缓存中读取，一般会放在session里面
        openid              string          [选填]用户openid，建议提供，提供该参数可以减少请求微信接口次数，该参数与oa_access_token一起传入方可生效
        oa_access_token     string          [选填]用户oa_access_token 建议提供，提供该参数可以减少请求微信接口次数，该参数与openid一起传入方可生效
        refresh_token       string          [选填]用户刷新 oa_access_token，建议提供，提供该参数可以减少请求微信接口次数

        cache_fun           string          [选填]允许传入一个回调方法，必须接收data参数，包含token等信息，data信息如下
        cache_args          string          缓存方法的args传参，类型为元组()
        cache_kwargs        string          缓存方法的kwargs传参，类型为字典{}
        scope               string          应用授权作用域，合法值：
                                                snsapi_base或Auth2.snsApiBase （不弹出授权页面，直接跳转，只能获取用户openid）
                                                [默认]snsapi_userinfo或Auth2.snsApiUserInfo（弹出授权页面，可通过 openid 拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息 ）

        state               string          重定向后会带上 state 参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节
        force_popup         string          强制此次授权需要用户弹窗确认；默认为false；需要注意的是，若用户命中了特殊场景下的静默授权逻辑，则此参数不生效
        force_snap_shot     string          强制此次授权进入快照页；默认为false；需要注意的是，若本次登录命中了近期登录过免授权逻辑逻辑或特殊场景下的静默授权逻辑，则此参数不生效
        code                string          此参数为回调时携带的参数，无需手动传入。

    cache_fun回调函数，参数data是一个WeChatDate对象，包含：
        属性                  类型              说明
        access_token        string          网页授权接口调用凭证,注意：此access_token与基础支持的access_token不同
        expires_in          number          access_token接口调用凭证超时时间，单位（秒）
        refresh_token       string          用户刷新access_token，有效期为30天
        openid              string          用户唯一标识，请注意，在未关注公众号时，用户访问公众号的网页，也会产生一个用户和公众号唯一的OpenID
        scope               string          用户授权的作用域，使用逗号（,）分隔

    返回：返回两个参数，(url: str, userinfo: WeChatData)  url不为空时重定向到url，userinfo不为空：完成所有验证，userinfo为用户的信息
        url：用户授权地址，301重定向到url即可

        userinfo包含参数：
            属性                  类型                  说明
            openid              string              用户的唯一标识
            nickname            string              用户昵称
            sex                 number              用户的性别，值为1时是男性，值为2时是女性，值为0时是未知
            province            string              用户个人资料填写的省份
            city                string              普通用户个人资料填写的城市
            country             string              国家，如中国为CN
            headimgurl          string              用户头像，最后一个数值代表正方形头像大小（有0、46、64、96、132数值可选，0代表640*640正方形头像），
                                                    用户没有头像时该项为空。若用户更换头像，原有头像 URL 将失效。
            privilege           <Array>.string      用户特权信息，json 数组，如微信沃卡用户为（chinaunicom）
            unionid             string              只有在用户将公众号绑定到微信开放平台帐号后，才会出现该字段。


简单的使用示例：

    def oa_access_token_cache(data, request, *args, **kwargs):
        """ 
            缓存方法
            第一个参数必须接收data, 其余参数与cache_args、cache_kwargs传入的一致即可
        """
        # 业务逻辑


    def login():
        # 1、接收一个GET请求的参数code，以Django框架为例
        code = request.GET.get("code")  # 从url中获取?后面的code，请求回调地址时，微信会加上这个code，只需要接收就行。

        # 2、必须传接收到的code，否则会无限刷新授权页面
        #    接收两个参数 url, user_info
        url, user_info = oa.authorize_userinfo(
            code=code,

            # 用于刷新access_token，一般只需要做refresh_token缓存即可，refresh_token有效期为30天
            refresh_token="",

            # 可以通过cache_fun参数，传入一个方法实现access_token、openid、refresh_token等参数缓存，实例化时传入，可以减少请求次数。
            cache_fun=oa_access_token_cache,
            cache_args=(request,),  # 回调函数的元组参数
            cache_kwargs={}  # 回调函数的字典参数
        )

        # url不为None时，重定向到url
        if url:
            redirect(url)   # 重定向到url

        # 到这里已经是授权成功了，user_info就是用户的信息


#### 初始化access_token
直接获取access_token，无需处理code

    data = oa.init_oa_access_token(scope=None, state=None, force_popup=None, force_snap_shot=None, code=None)
    传参：
        属性                  类型              说明
        scope               string          应用授权作用域，合法值：
                                                snsapi_base或Auth2.snsApiBase （不弹出授权页面，直接跳转，只能获取用户openid）
                                                snsapi_userinfo或Auth2.snsApiUserInfo（弹出授权页面，可通过 openid 拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息 ）

        state               string          重定向后会带上 state 参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节
        force_popup         string          强制此次授权需要用户弹窗确认；默认为false；需要注意的是，若用户命中了特殊场景下的静默授权逻辑，则此参数不生效
        force_snap_shot     string          强制此次授权进入快照页；默认为false；需要注意的是，若本次登录命中了近期登录过免授权逻辑逻辑或特殊场景下的静默授权逻辑，则此参数不生效
        code                string          此参数为回调时携带的参数，无需手动传入。

    返回：url, data 两个参数
        url不为None时，请重定向到该url，此时data为None

        data：WeChatDate对象，包含参数：
            属性                  类型              说明
            access_token        string          网页授权接口调用凭证,注意：此access_token与基础支持的access_token不同
            expires_in          number          access_token接口调用凭证超时时间，单位（秒）
            refresh_token       string          用户刷新access_token，有效期为30天
            openid              string          用户唯一标识，请注意，在未关注公众号时，用户访问公众号的网页，也会产生一个用户和公众号唯一的OpenID
            scope               string          用户授权的作用域，使用逗号（,）分隔



#### 用户同意授权，获取code
弹出授权，用户同意后获取code（只需要同意一次）
如果用户同意授权，页面将跳转至 redirect_uri/?code=CODE&state=STATE

    data = oa.authorize(redirect_uri=None, scope=None, state=None, force_popup=None, force_snap_shot=None)
    传参：
        属性                  类型              说明
        redirect_uri        string          授权后重定向的回调链接地址， 请使用 urlEncode 对链接进行处理
        scope               string          应用授权作用域，合法值：
                                                snsapi_base或Auth2.snsApiBase （不弹出授权页面，直接跳转，只能获取用户openid）
                                                snsapi_userinfo或Auth2.snsApiUserInfo（弹出授权页面，可通过 openid 拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息 ）

        state               string          重定向后会带上 state 参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节
        force_popup         string          强制此次授权需要用户弹窗确认；默认为false；需要注意的是，若用户命中了特殊场景下的静默授权逻辑，则此参数不生效
        force_snap_shot     string          强制此次授权进入快照页；默认为false；需要注意的是，若本次登录命中了近期登录过免授权逻辑逻辑或特殊场景下的静默授权逻辑，则此参数不生效


    返回：
        url链接，让用户重定向到该地址即可


#### code换access_token
这里的access_token与基础支持的access_token不同，为了方便区分，这里称为oa_access_token

    data = oa.get_oa_access_token(code)
    传参：
        属性                  类型              说明
        code                string           填写第一步获取的 code 参数，在回调参数中的code

    返回(WeChatDate类型)：
        属性                  类型              说明
        access_token        string          网页授权接口调用凭证,注意：此access_token与基础支持的access_token不同
        expires_in          number          access_token接口调用凭证超时时间，单位（秒）
        refresh_token       string          用户刷新access_token，有效期为30天
        openid              string          用户唯一标识，请注意，在未关注公众号时，用户访问公众号的网页，也会产生一个用户和公众号唯一的OpenID
        scope               string          用户授权的作用域，使用逗号（,）分隔


#### 更新access_token
这里的access_token与基础支持的access_token不同，为了方便区分，这里称为oa_access_token

    data = oa.update_oa_access_token(refresh_token=None)
    传参：
        属性                  类型              说明
        refresh_token       string           [此处传参或初始化传参]上次授权获取的 refresh_token

    返回(WeChatDate类型)：
        属性                  类型              说明
        access_token        string          网页授权接口调用凭证,注意：此access_token与基础支持的access_token不同
        expires_in          number          access_token接口调用凭证超时时间，单位（秒）
        refresh_token       string          用户刷新access_token，有效期为30天
        openid              string          用户唯一标识，请注意，在未关注公众号时，用户访问公众号的网页，也会产生一个用户和公众号唯一的OpenID
        scope               string          用户授权的作用域，使用逗号（,）分隔


#### 获取用户信息
如果网页授权作用域为snsapi_userinfo, 则可以通过该接口拉取用户信息了。

    data = oa.get_userinfo(openid=None)
    传参：
        属性                  类型              说明
        openid              string           用户openid

    返回(WeChatDate类型)：
        属性                  类型                  说明
        openid              string              用户的唯一标识
        nickname            string              用户昵称
        sex                 number              用户的性别，值为1时是男性，值为2时是女性，值为0时是未知
        province            string              用户个人资料填写的省份
        city                string              普通用户个人资料填写的城市
        country             string              国家，如中国为CN
        headimgurl          string              用户头像，最后一个数值代表正方形头像大小（有0、46、64、96、132数值可选，0代表640*640正方形头像），
                                                用户没有头像时该项为空。若用户更换头像，原有头像 URL 将失效。
        privilege           <Array>.string      用户特权信息，json 数组，如微信沃卡用户为（chinaunicom）
        unionid             string              只有在用户将公众号绑定到微信开放平台帐号后，才会出现该字段。


#### 检验授权凭证（access_token）是否有效
如果网页授权作用域为snsapi_userinfo, 则可以通过该接口拉取用户信息了。

    data = oa.auth_access_token(openid=None, oa_access_token=None)
    传参：
        属性                  类型              说明
        access_token        string           授权凭证
        openid              string           用户的唯一标识

    返回(WeChatDate类型)：
        属性                  类型                  说明
        openid              string              用户的唯一标识
        nickname            string              用户昵称
        sex                 number              用户的性别，值为1时是男性，值为2时是女性，值为0时是未知
        province            string              用户个人资料填写的省份
        city                string              普通用户个人资料填写的城市
        country             string              国家，如中国为CN
        headimgurl          string              用户头像，最后一个数值代表正方形头像大小（有0、46、64、96、132数值可选，0代表640*640正方形头像），
                                                用户没有头像时该项为空。若用户更换头像，原有头像 URL 将失效。
        privilege           <Array>.string      用户特权信息，json 数组，如微信沃卡用户为（chinaunicom）
        unionid             string              只有在用户将公众号绑定到微信开放平台帐号后，才会出现该字段。


## 校验方法

### 验证服务器地址的有效性方法
用于消息接口配置域名时的校验方法

    from py_wechat_tools import check
    
    is_wechat_messages = check.message_push_check(
        token=token,
        signature=signature,
        timestamp=timestamp,
        nonce=nonce
    )

    传参：
        属性                  类型              说明
        token               string          用户 openid
        signature           string          通过 wx.startSoterAuthentication 成功回调获得的 resultJSON 字段，注意：必须转str类型
        timestamp           number          通过 wx.startSoterAuthentication 成功回调获得的 resultJSONSignature 字段
        nonce               string          通过 wx.startSoterAuthentication 成功回调获得的 resultJSONSignature 字段

    返回：
        返回值为True or False；True 代表校验通过，False代表校验不通过
