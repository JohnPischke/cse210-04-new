
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley



STONES_PER_FRAME = 1
import pyray

class Director:
    
    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._cast = ""

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
        self._cast.fall()
        self._cast.create_stones(STONES_PER_FRAME)
        self._cast.compare()

    def _do_outputs(self):
        self._video_service.clear_buffer()
        actors = self._cast.get_cast()
        player = self._cast.get_player()
        self._video_service.draw_actor(player)
        self._video_service.draw_actors(actors)
        pyray.draw_text(str(self._cast.points_total), 25, 25, 30, (252,252,252))
        self._video_service.flush_buffer()
