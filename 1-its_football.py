import time 

def count_down(time_set):
    try:
        sec = int(time_set) * 60 # convert minutes to seconds
        if sec < 60: # warning message if input time is less than 1 minute
            print("Warning: Time input is less than 1 minute!")
            return
        print("Your Count down time starts for {} minutes.".format(time_set))
        time.sleep(0.1)

        while sec:
            mins, secs = divmod(sec, 60)
            print("{:02d}:{:02d}".format(mins, secs))
            if sec == int(time_set)*60*0.2: # warning message at 20%
                print("Warning: Almost finished!")
            time.sleep(1)
            sec -= 1

        print("Completed!")
    except ValueError:
        print("Error: Please enter only integers for minutes!")
        count_down(input("\nPlease enter the time for count down (in minutes): "))

# take user input for time and call the function
try:
    time_set = int(input("Please enter your count down time (in minutes): \t"))
    count_down(time_set)
except ValueError:
    print("Error: Please enter only integers for minutes!")
    time_set = input("Please enter a number for your count down time: \n")
    count_down(time_set)