# logging模块
- 日志级别
    - 级别可自定义: DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
- 使用方式: 单例模式
    - 直接使用logging(封装了其他组件)

# logging模块级别的日志
- 使用以下几个函数
    - logging.debug(msg, *args, **kwargs)
    - logging.info(msg, *args, **kwargs)
    - logging.warning(msg, *args, **kwargs)
    - logging.error(msg, *args, **kwargs)
    - logging.critical(msg, *args, **kwargs)
    - logging.log(level, *args, **kwargs)
    - logging.basicConfig(**kwargs)
- logging.basicConfig(**kwargs)
    - 对root logger进行一次性配置
    - 只在第一次调用的时候起作用
    - 不配置logger则使用默认值
        - 输出：sys.stderr，即：标准输出
        - 级别：WARNING
        - 格式： level:log_name:content
- format参数
    
    
    | 字段/属性名称 | 使用格式 | 描述 |
    | ------ | ------ | ------ |
    | asctime | %(asctime)s | 日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896 |
    | created | %(created)f | 日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值 |
    | relativeCreated | %(relativeCreated)d | 日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的） |
    | msecs | %(msecs)d | 日志事件发生事件的毫秒部分 |
    | levelname | %(levelname)s | 该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'） |
    | levelno | %(levelno)s | 该日志记录的数字形式的日志级别（10, 20, 30, 40, 50） |
    | name | %(name)s | 所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger |
    | message | %(message)s | 日志记录的文本内容，通过 msg % args计算得到的 |
    | pathname | %(pathname)s | 调用日志记录函数的源码文件的全路径 |
    | filename | %(filename)s | pathname的文件名部分，包含文件后缀 |
    | module | %(module)s | filename的名称部分，不包含后缀 |
    | lineno | %(lineno)d | 调用日志记录函数的源代码所在的行号 |
    | funcName | %(funcName)s | 调用日志记录函数的函数名 |
    | process | %(process)d | 进程ID |
    | processName | %(processName)s | 程名称，Python 3.1新增 |
    | thread | %(thread)d | 线程ID |
    | threadName | %(thread)s | 线程名称 |
    
    

# logging模块的处理流程
- 四大组件
    - 日志起(Logger): 产生日志的一个接口
    - 处理器(Handler): 把产生的日志发送到相应的目的地
    - 过滤器(Filter): 更精细的控制那些日志输出
    - 格式器(Formatter): 对输出信息进行格式化
- Logger
    - 产生一个日志
    - 操作
        - Logger.setLevel()
        - Logger.addHandler()/Logger.removeHandler()
        - Logger.addFilter()/Logger.removeFilter()
        - Logger.debug: 产生一条debug级别的日志，同理info/warning...
        - Logger.exception(): 创建类似于Logger.error等
        - Logger.log(): 同logging.log
    - 如何得到logger对象
        - 实例化
        - logging.getLogger()
- Handler
    - 把log发送到指定位置
    - 操作
        - setLevel
        - setFormat
        - addFilter/removeFilter
    - 不需要直接使用, Handler是基类
        - logging.StreamHandler: 将日志消息发送到Stream,如:std.out、std.error
        - logging.FileHandler: 将日志文件发送到文件，默认文件会无限增长
        - logging.handlers.RotatingFileHandler: 发送到文件，支持按文件大小切割
        - logging.handlers.TimedRotatingFileHandler:发送到文件，支持按时间切割
        - logging.handlers.HTTPHandler: 将日志消息以GET/POST发送到指定的HTTP服务器
        - logging.handlers.SMTPHandler: 将日志消息发送给指定的邮箱地址
        - logging.NullHandler: 不做任何处理
- Format类
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 三个参数
        - fmt: 指定消息格式化字符串
        - datefmt: 指定日期格式字符串
        - style: 可取值 %、{ 、$.如不指定，默认%
- Filter类
    - 可以被Handler和Logger使用
    - 控制传递过来的信息的具体内容
    