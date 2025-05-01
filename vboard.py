import gi
import uinput
import time
import os
import configparser
# Removed import sys

os.environ['GDK_BACKEND'] = 'wayland'

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib


# English key mapping
key_mapping_en = {
    # Added Esc, F keys, and Delete
    uinput.KEY_ESC: "Esc", uinput.KEY_F1: "F1", uinput.KEY_F2: "F2", uinput.KEY_F3: "F3", uinput.KEY_F4: "F4",
    uinput.KEY_F5: "F5", uinput.KEY_F6: "F6", uinput.KEY_F7: "F7", uinput.KEY_F8: "F8", uinput.KEY_F9: "F9",
    uinput.KEY_F10: "F10", uinput.KEY_F11: "F11", uinput.KEY_F12: "F12", uinput.KEY_DELETE: "Delete",

    uinput.KEY_1: "1", uinput.KEY_2: "2", uinput.KEY_3: "3", uinput.KEY_4: "4", uinput.KEY_5: "5", uinput.KEY_6: "6",
    uinput.KEY_7: "7", uinput.KEY_8: "8", uinput.KEY_9: "9", uinput.KEY_0: "0", uinput.KEY_MINUS: "-", uinput.KEY_EQUAL: "=",
    uinput.KEY_BACKSPACE: "Backspace", uinput.KEY_TAB: "Tab", uinput.KEY_Q: "Q", uinput.KEY_W: "W", uinput.KEY_E: "E", uinput.KEY_R: "R",
    uinput.KEY_T: "T", uinput.KEY_Y: "Y", uinput.KEY_U: "U", uinput.KEY_I: "I", uinput.KEY_O: "O", uinput.KEY_P: "P",
    uinput.KEY_LEFTBRACE: "[", uinput.KEY_RIGHTBRACE: "]", uinput.KEY_ENTER: "Enter", uinput.KEY_LEFTCTRL: "Ctrl_L", uinput.KEY_A: "A",
    uinput.KEY_S: "S", uinput.KEY_D: "D", uinput.KEY_F: "F", uinput.KEY_G: "G", uinput.KEY_H: "H", uinput.KEY_J: "J", uinput.KEY_K: "K",
    uinput.KEY_L: "L", uinput.KEY_SEMICOLON: ";", uinput.KEY_APOSTROPHE: "'", uinput.KEY_GRAVE: "`", uinput.KEY_LEFTSHIFT: "Shift_L",
    uinput.KEY_BACKSLASH: "\\", uinput.KEY_Z: "Z", uinput.KEY_X: "X", uinput.KEY_C: "C", uinput.KEY_V: "V", uinput.KEY_B: "B",
    uinput.KEY_N: "N", uinput.KEY_M: "M", uinput.KEY_COMMA: ",", uinput.KEY_DOT: ".", uinput.KEY_SLASH: "/",
    uinput.KEY_KPENTER: "Enter", uinput.KEY_LEFTALT: "Alt_L", uinput.KEY_RIGHTALT: "Alt_R", uinput.KEY_SPACE: "Space", uinput.KEY_CAPSLOCK: "CapsLock",
    uinput.KEY_SCROLLLOCK: "ScrollLock", uinput.KEY_PAUSE: "Pause", uinput.KEY_INSERT: "Insert", uinput.KEY_HOME: "Home",
    uinput.KEY_PAGEUP: "PageUp", uinput.KEY_END: "End", uinput.KEY_PAGEDOWN: "PageDown",
    uinput.KEY_RIGHT: "→", uinput.KEY_LEFT: "←", uinput.KEY_DOWN: "↓", uinput.KEY_UP: "↑", uinput.KEY_NUMLOCK: "NumLock",
    uinput.KEY_RIGHTCTRL: "Ctrl_R", uinput.KEY_LEFTMETA:"Super_L", uinput.KEY_RIGHTMETA:"Super_R"}

