import os, subprocess, re, random


def gen_text(frame):

    raw_txt = subprocess.run(
        [
            "tesseract",
            frame,
            "-",
            "-l",
            "spa",
        ],
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")

    # print(raw_txt)
    print("---")
    clean_text = raw_txt
    clean_text = re.sub(".*TikTok.*", "", clean_text)
    clean_text = re.sub(".*TikTOk.*", "", clean_text)
    clean_text = re.sub(".*TikTOK.*", "", clean_text)
    clean_text = re.sub("Reply to", "", clean_text)
    clean_text = re.sub(".*comment", "", clean_text)
    clean_text = re.sub(".*rtauler.*", "", clean_text)
    clean_text = re.sub("^(?:[\n ]*(?:\r?\n|\r))+", "", clean_text)
    clean_text = re.sub("/", "", clean_text)
    clean_text = re.sub("\n\n", "\n", clean_text)
    clean_text = re.sub("\n", " ", clean_text)

    # print(clean_text)
    short_clean_text = clean_text[:100]
    # short_clean_text = (clean_text[:98] + "..") if len(clean_text) > 98 else clean_text
    # print(short_clean_text)
    # print("chars:", len(short_clean_text))
    # print("---")
    return short_clean_text


# create the text and rename the file
directory = "videos"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    identifier, _ = os.path.splitext(filename)
    if f.endswith(".jpg"):
        print(f)
        try:
            new_filename = gen_text(f)
            print(new_filename)
            if new_filename:
                os.rename(
                    "videos" + "/" + identifier + ".mp4",
                    "videos" + "/" + new_filename + ".mp4",
                )
            else:
                print("no filename was generated")
        except:
            print("could not generate text")
