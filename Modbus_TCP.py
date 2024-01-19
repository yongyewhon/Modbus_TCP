import cv2
import time
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils

#Modbus_TCP_Address = "192.168.1.200" #Waveshare
#Modbus_TCP_Port = 502
#Modbus_TCP_Delay = 0.03
Modbus_TCP_Address = "169.254.173.207" #HF5111S
Modbus_TCP_Port = 503
Modbus_TCP_Delay = 0
Modbus_Device = 10
Modbus_TCP_Debug = True
#c = ModbusClient(host='localhost', port=Modbus_TCP_Port, unit_id=1, timeout=30.0, debug=False, auto_open=True, auto_close=False)
node01 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=1, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
node02 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=2, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
node03 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=3, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
node04 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=4, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
node05 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=5, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
node06 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=6, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
node07 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=7, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
node08 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=8, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
node09 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=9, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
node10 = ModbusClient(host=Modbus_TCP_Address, port=Modbus_TCP_Port, unit_id=10, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
value = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

def Modbus_TCP_Read():
    global value
    if Modbus_TCP_Debug is True: t1 = cv2.getTickCount()
    for i in range(1, Modbus_Device+1):
        # read 2 registers at address 3, store result in regs list (decimal and measure value)
        regs_list = None
        if i == 1: regs_list = node01.read_holding_registers(3, 2)
        elif i == 2: regs_list = node02.read_holding_registers(3, 2)
        elif i == 3: regs_list = node03.read_holding_registers(3, 2)
        elif i == 4: regs_list = node04.read_holding_registers(3, 2)
        elif i == 5: regs_list = node05.read_holding_registers(3, 2)
        elif i == 6: regs_list = node06.read_holding_registers(3, 2)
        elif i == 7: regs_list = node07.read_holding_registers(3, 2)
        elif i == 8: regs_list = node08.read_holding_registers(3, 2)
        elif i == 9: regs_list = node09.read_holding_registers(3, 2)
        elif i == 10: regs_list = node10.read_holding_registers(3, 2)
        #print(i, regs_list, type(regs_list))
        # if success display registers
        if str(type(regs_list)) == "<class 'NoneType'>": print(f"Error read from node{i} registers") 
        elif len(regs_list) == 2:
            value[i] = float(utils.get_2comp(regs_list[1], 16)) / (10**regs_list[0])
            #print(regs_list, type(regs_list))
            print(f"node0{i}= {value[i]}")
        else: print(f"Invalid read from node{i} registers")
        if Modbus_TCP_Delay > 0: time.sleep(Modbus_TCP_Delay)
    if Modbus_TCP_Debug is True: 
        t2 = cv2.getTickCount()
        print("Time taken = {:.4f} seconds". format((t2-t1) / cv2.getTickFrequency()))
    return value

def Modbus_TCP_Write():
    reg_value = 2
    write_status = node01.write_single_register(3, reg_value)
    if write_status is False:
        print("Error write to register")

while True:
    Modbus_TCP_Read()
    time.sleep(0.5)
