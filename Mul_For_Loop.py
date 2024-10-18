cricket = ["bcci", "ecb", "aus", "sa"]
extensions = ["in", "com", "org"]

for web in cricket:
    for ext in extensions:
        print("www.{}.{}".format(web, ext))
