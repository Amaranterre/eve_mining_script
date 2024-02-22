import keyboard
import time

def setStopFlag():
    global blStop
    blStop = True
if __name__ == '__main__':
    blStop = False
    # set hot key
    keyboard.add_hotkey('ctrl+shift+t',setStopFlag)
    
    print('----------Start-----------------')
    intCnt = 0    
    while intCnt < 10 and blStop == False:
        print( "%s  Print result from loop in main process, intCnt is: %d"%(time.ctime(),intCnt))
        time.sleep(5)
        print("now wake up!")
        intCnt +=1
        
    if blStop == False:
        print( 'Timeout!')
    else:
        print( 'End: stopped by user!')