# -*- coding: UTF-8 -*-


def read_image_pixels(image_path):
    with open(image_path, "rb") as f:
        # 读取文件头信息，对于常见的图像格式如 BMP、PNG、JPEG 等，文件头包含了一些特定的标识和图像信息
        header = f.read(16)
        # 判断是否为 BMP 格式
        if header[:2] == b"BM":
            # 跳过一些 BMP 文件特定的字节
            f.read(14)
            width, height = int.from_bytes(
                f.read(4), byteorder="little"
            ), int.from_bytes(f.read(4), byteorder="little")
            # 跳过每行像素数据的填充字节
            row_padding = (4 - (width * 3) % 4) % 4
            pixels = []
            for _ in range(height):
                row = []
                for _ in range(width):
                    b = f.read(1)[0]
                    g = f.read(1)[0]
                    r = f.read(1)[0]
                    row.append((r, g, b))
                f.read(row_padding)
                pixels.append(row)
            return pixels
        else:
            raise ValueError("Unsupported image format")


if __name__ == "__main__":
    print(read_image_pixels("fourier/imgs/avatar.jpg"))
