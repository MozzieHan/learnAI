
1. 启动命令： 
    ```shell
    # -c 制定并发参数, 默认为cpu核数
    celery --app=everparty.celery:app worker --loglevel=INFO -n worker_high -Q party.high -c 2
    ```
2. 启动worker时不指定-Q参数时将绑定在一个默认名字为"celery" 的queue
3. 指定queue方式
    - 在  @task(queue="party.high")  上制定
    - 在  .apply_async((1,1,1), queue="party.high") 指定
    - 配置文件中指定
        ```python
        CELERY_ROUTES = {
            'entity.tasks.task_test.task_high': {
                'queue': "party.high",
            },
            'entity.tasks.task_test.task_default': {
                'queue': "party.default",
            },
        }
        ```
