import time

def focus_timer(duration):
    """
    一个专注时钟函数，接受一个参数，代表专注时间（以分钟为单位）。
    """
    # 转换为秒数
    duration = duration * 60

    # 开始计时
    while duration:
        mins, secs = divmod(duration, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        duration -= 1

    # 完成计时
    print("Time's up!")
