# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" CS:GO-Clicker """


__version__ = "1.0"
__author__ = "github.com/klaus-moser"


import pyautogui
import sys
import keyboard
import time


AUTO_STOP = 600  # Auto stopt ime in seconds
OFFSET = 77  # offset from the center


def main():
    """
    Auto clicker to start during CS:CO. Clicks always in the middle.
    """

    print("*** Start CS:GO Auto-clicker. ***\n")

    current_time = time.time()  # Get the current time
    end_time = current_time + AUTO_STOP  # time 10 minutes in the future
    screen_width, screen_height = pyautogui.size()  # Get the resolution of the screen

    print("Screen Resolution:", screen_width, "x", screen_height)
    print(f"AUTO_STOP after {AUTO_STOP} seconds.\n")

    center_x, center_y = screen_width / 2, (screen_height / 2) - OFFSET  # Calculate the center of the screen

    try:
        i = 1
        while True:
            print(f"\r{i}th Click! Press 'F11' to stop...", end='', flush=True)
            
            pyautogui.moveTo(center_x, center_y)  # move the mouse to the center of the screen
            pyautogui.click()  # click
            if keyboard.is_pressed('f11') or time.time() >= end_time:  # F11 for break
                break
            i += 1

    except Exception as e:
        sys.exit(e)

    finally:
        print("\n\n*** Exiting program. ***")


if __name__ == '__main__':
    main()
