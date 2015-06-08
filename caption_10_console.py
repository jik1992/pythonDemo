import uuid

from prettytable import PrettyTable
import wget

table = PrettyTable(["animal", "ferocity"])
table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["Rabbit of Caerbannog", 110])
table.add_row(["cat", -1])
table.add_row(["platypus", 23])
table.add_row(["dolphin", 63])
table.add_row(["albatross", 44])
table.sort_key("ferocity")
table.reversesort = True

# print table

print uuid.uuid4()

# pbar = ProgressBar(maxval=10)
# for i in range(1, 11):
#     pbar.next_update(i)
#     time.sleep(1)
# pbar.finish()
filename=wget.download("http://dldir1.qq.com/qqfile/qq/QQ7.2/14810/QQ7.2.exe")

