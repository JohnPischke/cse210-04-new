STONES_PER_FRAME = 2

class Director:
    
    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service

    def start_game(self, cast):
        self._cast = cast
        self.game_loop()

    def game_loop(self):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._video_service.close_window()

    def _get_inputs(self):
        player = self._cast.player
        velocity = self._keyboard_service.get_direction()
        player.move_x(velocity)
        pass

    def _do_updates(self):
        self._cast.create_stones(STONES_PER_FRAME)

    def _do_outputs(self):
        pass
