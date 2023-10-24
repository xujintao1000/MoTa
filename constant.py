IMAGE_NAME_LIST = ["./resources/image/BlueImage.png",
                   "./resources/image/Mota50Floor.png",
                   "./resources/image/Mota50Frame.png",
                   "./resources/image/Reference.png",
                   "./resources/image/ReferenceBackground.png"
                   ]

IMAGE_LOCATION_LIST = {}
DEBUG = True

def init_load_data():
    # 打开文件并按行读取数据
    with open("./resources/Data/Floor/PictureLocation.txt", "r") as file:
        data_lines = file.readlines()
        # 输出每行数据,转换类型为int
        for line in data_lines:
            items = line.strip().split()
            for i in range(0, 4):
                items[i] = int(items[i])
            items[5] = int(items[5])
            IMAGE_LOCATION_LIST[items[5]] = items





init_load_data()


if DEBUG:
    print("IMAGE_LOCATION_LIST", IMAGE_LOCATION_LIST)
