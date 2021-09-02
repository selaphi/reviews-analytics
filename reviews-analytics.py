data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)

        count += 1 # count + 1 = count 的快寫法
        if count % 1000 == 0:
            print(len(data))

print('已讀取完成，資料一共有', len(data), '筆')

sum_len = 0
for word in data:
	sum_len += len(word)

print('已計算完成，每筆留言平均有', sum_len/len(data), '個字')