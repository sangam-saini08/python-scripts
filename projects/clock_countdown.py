import time

print("🕛-- WELCOME TO TIMER CLOCK -- 🕛\n")

while True:
    try:
        seconds = int(input("⏱️  Enter the Time in Seconds: "))

        if seconds < 10:
            print("Time should be Greater Than Ten(10)!!")
            continue
        break
    except ValueError:
        print("Enter a valid integer!!")


def multiplication_table(n):
    return [n * i for i in range(11)]

bar_list = multiplication_table(seconds/10)

reverse_index = 10
percentage = 110

print("\n🔔 Timer Started...")
for remaining in range(seconds,-1,-1):
    minutes,secs = divmod(remaining,60)
    time_formate = f"{minutes:02}:{secs:02}"
    if remaining in bar_list:
        loading_bar = "="*reverse_index
        reverse_index -= 1
        percentage -= 10 
    print(f"⏱ Time Left # {time_formate} |{loading_bar:<10}|{percentage:3d}% Left",end="\r")
    
    time.sleep(1)

print("🔕 Times Up--")