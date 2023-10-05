text = "test"

def print_text_100_times (text):
    for current in range(100):
        print(text)


x = 1
while x < 100:
    x = x * 2
    print(x) 

for i in range(10):
    print(f'Start loop with i == {i}')
    if i == 3:
        print('Break out')
        break
    if i < 2:
        print(f'Continue')
        continue
    print('End loop')
