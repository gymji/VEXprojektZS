# --------------------------------------------------------------------------------- #
#                                                                                   #
#    Project:          Base Robot With Sensors                                      #
#    Module:           main.py                                                      #
#    Author:           VEX                                                          #
#    Created:          Fri Aug 05 2022                                              #
#    Description:      Base IQ Gen 2 robot with controls and with sensors           #
#                                                                                   #
#    Configuration:    BaseBot with Sensors (Drivetrain 2-motor, Inertial)          #
#                      Left Motor in Port 1                                         #
#                      Right Motor in Port 6                                        #
#                      TouchLED in Port 2                                           #
#                      Optical Sensor in Port 3                                     #
#                      Distance Sensor in Port 7                                    #
#                      Bumper in Port 8                                             #
#                                                                                   #
# --------------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_drive_smart = Motor(Ports.PORT1, 1, False)
right_drive_smart = Motor(Ports.PORT6, 1, True)

drivetrain = SmartDrive(left_drive_smart, right_drive_smart, brain_inertial, 200)
touchled_2 = Touchled(Ports.PORT2)
optical_3 = Optical(Ports.PORT3)
distance_7 = Distance(Ports.PORT7)
bumper_8 = Bumper(Ports.PORT8)


def calibrate_drivetrain():
    # Calibrate the Drivetrain Inertial
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")
    brain_inertial.calibrate()
    while brain_inertial.is_calibrating():
        sleep(25, MSEC)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)


# Begin project code
calibrate_drivetrain() # nakalibruje polohu
brain.play_sound(SoundType.TADA) # zahraje TAD??
touchled_2.set_color(Color.GREEN) # LED zezelen??
brain.screen.print("Ahoj lidi") # vyp????e text
brain.screen.next_row() # dal???? ????dek
brain.screen.print("ja jsem VEX") # vyp????e text
## ??ek?? dokud nen?? stiknuta dotykov?? LED
while not touchled_2.pressing():
    wait(20, MSEC)
touchled_2.set_color(Color.ORANGE)
## ??ek?? dokud nen?? stiknut n??razn??k
while not bumper_8.pressing():
    drivetrain.drive(FORWARD) # jede dop??edu
    wait(20, MSEC) # motor jede program ??ek??
drivetrain.stop() # motor se zastav??
touchled_2.set_color(Color.RED) # LED z??erven??
drivetrain.drive_for(REVERSE, 20, MM) # couvne 20mm
brain.screen.next_row() # dal???? ????dek na displej
brain.screen.print("STOP") # vyp????e text
brain.play_sound(SoundType.SIREN) # p??ehraje zvuk sir??ny
# konec programu
