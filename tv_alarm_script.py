import ir_sender, time


def run():
    ir_sender.send('pwr_btn')   # Turn on TV
    time.sleep(7)
    ir_sender.send('tv_radio_btn')   # Make sure the source is the TV
    time.sleep(5)
    ir_sender.send('ch_4_btn')  # Set it to channel 4
    time.sleep(5)
    for i in range(10):
        ir_sender.send('volume_up_btn')     # Increase volume 10 steps
        time.sleep(0.1)
