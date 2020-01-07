from PIL import Image
import os


class ImageToASCII:
    def __init__(self, raw_image, mode="light"):
        self.characters = [' ', '.', ',', '~', '+', '*', '=', '%', '$', '&', '#']

        self.output = ''
        self.mode = mode

        if self.mode == "dark":
            self.characters.reverse()

        self.raw_image = raw_image

    @classmethod
    def open(cls, file_path, mode="light"):
        return cls(Image.open(file_path), mode)

    def ratio_range(self):
        for ratio in range(1, 10):
            yield self.process_image(ratio)

    def process_image_to_size(self, size):
        new_width, new_height = size
        resized_image = self.raw_image.resize((new_width, new_height))

        output = [""] * new_height
        for y in range(new_height):
            row = [""] * new_width
            for x in range(new_width):
                # Max750//75 = 0 through 10, the amount of Characters used.
                brightness = (sum(resized_image.getpixel((x, y))) // 68) - 1
                if brightness < 0:
                    brightness = 0
                row[x] = self.characters[brightness]
            output[y] = "".join(row)
        return "\n".join(output)

    def process_image(self, ratio):
        new_width = self.raw_image.width // ratio
        new_height = self.raw_image.height // ratio
        resized_image = self.raw_image.resize((new_width, new_height))

        output = [""] * new_height
        for y in range(new_height):
            row = [""] * new_width
            for x in range(new_width):
                # Max750//75 = 0 through 10, the amount of Characters used.
                brightness = (sum(resized_image.getpixel((x, y))) // 68) - 1
                if brightness < 0:
                    brightness = 0
                row[x] = self.characters[brightness]
            output[y] = "".join(row)
        return "\n".join(output)

    def write(self, file_path, ratio):
        if isinstance(ratio, tuple):
            with open(file_path, "w") as output_file:
                output_file.write(self.process_image_to_size(ratio))
        else:
            with open(file_path, "w") as output_file:
                output_file.write(self.process_image(ratio))


def options(file_path):
    image_choice_text = "What is the name of the image you want me to convert?\nMind you, I'm picky and only like .jpg"

    mode_text = "1 for LightMode(Dark Text on a light background)\n2 for Darkmode(Light text on a dark background)"

    for file in os.listdir(f"{file_path}/Images"):
        print(file)

    image_choice = input(image_choice_text)
    mode = "light" if input(mode_text) == "1" else "dark"

    return os.path.join(file_path, "Images", image_choice + ".jpg"), mode


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--files", nargs="*", default=[],
                        help="Specify any number of input images")
    parser.add_argument("-d", "--dirs_in", nargs="*", default=[],
                        help="Specify any number of input directories")
    parser.add_argument("-o", "--dir_out", default="./ASCIIArt",
                        help="Specify an output directory.")
    parser.add_argument("-m", "--mode", default="light", choices=("light", "dark"),
                        help="Specify the brightness setting")
    brightnesses = parser.add_mutually_exclusive_group()
    brightnesses.add_argument("-a", "--all", action="store_true",
                              help="Produces outputs in all sizes.")
    brightnesses.add_argument("-r", "--range", dest="range", nargs=2, type=int,
                              help="Produces outputs in the specified range of sizes (1 is the largest, and maintains"
                                   "the original image size. The image's height and width is divided by the size.")
    brightnesses.add_argument("--ratio", type=int,
                              help="Produces outputs whose size is the ratio of the input image dimensions.")
    brightnesses.add_argument("-s", "--size", nargs=2, type=int,
                              help="Produces outputs in the specified size.")
    parser.add_argument("--flatten", action="store_true",
                        help="Flattens images.")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    min_ratio = 1
    max_ratio = 10

    if args.range:
        min_ratio, max_ratio = args.range
        max_ratio += 1
    elif args.ratio:
        min_ratio = args.ratio
        max_ratio = args.ratio + 1
    elif args.size:
        min_ratio = None

    image_generated = False
    os.makedirs(args.dir_out, exist_ok=True)


    def process_file(file_name, mode):
        global image_generated
        image_generated = True
        image_processor = ImageToASCII.open(file_name, args.mode)
        if args.flatten:
            file_name = os.path.basename(file_name)
        file_base = file_name.split(".")[0]
        os.makedirs(os.path.join(args.dir_out, os.path.dirname(file_base)), exist_ok=True)

        if min_ratio:
            for i in range(1, 10):
                image_processor.write(os.path.join(args.dir_out, f"{file_base}-{i}-{args.mode}.txt"), i)
        else:
            for i in range(1, 10):
                image_processor.write(os.path.join(args.dir_out, f"{file_base}-{args.mode}.txt"), args.size)


    for file in args.files:
        process_file(file, args.mode)
    for directory in args.dirs_in:
        for file in os.listdir(directory):
            if file.endswith(".jpg"):
                process_file(file, args.mode)

    if not image_generated:
        file_path, mode = options(os.path.dirname(os.path.abspath(__file__)))
        file_name = os.path.basename(file_path).split(".")[0]
        process_file(file_path, mode)
