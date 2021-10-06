# -*- coding: utf-8 -*-
import threading


class Singleton(type):
    _instance_lock = threading.Lock()

    # 元类的__init__方法负责在类创建后初始化类属性
    def __init__(cls, *args, **kwargs):
        # 虽然子类SubClass创建时继承了基类MyClass的类属性_instance，但是会在此处被重置为None，从而SubClass也是单例模式
        cls._instance = None
        super(Singleton, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        # 外层校验是为了避免单例已产生后，线程还要拿锁，浪费锁资源
        if cls._instance is None:
            with Singleton._instance_lock:
                # 内层校验是单例逻辑的条件判断，必须放在锁内，是为了避免线程在等锁的过程中单例已产生
                if cls._instance is None:
                    # 通过super函数调用父元类type的__call__方法完成实例化
                    cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance
