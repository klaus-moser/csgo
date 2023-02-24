# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" CS:GO-Clicker """

__version__ = "1.1"
__author__ = "github.com/klaus-moser"

import pyautogui
import sys
import keyboard


OFFSET_PERCENT = 0.08333  # offset percentage of pixel of the 'ACCEPT' button


def main():
    """
    Auto clicker to start during CS:CO. Clicks always in the middle.
    """

    print("*** Start CS:GO Auto-clicker. ***\n")

    screen_width, screen_height = pyautogui.size()  # Get the resolution of the screen

    print(f"Screen Resolution:\t{screen_width} x {screen_height}")
    print(f"Screen Center:\t\t{(int(screen_width/2), int(screen_height/2))}")
    print(f"Offset:\t\t\t\t{int(screen_height * OFFSET_PERCENT)}px")

    center_x, center_y = screen_width / 2, (screen_height / 2) - int(screen_height * OFFSET_PERCENT)  # calculation

    print(f"Button center:\t\t{(int(center_x), int(center_y))}\n")

    try:
        i = 1
        while True:

            if i % 2 == 0:
                pyautogui.moveTo(center_x + 5, center_y)  # move the mouse + 5px
            else:
                pyautogui.moveTo(center_x - 5, center_y)  # move the mouse - 5px

            pyautogui.click()  # click

            print(f"\r{i}th Click! Press 'F11' to stop...", end='', flush=True)

            if keyboard.is_pressed('f11'):  # 'F11' to break loop
                break
            i += 1

    except Exception as e:
        sys.exit(e)

    finally:
        print("\n\n*** Exiting program. ***")


if __name__ == '__main__':
    main()
