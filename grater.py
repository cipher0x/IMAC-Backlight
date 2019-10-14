
backLight_Max = "/sys/class/backlight/radeon_bl0/max_brightness"
backLight = "/sys/class/backlight/radeon_bl0/brightness"
def main():
    
    #get max 
    f = open(backLight_Max,"r")
    maxValue = f.read()
    print ("Max screen value: {}".format(maxValue))
    maxValueInt = int(maxValue)
    f.close()

    #get user input value
    print("Enter Brightness value: ")
    user_input = input()
    setValue = int(user_input)
    
    if setValue < 30:
        setValue = 30

    print("Setting screen brightness to: {}".format(setValue))

    #set screen brightness 
    f = open(backLight, "w")
    f.write(str(setValue))
    f.close()

main()
