# Import all modules
import Interface as itf

window, tab_frame = itf.main_window()

tab_massa = itf.massa_tab(tab_frame)
tab_massa.grid()

tab_temp = itf.temp_tab(tab_frame)
tab_temp.grid()

tab_dec = itf.dec_tab(tab_frame)
tab_dec.grid()

tab_byte = itf.byte_tab(tab_frame)
tab_byte.grid()

tab_time = itf.time_tab(tab_frame)
tab_time.grid()

tab_panjang = itf.length_tab(tab_frame)
tab_panjang.grid()


tab_frame.add(tab_massa, text='Massa')
tab_frame.add(tab_temp, text='Suhu')
tab_frame.add(tab_dec, text='Decimal')
tab_frame.add(tab_byte, text='Data')
tab_frame.add(tab_time, text='Waktu')
tab_frame.add(tab_panjang, text='Panjang')

itf.window_program(window)
