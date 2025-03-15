from QA_automation_phone.config import config
class keyevent(config):
    def __init__(self,device: str = None, connect = None, x_screen: int = None, y_screen: int = None) -> None:
        super().__init__(device, connect, x_screen, y_screen)
    def press_home(self):
        self.adb_keyevent(3)
    def press_back(self):
        self.adb_keyevent(4)
    def press_recent(self):
        self.adb_keyevent(187)
    def press_power(self):
        self.adb_keyevent(26)
    def press_volume_up(self):
        self.adb_keyevent(24)
    def press_volume_down(self):
        self.adb_keyevent(25)
    def press_camera(self):
        self.adb_keyevent(27)
    def press_call(self):
        self.adb_keyevent(5)
    def press_end_call(self):
        self.adb_keyevent(6)
    def press_headsethook(self):
        self.adb_keyevent(79)
    def press_focus(self):
        self.adb_keyevent(80)
    def press_notification(self):
        self.adb_keyevent(83)
    def press_search(self):
        self.adb_keyevent(84)
    def press_media_play_pause(self):
        self.adb_keyevent(85)
    def press_media_stop(self):
        self.adb_keyevent(86)
    def press_media_next(self):
        self.adb_keyevent(87)
    def press_media_previous(self):
        self.adb_keyevent(88)
    def press_media_rewind(self):
        self.adb_keyevent(89)
    def press_media_fast_forward(self):
        self.adb_keyevent(90)
    def press_launch_voice_assistant(self):
        self.adb_keyevent(91)
    def press_camera_focus(self):
        self.adb_keyevent(92)
    def press_enter(self):
        self.adb_keyevent(66)
    def press_del(self):
        self.adb_keyevent(67)
    def press_0(self):
        self.adb_keyevent(7)
    def press_1(self):
        self.adb_keyevent(8)
    def press_2(self):
        self.adb_keyevent(9)
    def press_3(self):
        self.adb_keyevent(10)
    def press_4(self):
        self.adb_keyevent(11)
    def press_5(self):
        self.adb_keyevent(12)
    def press_6(self):
        self.adb_keyevent(13)
    def press_7(self):
        self.adb_keyevent(14)
    def press_8(self):
        self.adb_keyevent(15)
    def press_9(self):
        self.adb_keyevent(16)
    def press_star(self):
        self.adb_keyevent(17)
    def press_pound(self):
        self.adb_keyevent(18)
    def press_dpad_up(self):
        self.adb_keyevent(19)
    def press_dpad_down(self):
        self.adb_keyevent(20)
    def press_dpad_left(self):
        self.adb_keyevent(21)
    def press_dpad_right(self):
        self.adb_keyevent(22)
    def press_dpad_center(self):
        self.adb_keyevent(23)
    def press_volume_mute(self):
        self.adb_keyevent(164)
    def press_page_up(self):
        self.adb_keyevent(92)
    def press_page_down(self):
        self.adb_keyevent(93)
    def press_move_home(self):
        self.adb_keyevent(122)
    def press_move_end(self):
        self.adb_keyevent(123)
    def press_forward(self):
        self.adb_keyevent(125)
    def press_backword(self):
        self.adb_keyevent(126)
    def press_tab(self):
        self.adb_keyevent(61)
    def press_space(self):
        self.adb_keyevent(62)
    def press_A(self):
        self.adb_keyevent(29)
    def press_B(self):
        self.adb_keyevent(30)
    def press_C(self):
        self.adb_keyevent(31)
    def press_D(self):
        self.adb_keyevent(32)
    def press_E(self):
        self.adb_keyevent(33)
    def press_F(self):
        self.adb_keyevent(34)
    def press_G(self):
        self.adb_keyevent(35)
    def press_H(self):
        self.adb_keyevent(36)
    def press_I(self):
        self.adb_keyevent(37)
    def press_J(self):
        self.adb_keyevent(38)
    def press_K(self):
        self.adb_keyevent(39)
    def press_L(self):
        self.adb_keyevent(40)
    def press_M(self):
        self.adb_keyevent(41)
    def press_N(self):
        self.adb_keyevent(42)
    def press_O(self):
        self.adb_keyevent(43)
    def press_P(self):
        self.adb_keyevent(44)
    def press_Q(self):
        self.adb_keyevent(45)
    def press_R(self):
        self.adb_keyevent(46)
    def press_S(self):
        self.adb_keyevent(47)
    def press_T(self):
        self.adb_keyevent(48)
    def press_U(self):
        self.adb_keyevent(49)
    def press_V(self):
        self.adb_keyevent(50)
    def press_W(self):
        self.adb_keyevent(51)
    def press_X(self):
        self.adb_keyevent(52)
    def press_Y(self):
        self.adb_keyevent(53)
    def press_Z(self):
        self.adb_keyevent(54)
    def press_comma(self):
        self.adb_keyevent(55)
    def press_period(self):
        self.adb_keyevent(56)
    def press_alt_left(self):
        self.adb_keyevent(57)
    def press_alt_right(self):
        self.adb_keyevent(58)
    def press_shift_left(self):
        self.adb_keyevent(59)
    def press_shift_right(self):
        self.adb_keyevent(60)
    def press_sym(self):
        self.adb_keyevent(63)
    def press_envelop(self):
        self.adb_keyevent(65)
    def press_at(self):
        self.adb_keyevent(77)


