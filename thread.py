from wmControl import wlmConst
from wmControl import control
from wmControl import wlmData


class callback:
    version = 0
    put = None

    # Prints all measured frequencys of one WM
    # Unit: THz
    def frequencysProcEx(self, Ver, Mode, IntVal, DblVal, Res1):
        if (Ver == self.version and Mode == wlmConst.cmiWavelength1):
            print("Time:{}, WM:{}, Channel:1, Wavelength:{:.8f}".format(IntVal, Ver, 299792.458/DblVal))
        if (Ver == self.version and Mode == wlmConst.cmiWavelength2):
            print("Time:{}, WM:{}, Channel:2, Wavelength:{:.8f}".format(IntVal, Ver, 299792.458/DblVal))
        if (Ver == self.version and Mode == wlmConst.cmiWavelength3):
            print("Time:{}, WM:{}, Channel:3, Wavelength:{:.8f}".format(IntVal, Ver, 299792.458/DblVal))
        if (Ver == self.version and Mode == wlmConst.cmiWavelength4):
            print("Time:{}, WM:{}, Channel:4, Wavelength:{:.8f}".format(IntVal, Ver, 299792.458/DblVal))
        if (Ver == self.version and Mode == wlmConst.cmiWavelength5):
            print("Time:{}, WM:{}, Channel:5, Wavelength:{:.8f}".format(IntVal, Ver, 299792.458/DblVal))
        if (Ver == self.version and Mode == wlmConst.cmiWavelength6):
            print("Time:{}, WM:{}, Channel:6, Wavelength:{:.8f}".format(IntVal, Ver, 299792.458/DblVal))
        if (Ver == self.version and Mode == wlmConst.cmiWavelength7):
            print("Time:{}, WM:{}, Channel:7, Wavelength:{:.8f}".format(IntVal, Ver, 299792.458/DblVal))
        if (Ver == self.version and Mode == wlmConst.cmiWavelength8):
            print("Time:{}, WM:{}, Channel:8, Wavelength:{:.8f}".format(IntVal, Ver, 299792.458/DblVal))

    # Prints all measured wavelengths one WM
    # Unit: nm
    def wavelengthsProcEx(self, Ver, Mode, IntVal, DblVal, Res1):
        if (Ver == self.version and Mode == wlmConst.cmiWavelength1):
            print("Time:{}, WM:{}, Channel:1, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            #self.put([IntVal, Ver, DblVal])
        if (Ver == self.version and Mode == wlmConst.cmiWavelength2):
            print("Time:{}, WM:{}, Channel:2, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            #self.put([IntVal, Ver, DblVal])
        if (Ver == self.version and Mode == wlmConst.cmiWavelength3):
            print("Time:{}, WM:{}, Channel:3, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            #self.put([IntVal, Ver, DblVal])
        if (Ver == self.version and Mode == wlmConst.cmiWavelength4):
            print("Time:{}, WM:{}, Channel:4, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            #self.put([IntVal, Ver, DblVal])
        if (Ver == self.version and Mode == wlmConst.cmiWavelength5):
            print("Time:{}, WM:{}, Channel:5, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            #self.put([IntVal, Ver, DblVal])
        if (Ver == self.version and Mode == wlmConst.cmiWavelength6):
            print("Time:{}, WM:{}, Channel:6, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            #self.put([IntVal, Ver, DblVal])
        if (Ver == self.version and Mode == wlmConst.cmiWavelength7):
            print("Time:{}, WM:{}, Channel:7, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            #self.put([IntVal, Ver, DblVal])
        if (Ver == self.version and Mode == wlmConst.cmiWavelength8):
            print("Time:{}, WM:{}, Channel:8, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            #self.put([IntVal, Ver, DblVal])


    # Prints all measured wavelengths of all WMs connected to the control-PC
    # Unit: nm
    def allwavelengthsProcEx(self, Ver, Mode, IntVal, DblVal, Res1):
        if (Mode == wlmConst.cmiWavelength1):
            #print("Time:{}, WM:{}, Channel:1, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            self.put([IntVal, Ver, DblVal])
        if (Mode == wlmConst.cmiWavelength2):
            #print("Time:{}, WM:{}, Channel:2, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            self.put([IntVal, Ver, DblVal])
        if (Mode == wlmConst.cmiWavelength3):
            #print("Time:{}, WM:{}, Channel:3, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            self.put([IntVal, Ver, DblVal])
        if (Mode == wlmConst.cmiWavelength4):
            #print("Time:{}, WM:{}, Channel:4, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            self.put([IntVal, Ver, DblVal])
        if (Mode == wlmConst.cmiWavelength5):
            #print("Time:{}, WM:{}, Channel:5, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            self.put([IntVal, Ver, DblVal])
        if (Mode == wlmConst.cmiWavelength6):
            #print("Time:{}, WM:{}, Channel:6, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            self.put([IntVal, Ver, DblVal])
        if (Mode == wlmConst.cmiWavelength7):
            #print("Time:{}, WM:{}, Channel:7, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            self.put([IntVal, Ver, DblVal])
        if (Mode == wlmConst.cmiWavelength8):
            #print("Time:{}, WM:{}, Channel:8, Wavelength:{:.8f}".format(IntVal, Ver, DblVal))
            self.put([IntVal, Ver, DblVal])


    def getSwitchedChannel(self, Ver, Mode, IntVal, DblVal, Res1):
        if (Ver == self.version and Mode == wlmConst.cmiSwitcherChannel):
            print("Time:{}, WM:{}, Active Channel: {}, Getter-state:{}".format(Res1, Ver, IntVal, DblVal), "Wavelength:{:.8f}".format(wlmData.dll.GetWavelengthNum(IntVal, 0)))

    def __init__(self, ver, wavemeter):
        self.version = ver
        self.put = wavemeter.putBfr