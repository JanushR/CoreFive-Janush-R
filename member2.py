import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music_volume = 0.5
        self.sound_volume = 0.7
        self.current_music = None

    def load_sound(self, name, file_path):
        """Load a sound effect into memory"""
        try:
            sound = pygame.mixer.Sound(file_path)
            sound.set_volume(self.sound_volume)
            self.sounds[name] = sound
            return True
        except pygame.error:
            print(f"Couldn't load sound: {file_path}")
            return False

    def play_sound(self, name):
        """Play a loaded sound effect"""
        if name in self.sounds:
            self.sounds[name].play()

    def load_background_music(self, file_path):
        """Load and start playing background music"""
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.set_volume(self.music_volume)
            self.current_music = file_path
            return True
        except pygame.error:
            print(f"Couldn't load music: {file_path}")
            return False

    def play_background_music(self, loops=-1):
        """Start playing the loaded background music"""
        if self.current_music:
            pygame.mixer.music.play(loops)

    def stop_background_music(self):
        """Stop the currently playing background music"""
        pygame.mixer.music.stop()

    def pause_background_music(self):
        """Pause the currently playing background music"""
        pygame.mixer.music.pause()

    def unpause_background_music(self):
        """Unpause the background music"""
        pygame.mixer.music.unpause()

    def set_music_volume(self, volume):
        """Set the volume of the background music (0.0 to 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)

    def set_sound_volume(self, volume):
        """Set the volume of all sound effects (0.0 to 1.0)"""
        self.sound_volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            sound.set_volume(self.sound_volume)

    def fade_out_music(self, time_ms):
        """Fade out the background music over the specified time"""
        pygame.mixer.music.fadeout(time_ms)

    def is_music_playing(self):
        """Check if background music is currently playing"""
        return pygame.mixer.music.get_busy()

# Example sound effects dictionary
GAME_SOUNDS = {
    'collision': 'sounds/collision.wav',
    'powerup': 'sounds/powerup.wav',
    'game_over': 'sounds/game_over.wav',
    'menu_select': 'sounds/menu_select.wav',
    'background_music': 'sounds/background_music.mp3'
}

class GameAudio:
    def __init__(self):
        self.sound_manager = SoundManager()
        self.initialize_sounds()

    def initialize_sounds(self):
        """Initialize all game sounds and music"""
        # Create sounds directory if it doesn't exist
        if not os.path.exists('sounds'):
            os.makedirs('sounds')
            print("Created sounds directory. Please add sound files.")

        # Load all sound effects
        for sound_name, sound_path in GAME_SOUNDS.items():
            if sound_name != 'background_music':
                self.sound_manager.load_sound(sound_name, sound_path)

        # Load background music
        self.sound_manager.load_background_music(GAME_SOUNDS['background_music'])

    def play_game_sound(self, sound_name):
        """Play a game sound effect"""
        self.sound_manager.play_sound(sound_name)

    def start_background_music(self):
        """Start playing the background music"""
        self.sound_manager.play_background_music()

    def stop_background_music(self):
        """Stop the background music"""
        self.sound_manager.stop_background_music()

    def handle_volume_changes(self, music_volume=None, sound_volume=None):
        """Update volume levels for music and sound effects"""
        if music_volume is not None:
            self.sound_manager.set_music_volume(music_volume)
        if sound_volume is not None:
            self.sound_manager.set_sound_volume(sound_volume)

    def handle_game_events(self, event_type):
        """Play appropriate sounds for game events"""
        if event_type == 'collision':
            self.play_game_sound('collision')
        elif event_type == 'powerup':
            self.play_game_sound('powerup')
        elif event_type == 'game_over':
            self.play_game_sound('game_over')
            self.sound_manager.fade_out_music(2000)  # Fade out music over 2 seconds
        elif event_type == 'menu_select':
            self.play_game_sound('menu_select')

# Usage example
if __name__ == '__main__':
    pygame.init()
    game_audio = GameAudio()
    
    # Test sound system
    print("Testing sound system...")
    game_audio.start_background_music()
    game_audio.handle_game_events('powerup')
    
    # Keep the program running for a few seconds to hear the sounds
    pygame.time.wait(5000)
    pygame.quit()
