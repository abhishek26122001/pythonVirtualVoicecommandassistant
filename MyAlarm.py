import datetime
import winsound

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    altime = altime[11:-3]
    print(altime)

    Horeal = altime[:2]     # Slicing For Different Hours
    Horeal = int(Horeal) 
    Mireal = altime[3:5]     # Slicing For different Min
    Mireal = int(Mireal)
    print(f"Alarm is set for {Timing} sir!")

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("Alarm is Running")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif Mireal<datetime.datetime.now().minute:
                break

if __name__ == '__main__':
    alarm('9:27 PM')
