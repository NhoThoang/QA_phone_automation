from QA_automation_phone.config import config
class keyevent:
    def __init__(self,device: str = None, connect = None, x_screen: int = None, y_screen: int = None) -> None:
        self.config = config(device=device, connect=connect, x_screen=x_screen, y_screen=y_screen)
    def press_home(self, device: str):
        self.config.adb_keyevent(device,3)
    def press_back(self, device: str):
        self.config.adb_keyevent(device,4)
    def press_recent(self, device: str):
        self.config.adb_keyevent(device,187)
    def press_power(self, device: str):
        self.config.adb_keyevent(device,26)
    def press_volume_up(self, device: str):
        self.config.adb_keyevent(device,24)
    def press_volume_down(self, device: str):
        self.config.adb_keyevent(device,25)
    def press_camera(self, device: str):
        self.config.adb_keyevent(device,27)
    def press_call(self, device: str):
        self.config.adb_keyevent(device,5)
    def press_end_call(self, device: str):
        self.config.adb_keyevent(device,6)
    def press_headsethook(self, device: str):
        self.config.adb_keyevent(device,79)
    def press_focus(self, device: str):
        self.config.adb_keyevent(device,80)
    def press_notification(self, device: str):
        self.config.adb_keyevent(device,83)
    def press_search(self, device: str):
        self.config.adb_keyevent(device,84)
    def press_media_play_pause(self, device: str):
        self.config.adb_keyevent(device,85)
    def press_media_stop(self, device: str):
        self.config.adb_keyevent(device,86)
    def press_media_next(self, device: str):
        self.config.adb_keyevent(device,87)
    def press_media_previous(self, device: str):
        self.config.adb_keyevent(device,88)
    def press_media_rewind(self, device: str):
        self.config.adb_keyevent(device,89)
    def press_media_fast_forward(self, device: str):
        self.config.adb_keyevent(device,90)
    def press_launch_voice_assistant(self, device: str):
        self.config.adb_keyevent(device,91)
    def press_camera_focus(self, device: str):
        self.config.adb_keyevent(device,92)
    def press_enter(self, device: str):
        self.config.adb_keyevent(device,66)
    def press_del(self, device: str):
        self.config.adb_keyevent(device,67)
    def press_0(self, device: str):
        self.config.adb_keyevent(device,7)
    def press_1(self, device: str):
        self.config.adb_keyevent(device,8)
    def press_2(self, device: str):
        self.config.adb_keyevent(device,9)
    def press_3(self, device: str):
        self.config.adb_keyevent(device,10)
    def press_4(self, device: str):
        self.config.adb_keyevent(device,11)
    def press_5(self, device: str):
        self.config.adb_keyevent(device,12)
    def press_6(self, device: str):
        self.config.adb_keyevent(device,13)
    def press_7(self, device: str):
        self.config.adb_keyevent(device,14)
    def press_8(self, device: str):
        self.config.adb_keyevent(device,15)
    def press_9(self, device: str):
        self.config.adb_keyevent(device,16)
    def press_star(self, device: str):
        self.config.adb_keyevent(device,17)
    def press_pound(self, device: str):
        self.config.adb_keyevent(device,18)
    def press_dpad_up(self, device: str):
        self.config.adb_keyevent(device,19)
    def press_dpad_down(self, device: str):
        self.config.adb_keyevent(device,20)
    def press_dpad_left(self, device: str):
        self.config.adb_keyevent(device,21)
    def press_dpad_right(self, device: str):
        self.config.adb_keyevent(device,22)
    def press_dpad_center(self, device: str):
        self.config.adb_keyevent(device,23)
    def press_volume_mute(self, device: str):
        self.config.adb_keyevent(device,164)
    def press_page_up(self, device: str):
        self.config.adb_keyevent(device,92)
    def press_page_down(self, device: str):
        self.config.adb_keyevent(device,93)
    def press_move_home(self, device: str):
        self.config.adb_keyevent(device,122)
    def press_move_end(self, device: str):
        self.config.adb_keyevent(device,123)
    def press_forward(self, device: str):
        self.config.adb_keyevent(device,125)
    def press_backword(self, device: str):
        self.config.adb_keyevent(device,126)
    def press_tab(self, device: str):
        self.config.adb_keyevent(device,61)
    def press_space(self, device: str):
        self.config.adb_keyevent(device,62)
    def press_A(self, device: str):
        self.config.adb_keyevent(device,29)
    def press_B(self, device: str):
        self.config.adb_keyevent(device,30)
    def press_C(self, device: str):
        self.config.adb_keyevent(device,31)
    def press_D(self, device: str):
        self.config.adb_keyevent(device,32)
    def press_E(self, device: str):
        self.config.adb_keyevent(device,33)
    def press_F(self, device: str):
        self.config.adb_keyevent(device,34)
    def press_G(self, device: str):
        self.config.adb_keyevent(device,35)
    def press_H(self, device: str):
        self.config.adb_keyevent(device,36)
    def press_I(self, device: str):
        self.config.adb_keyevent(device,37)
    def press_J(self, device: str):
        self.config.adb_keyevent(device,38)
    def press_K(self, device: str):
        self.config.adb_keyevent(device,39)
    def press_L(self, device: str):
        self.config.adb_keyevent(device,40)
    def press_M(self, device: str):
        self.config.adb_keyevent(device,41)
    def press_N(self, device: str):
        self.config.adb_keyevent(device,42)
    def press_O(self, device: str):
        self.config.adb_keyevent(device,43)
    def press_P(self, device: str):
        self.config.adb_keyevent(device,44)
    def press_Q(self, device: str):
        self.config.adb_keyevent(device,45)
    def press_R(self, device: str):
        self.config.adb_keyevent(device,46)
    def press_S(self, device: str):
        self.config.adb_keyevent(device,47)
    def press_T(self, device: str):
        self.config.adb_keyevent(device,48)
    def press_U(self, device: str):
        self.config.adb_keyevent(device,49)
    def press_V(self, device: str):
        self.config.adb_keyevent(device,50)
    def press_W(self, device: str):
        self.config.adb_keyevent(device,51)
    def press_X(self, device: str):
        self.config.adb_keyevent(device,52)
    def press_Y(self, device: str):
        self.config.adb_keyevent(device,53)
    def press_Z(self, device: str):
        self.config.adb_keyevent(device,54)
    def press_comma(self, device: str):
        self.config.adb_keyevent(device,55)
    def press_period(self, device: str):
        self.config.adb_keyevent(device,56)
    def press_alt_left(self, device: str):
        self.config.adb_keyevent(device,57)
    def press_alt_right(self, device: str):
        self.config.adb_keyevent(device,58)
    def press_shift_left(self, device: str):
        self.config.adb_keyevent(device,59)
    def press_shift_right(self, device: str):
        self.config.adb_keyevent(device,60)
    def press_sym(self, device: str):
        self.config.adb_keyevent(device,63)
    def press_envelop(self, device: str):
        self.config.adb_keyevent(device,65)
    def press_at(self, device: str):
        self.config.adb_keyevent(device,77)