# Russian key mapping (ЙЦУКЕН layout)
key_mapping_ru = {
    # Added Esc, F keys, and Delete
    uinput.KEY_ESC: "Esc", uinput.KEY_F1: "F1", uinput.KEY_F2: "F2", uinput.KEY_F3: "F3", uinput.KEY_F4: "F4",
    uinput.KEY_F5: "F5", uinput.KEY_F6: "F6", uinput.KEY_F7: "F7", uinput.KEY_F8: "F8", uinput.KEY_F9: "F9",
    uinput.KEY_F10: "F10", uinput.KEY_F11: "F11", uinput.KEY_F12: "F12", uinput.KEY_DELETE: "Delete",

    uinput.KEY_1: "1", uinput.KEY_2: "2", uinput.KEY_3: "3", uinput.KEY_4: "4", uinput.KEY_5: "5", uinput.KEY_6: "6",
    uinput.KEY_7: "7", uinput.KEY_8: "8", uinput.KEY_9: "9", uinput.KEY_0: "0", uinput.KEY_MINUS: "-", uinput.KEY_EQUAL: "=",
    uinput.KEY_BACKSPACE: "Backspace", uinput.KEY_TAB: "Tab", uinput.KEY_Q: "Й", uinput.KEY_W: "Ц", uinput.KEY_E: "У", uinput.KEY_R: "К",
    uinput.KEY_T: "Е", uinput.KEY_Y: "Н", uinput.KEY_U: "Г", uinput.KEY_I: "Ш", uinput.KEY_O: "Щ", uinput.KEY_P: "З",
    uinput.KEY_LEFTBRACE: "Х", uinput.KEY_RIGHTBRACE: "Ъ", uinput.KEY_ENTER: "Enter", uinput.KEY_LEFTCTRL: "Ctrl_L", uinput.KEY_A: "Ф",
    uinput.KEY_S: "Ы", uinput.KEY_D: "В", uinput.KEY_F: "А", uinput.KEY_G: "П", uinput.KEY_H: "Р", uinput.KEY_J: "О", uinput.KEY_K: "Л",
    uinput.KEY_L: "Д", uinput.KEY_SEMICOLON: "Ж", uinput.KEY_APOSTROPHE: "Э", uinput.KEY_GRAVE: "Ё", uinput.KEY_LEFTSHIFT: "Shift_L",
    uinput.KEY_BACKSLASH: "\\", uinput.KEY_Z: "Я", uinput.KEY_X: "Ч", uinput.KEY_C: "С", uinput.KEY_V: "М", uinput.KEY_B: "И",
    uinput.KEY_N: "Т", uinput.KEY_M: "Ь", uinput.KEY_COMMA: "Б", uinput.KEY_DOT: "Ю", uinput.KEY_SLASH: ".",
    uinput.KEY_KPENTER: "Enter", uinput.KEY_LEFTALT: "Alt_L", uinput.KEY_RIGHTALT: "Alt_R", uinput.KEY_SPACE: "Space", uinput.KEY_CAPSLOCK: "CapsLock",
    uinput.KEY_SCROLLLOCK: "ScrollLock", uinput.KEY_PAUSE: "Pause", uinput.KEY_INSERT: "Insert", uinput.KEY_HOME: "Home",
    uinput.KEY_PAGEUP: "PageUp", uinput.KEY_END: "End", uinput.KEY_PAGEDOWN: "PageDown",
    uinput.KEY_RIGHT: "→", uinput.KEY_LEFT: "←", uinput.KEY_DOWN: "↓", uinput.KEY_UP: "↑", uinput.KEY_NUMLOCK: "NumLock",
    uinput.KEY_RIGHTCTRL: "Ctrl_R", uinput.KEY_LEFTMETA:"Super_L", uinput.KEY_RIGHTMETA:"Super_R"}


# Mappings for shifted characters/symbols for both layouts
shifted_mapping_en = {
    "`": "~", "1": "!", "2": "@", "3": "#", "4": "$", "5": "%", "6": "^", "7": "&", "8": "*", "9": "(", "0": ")",
    "-": "_", "=": "+", "[": "{", "]": "}", "\\": "|", ";": ":", "'": "\"", ",": "<", ".": ">", "/": "?"
}

