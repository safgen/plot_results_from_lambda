import boto3
import json
import matplotlib.pyplot as plt


client = boto3.client('lambda', region_name='ap-northeast-2')

test_obj = "{\"DailyUsage\": \"value1\", \"key2\": \"value2\", \"key3\": \"value3\"}"
x = [0]
y = [0]
y2 = [0]
y3 = [0]


def onclick(event):
    global x, y, y2, y3
    if event.button == 1:
        try:
            response = client.invoke(
                FunctionName='arn:aws:lambda:.....',
                Payload=test_obj,
            )
            print(response["StatusCode"])
            response_dict = json.loads(json.loads(response['Payload'].read().decode()))
            x = [item["Date"].split("T")[0].split('020-')[1] for item in response_dict]
            y = [item["DailyUsers"] for item in response_dict]
            y2 = [item["MedianUsage"] for item in response_dict]
            y3 = [item["TotalUsage"] for item in response_dict]
        except Exception as e:
            print(e)
    ax1.bar(x, y)
    ax2.plot(x, y2)
    ax3.plot(x, y3)
    plt.draw()


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex='all')
ax1.bar(x, y)
ax1.set_title("Daily Users")
ax2.bar(x, y2)
ax2.set_title("Daily Median Usage (minutes)")
ax3.bar(x, y3)
ax3.set_title("Daily Total Usage (minutes)")
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
plt.draw()

