from approxeng.input import CentredAxis, Controller, Button

__all__ = ['NEJoystick']

MY_VENDOR_ID = 5824
MY_PRODUCT_ID = 1159

class NEJoystick(Controller):
    """
    Driver for the Neave Engineering Joystick
    """

    def __init__(self, dead_zone=0.1, hot_zone=0.1):
        """
        Axis and button definitions for my new controller class

        :param float dead_zone:
            Used to set the dead zone for each :class:`approxeng.input.CentredAxis` in the controller.
        :param float hot_zone:
            Used to set the hot zone for each :class:`approxeng.input.CentredAxis` in the controller.
        """
        super(NEJoystick, self).__init__(
            controls=[
                Button("SW1", 288, sname='square'),
                Button("SW2", 289, sname='triangle'),
                Button("SW3", 292, sname='circle'),
                Button("TRIGGER", 293, sname='cross'),
                Button("Right Stick", 295, sname='rs'),
                Button("Left Stick", 294, sname='ls'),
                Button("TOG_DOWN", 290, sname='l1'),
                Button("TOG_UP", 291, sname='r1'),
                Button("ENCODER_BTN", 296, sname='select'),
                CentredAxis("Left Horizontal", 0, 65535, 0, sname='lx'),
                CentredAxis("Left Vertical", 0, 65535, 1, sname='ly'),
                CentredAxis("Left Rotate", 0, 65535, 2, sname='tx'),
                CentredAxis("Right Horizontal", 0, 65535, 3, sname='rx'),
                CentredAxis("Right Vertical", 0, 65535, 4, sname='ry'),
                CentredAxis("Right Rotate", 0, 65535, 5, sname='ty'),
                CentredAxis("Encoder Value", 0, 65535, 6, sname='lt')
            ],
                dead_zone=dead_zone,
                hot_zone=hot_zone)

    @staticmethod
    def registration_ids():
        """
        :return: list of (vendor_id, product_id) for this controller
        """
        return [(MY_VENDOR_ID, MY_PRODUCT_ID)]

    def __repr__(self):
        return 'NEJoystick'