shifted_mapping_ru = {
    "1": "!", "2": "\"", "3": "№", "4": ";", "5": "%", "6": ":", "7": "?", "8": "*", "9": "(", "0": ")",
    "-": "_", "=": "+", "Й": "Й", "Ц": "Ц", "У": "У", "К": "К", "Е": "Е", "Н": "Н", "Г": "Г", "Ш": "Ш", "Щ": "Щ", "З": "З",
    "Х": "Х", "Ъ": "Ъ", "Ф": "Ф", "Ы": "Ы", "В": "В", "А": "А", "П": "П", "Р": "Р", "О": "О", "Л": "Л", "Д": "Д",
    "Ж": "Ж", "Э": "Э", "Ё": "Ё", "\\": "/", "Я": "Я", "Ч": "Ч", "С": "С", "М": "М", "И": "И", "Т": "Т", "Ь": "Ь",
    "Б": "Б", "Ю": "Ю", ".": ","
}


class VirtualKeyboard(Gtk.Window):
    def __init__(self):
        super().__init__(title="Virtual Keyboard", name="toplevel")

        self.set_border_width(0)
        self.set_resizable(True)
        self.set_keep_above(True)
        self.set_modal(False)
        self.set_focus_on_map(False)
        self.set_can_focus(False)
        self.set_accept_focus(False)
        self.width=0
        self.height=0

        self.CONFIG_DIR = os.path.expanduser("~/.config/vboard")
        self.CONFIG_FILE = os.path.join(self.CONFIG_DIR, "settings.conf")
        self.config = configparser.ConfigParser()

        # Set fixed background color and text color
        self.bg_color = "245, 245, 220"  # Beige
        self.opacity="0.90"
        self.text_color="#1C1C1C" # Dark color for light background

        self.read_settings() # Still read opacity and size settings


        self.modifiers = {
            uinput.KEY_LEFTSHIFT: False,
            uinput.KEY_LEFTCTRL: False,
            uinput.KEY_RIGHTCTRL: False,
            uinput.KEY_LEFTALT: False,
            uinput.KEY_RIGHTALT: False,
            uinput.KEY_LEFTMETA: False,
            uinput.KEY_RIGHTMETA: False
        }
        # Removed the colors list as color customization is removed


        if (self.width!=0):
            self.set_default_size(self.width, self.height)

        self.header = Gtk.HeaderBar()
        self.header.set_show_close_button(True)
        self.buttons=[]
        self.row_buttons=[]
        # Removed color_combobox
        # Set the header bar as the titlebar of the window
        self.set_titlebar(self.header)
        self.create_settings()

        self.current_layout = "en" # Default layout is English
        self.key_mapping = key_mapping_en # Set initial key mapping
        self.shifted_mapping = shifted_mapping_en # Set initial shifted mapping

        self.grid = Gtk.Grid()  # Use Grid for layout
        # Set column and row spacing for better visual separation
        self.grid.set_column_spacing(3)
        self.grid.set_row_spacing(3)
        # Set columns to be homogeneous to distribute space
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)  # Allow rows to resize based on content
        self.grid.set_margin_start(3)
        self.grid.set_margin_end(3)
        self.grid.set_name("grid")
        self.add(self.grid)
        self.apply_css()

        # Initialize uinput device with all possible keys from both layouts
        # Ensure all keys from both mappings are included
        all_keys = list(set(list(key_mapping_en.keys()) + list(key_mapping_ru.keys())))
        self.device = uinput.Device(all_keys)


        self.draw_keyboard()


    def create_settings(self):
        self.create_button("☰", self.change_visibility,callbacks=1)
        self.create_button("+", self.change_opacity,True,2)
        self.create_button("-", self.change_opacity, False,2)
        self.create_button( f"{self.opacity}")
        # Removed color_combobox creation and connection

        # Add layout switch button
        self.layout_button = Gtk.Button(label="英／中") # Changed initial label
        self.layout_button.set_name("headbar-button")
        self.layout_button.connect("clicked", self.switch_layout)
        self.header.add(self.layout_button)
        self.buttons.append(self.layout_button)

        # Removed adding colors to combobox


    def on_resize(self, widget, event):
        self.width, self.height = self.get_size()  # Get the current size after resize


    def create_button(self, label_="", callback=None, callback2=None, callbacks=0):
        button= Gtk.Button(label=label_)
        button.set_name("headbar-button")
        if callbacks==1:
            button.connect("clicked", callback)
        elif callbacks==2:
            button.connect("clicked", callback, callback2)

        if label_==self.opacity:
            self.opacity_btn=button
            self.opacity_btn.set_tooltip_text("opacity")

        self.header.add(button)
        self.buttons.append(button)

    def change_visibility(self, widget=None):
        for button in self.buttons:
            if button.get_label()!="☰":
                button.set_visible(not button.get_visible())
        # Removed color_combobox visibility toggle
        self.layout_button.set_visible(not self.layout_button.get_visible())


    # Removed change_color method


    def change_opacity(self,widget, boolean):
        if (boolean):
            self.opacity = str(round(min(1.0, float(self.opacity) + 0.01),2))
        else:
            self.opacity = str(round(max(0.0, float(self.opacity) - 0.01),2))
        self.opacity_btn.set_label(f"{self.opacity}")
        self.apply_css()

    def apply_css (self):
        provider = Gtk.CssProvider()


        css = f"""
        headerbar {{
            background-color: rgba({self.bg_color}, {self.opacity});
            border: 0px;

        }}

        headerbar button{{
            min-width: 40px;
            padding: 0px;
            border: 0px;


        }}

        headerbar button label{{
        color: {self.text_color};

        }}

        #headbar-button {{
            background-image: none;
        }}

        #toplevel {{
            background-color: rgba({self.bg_color}, {self.opacity});




        }}

        #grid button label{{
            color: {self.text_color};


        }}

        #grid button {{
                    border: 1px solid rgba(85, 85, 85, 0.7) ;
                    background-image: none;

                }}

        button {{
            background-color: transparent;
            color:{self.text_color};

        }}

       #grid button:hover {{
            border: 1px solid #00CACB;
        }}

       tooltip {{
            color: white;
            padding: 5px;
        }}

        """


        try:
            provider.load_from_data(css.encode("utf-8"))
        except GLib.GError as e:
            print(f"CSS Error: {e.message}")
        Gtk.StyleContext.add_provider_for_screen(self.get_screen(), provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def draw_keyboard(self):
        # Clear existing buttons from the grid
        for child in self.grid.get_children():
            self.grid.remove(child)
        self.row_buttons = [] # Clear the list of row buttons

        # Define rows for keys based on the current layout for ortholinear layout
        # Using None as a placeholder for empty grid cells to maintain grid structure
        if self.current_layout == "en":
            rows = [
                # Row 0: Esc, F keys, Delete
                ["Esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Delete"], # 14 keys
                # Row 1: Numbers, Backspace
                ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "Backspace" ], # 13 keys + Backspace
                # Row 2: QWERTY
                ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"], # 14 keys
                # Row 3: ASDF
                ["CapsLock", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "Enter"], # 13 keys + Enter
                # Row 4: ZXC, Up/Down Arrows (Right Shift removed)
                ["Shift_L", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "↑", "↓"], # 12 keys + 2 arrows
                # Row 5: Modifiers, Left/Right Arrows (Right Shift and Up/Down removed)
                ["Ctrl_L","Super_L", "Alt_L", "Space", "Alt_R", "Super_R", "Ctrl_R", "←", "→"] # 9 keys + Space
            ]
        elif self.current_layout == "ru":
             rows = [
                # Row 0: Esc, F keys, Delete
                ["Esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Delete"], # 14 keys
                # Row 1: Numbers, Backspace
                ["Ё", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "Backspace" ], # 13 keys + Backspace
                # Row 2: ЙЦУКЕН
                ["Tab", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ", "\\"], # 14 keys
                # Row 3: ФЫВАПР
                ["CapsLock", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э", "Enter"], # 13 keys + Enter
                # Row 4: ЯЧСМИТ, Up/Down Arrows (Right Shift removed)
                ["Shift_L", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю", ".", "↑", "↓"], # 12 keys + 2 arrows
                # Row 5: Modifiers, Left/Right Arrows (Right Shift and Up/Down removed)
                ["Ctrl_L","Super_L", "Alt_L", "Space", "Alt_R", "Super_R", "Ctrl_R", "←", "→"] # 9 keys + Space
            ]


        # Create each row and add it to the grid
        for row_index, keys in enumerate(rows):
            self.create_row(self.grid, row_index, keys)

        self.grid.show_all() # Show the new buttons

    def create_row(self, grid, row_index, keys):
        col = 0  # Start from the first column
        # Define integer column spans for keys to achieve ortholinear look
        # These spans are relative and will be distributed by the grid
        span_map = {
            "Esc": 4, "F1": 4, "F2": 4, "F3": 4, "F4": 4, "F5": 4, "F6": 4, "F7": 4, "F8": 4, "F9": 4, "F10": 4, "F11": 4, "F12": 4,
            "Delete": 8, # Increased Delete span to fill space in row 0
            "Backspace": 8, # Backspace span 8 (2x standard)
            "Tab": 6, # 1.5x standard
            "CapsLock": 7, # 1.75x standard
            "Enter": 9, # 2.25x standard
            "Shift_L": 10, # Adjusted to fit row 4
            "Ctrl_L": 5, "Ctrl_R": 5, "Alt_L": 5, "Alt_R": 5, "Super_L": 5, "Super_R": 5, # 1.25x standard
            "Space": 20, # Adjusted to fit row 5
            "↑": 5, "↓": 5, "←": 5, "→": 5, # Arrows span 5 (1.25x standard to align better)
            "\\": 5, # Slightly increased \ span to help fill space (adjusted back to 5)
        }
        # Default span for standard keys (letters, numbers, symbols)
        default_span = 4


        for key_label in keys:
            # Get span from span_map, default to default_span
            width_span = span_map.get(key_label, default_span)

            # Handle modifier labels (remove _L/_R)
            if key_label in ("Shift_L", "Alt_L", "Alt_R", "Ctrl_L", "Ctrl_R", "Super_L", "Super_R"):
                 button = Gtk.Button(label=key_label[:-2])
            else:
                 button = Gtk.Button(label=key_label)


            key_event = None
            # Find the uinput key event for the current label in the current layout
            if self.current_layout == "en":
                key_event = next((key for key, label in key_mapping_en.items() if label == key_label), None)
            elif self.current_layout == "ru":
                 key_event = next((key for key, label in key_mapping_ru.items() if label == key_label), None)

            if key_event:
                button.connect("clicked", self.on_button_click, key_event)
                self.row_buttons.append(button)

                # Attach button to the grid with calculated width span
                grid.attach(button, col, row_index, width_span, 1)
                col += width_span  # Increment column based on the button's width span


    def switch_layout(self, widget):
        # Switch between English and Russian layouts
        if self.current_layout == "en":
            self.current_layout = "ru"
            self.key_mapping = key_mapping_ru
            self.shifted_mapping = shifted_mapping_ru
            self.layout_button.set_label("俄") # Changed label to Russian
        else:
            self.current_layout = "en"
            self.key_mapping = key_mapping_en
            self.shifted_mapping = shifted_mapping_en
            self.layout_button.set_label("英／中") # Changed label to English/Chinese

        # Redraw the keyboard with the new layout
        self.draw_keyboard()

    def update_label(self, show_symbols):
        # Update button labels based on shift state and current layout
        # This logic needs to be robust to find the corresponding button for a given key label
        # regardless of its position in the row_buttons list which can change based on layout.
        # A better approach is to store button references mapped to their key events or original labels.

        # For simplicity in this correction, we'll iterate through all buttons and update if the label matches
        # a key that has a shifted counterpart in the current layout's shifted mapping.
        current_shifted_mapping = self.shifted_mapping
        current_key_mapping = self.key_mapping # Need this to find the unshifted label

        for button in self.row_buttons:
            current_label = button.get_label()
            # Find the key event for the current label in the current key mapping
            key_event_for_label = None
            # Check both original key mapping and shifted mapping to find the key event
            for key, label in current_key_mapping.items():
                if label == current_label:
                    key_event_for_label = key
                    break
            if not key_event_for_label:
                 for key, label in current_shifted_mapping.items():
                      if label == current_label:
                           # Need to find the original unshifted label for this shifted label
                           original_unshifted_label = None
                           for unshifted_key, unshifted_label_val in current_key_mapping.items():
                               if unshifted_label_val == key: # Check if the key from shifted_mapping exists in key_mapping
                                    original_unshifted_label = unshifted_label_val
                                    key_event_for_label = unshifted_key # Use the key event of the unshifted key
                                    break
                           if original_unshifted_label:
                                break # Found the key event for the shifted label


            if show_symbols:
                # If shift is active, try to find the shifted character
                shifted_label = current_shifted_mapping.get(current_label)
                if shifted_label:
                    button.set_label(shifted_label)
            else:
                # If shift is not active, try to find the unshifted character
                # We need to find the original unshifted label from the shifted mapping
                unshifted_label = None
                for original, shifted in current_shifted_mapping.items():
                    if shifted == current_label:
                        unshifted_label = original
                        break # Found the original unshifted label

                if unshifted_label:
                     button.set_label(unshifted_label)
                # If no unshifted label found in the shifted map, it means the key doesn't change with shift,
                # or it's a modifier/special key, so keep the current label.


    def on_button_click(self, widget, key_event):
        # If the key event is one of the modifiers, update its state and return.
        if key_event in self.modifiers:
            self.modifiers[key_event] = not self.modifiers[key_event]
            # Toggle shift state
            if key_event in (uinput.KEY_LEFTSHIFT, uinput.KEY_RIGHTSHIFT): # Still check for RIGHTSHIFT in modifiers
                 show_symbols = self.modifiers[uinput.KEY_LEFTSHIFT] or self.modifiers.get(uinput.KEY_RIGHTSHIFT, False) # Safely check for RIGHTSHIFT
                 self.update_label(show_symbols)
            return

        # For a normal key, press any active modifiers.
        for mod_key, active in self.modifiers.items():
            if active:
                self.device.emit(mod_key, 1)

        # Emit the normal key press.
        self.device.emit(key_event, 1)
        #time.sleep(0.05)
        self.device.emit(key_event, 0)

        # Release the modifiers that were active and reset their state
        for mod_key, active in self.modifiers.items():
            if active:
                self.device.emit(mod_key, 0)
                self.modifiers[mod_key] = False

        # After releasing modifiers, update labels to show unshifted state
        self.update_label(False)


    def read_settings(self):
        # Ensure the config directory exists
        try:
            os.makedirs(self.CONFIG_DIR, exist_ok=True)
        except PermissionError:
            print("Warning: No permission to create the config directory. Proceeding without it.")

        try:
            if os.path.exists(self.CONFIG_FILE):
                self.config.read(self.CONFIG_FILE)
                # Removed reading bg_color and text_color from settings
                self.opacity = self.config.get("DEFAULT", "opacity" )
                self.width=self.config.getint("DEFAULT", "width" , fallback=0)
                self.height=self.config.getint("DEFAULT", "height", fallback=0)
                # print(f"rgba: {self.bg_color}, {self.opacity}") # Removed this print statement

        except configparser.Error as e:
            print(f"Warning: Could not read config file ({e}). Using default values.")



    def save_settings(self):
        # Only save opacity, width, and height
        self.config["DEFAULT"] = {"opacity": self.opacity, "width": self.width, "height": self.height}

        try:
            with open(self.CONFIG_FILE, "w") as configfile:
                self.config.write(configfile)

        except (configparser.Error, IOError) as e:
            print(f"Warning: Could not write to config file ({e}). Changes will not be saved.")


if __name__ == "__main__":
    # --- Start of existing application logic (without lock) ---
    win = VirtualKeyboard()
    win.connect("destroy", Gtk.main_quit)
    win.connect("destroy", lambda w: win.save_settings())
    win.show_all()
    win.connect("configure-event", win.on_resize)
    win.change_visibility()
    Gtk.main()
    # --- End of existing application logic (without lock) ---
