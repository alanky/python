with open('./files/1.txt', 'r', encoding='UTF-8') as f1, open('./files/2.txt', 'r', encoding='UTF-8') as f2, open('./files/3.txt', 'r', encoding='UTF-8') as f3, open(
        'files/output.txt', 'w', encoding='UTF-8') as out:
    for word1 in f1:
        word1 = word1.strip()  # 去除行末的换行符
        for word2 in f2:
            word2 = word2.strip()  # 去除行末的换行符
            for word3 in f3:
                word3 = word3.strip()  # 去除行末的换行符
                combination =word1  + word2 + word3 + "\n"  # 拼接单词并添加换行符
                out.write(combination)  # 将组合写入文件
            f3.seek(0)  # 将第三个文件的读取位置重置为文件开头，以便下一次循环使用
        f2.seek(0)  # 将第二个文件的读取位置重置为文件开头，以便下一次循环使用