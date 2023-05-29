# 任务
# 读取base + battle cysp二进制，合成完整skel二进制

b_num = b"200400"
f_num = str(b_num, encoding='UTF-8')
f1_path = f_num + "_CHARA_BASE.cysp.bytes"
f2_path = f_num + "_BATTLE.cysp.bytes"
f3_path = f_num + ".skel"

# 读取基础文件
with open(f1_path, "rb") as f1:
    b1 = b""
    while True:
        b = f1.read(1024)
        if b == b"":
            break
        b1 += b
    # 1. 定位开头
    i = 0
    for c in b1:
        if c == 0x1c:
            break
        i += 1
    result = b1[i:]
    # 读取增量文件
    with open(f2_path, "rb") as f2:
        b2 = b""
        while True:
            b = f2.read(1024)
            if b == b"":
                break
            b2 += b
        # 2.定位开头
        i = 0
        for c in b2:
            j = 0
            flag = True
            while True:
                if j >= len(b_num):
                    break
                if b2[i + j] != b_num[j]:
                    flag = False
                    break
                j += 1
            if flag:
                break
            i += 1
        result += bytes([0x50])  # 动画个数，可以填一个较大的值
        result += b2[i - 1:]
        with open(f3_path, "wb") as f3:
            f3.write(result)
