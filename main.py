import algorithm_FIFO_replace_pages as algorithm_fifo
import algorithm_LRU_replace_pages as algorithm_lru
import create_data as d
import calculations as calc

available_frames = [3, 5, 7]

fifo = algorithm_fifo.algorithm_FIFO()
lru = algorithm_lru.algorithm_LRU()
data = d.Data()
calculations = calc.Calculations()

data.create_random_data()

fifo.save_to_result_file()
lru.save_to_result_file()

calculations.save_all_calculations()