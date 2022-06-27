import os


if __name__ == '__main__':
    # generate new code from .ui file into control_gui_update.py file
    os.system("python3 -m PyQt6.uic.pyuic controlboard.ui -o controlboard_gui_update.py")

    # open controlboard_gui_update.py file & read
    update_file = open('controlboard_gui_update.py')
    u_lines = update_file.readlines()
    # close file
    update_file.close()
    # boolean and list to store part to be copied
    u_copy = False
    code_from_update = []
    # loop through each line
    for u_line in u_lines:
        # end copying if this is seen
        if u_line.startswith("        self.retranslateUi(mainWindow)"):
            u_copy = False
        # copy
        if u_copy:
            code_from_update.append(u_line)
        # start copying if this is seen
        if u_line.startswith("    def setupUi(self, mainWindow):"):
            u_copy = True

    # open controlboard_gui.py file & read
    gui_file = open('controlboard_gui.py')
    g_lines = gui_file.readlines()
    # close file
    gui_file.close()
    # boolean and list to store the result code
    g_copy = True
    full_code = []
    for g_line in g_lines:
        # start copying
        if g_line.startswith("        # end of generated code from updates"):
            g_copy = True
        if g_copy:
            full_code.append(g_line)
        # stop copying
        if g_line.startswith("        # start generated code from updates"):
            g_copy = False
            full_code.append(code_from_update)

    # write full code to file
    gui_file = open('controlboard_gui.py', 'w')

    for line in full_code:
        new_contents = "".join(line)
        # write contents to file
        gui_file.write(new_contents)

    gui_file.close()
