import visa
import matplotlib
import matplotlib.pyplot as plt



rm = visa.ResourceManager()
# print(rm.list_resources())
 
inst = rm.open_resource('TCPIP0::ifm118.ifmpan.poznan.pl::hpib7,16::INSTR')

print(inst.query("*IDN?"))

try:

   


    # print(inst.query("CALCulate1:PARameter:CATalog?"))
    # print(inst.query("DISPlay:CATalog?"))
    # print(inst.query("DISPlay:WINDow1:CATalog?"))

    inst.write("CALCulate:PARameter:SELect 'CH1_S11_1'")


    inst.write("SENSe1:SWEep:POIN 10")


    # 'Turn continuous sweep off
    inst.write("INITiate:CONTinuous OFF")

    # 'Take a sweep
    inst.write("INITiate:IMMediate;*wai")
 

    print(inst.query("SENSe1:SWEep:POIN?"))

    complex_values_str=inst.query("CALCulate:DATA? SDATA") #'Corrected, Complex Meas
    values=inst.query("CALCulate:DATA? FDATA")

    dane=[float(i) for i in values[:-1].split(',')]



    fig, ax = plt.subplots()
    ax.plot(dane)

    ax.set(xlabel='points', ylabel='Signal (a.u.)',
        title='About as simple as it gets, folks')
    ax.grid()

    # # fig.savefig("test.png")
    plt.show()


except NameError as err:
    print(err, '--> our error message')

