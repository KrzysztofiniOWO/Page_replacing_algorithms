import statistics as stat


class Calculations:

    def __init__(self):
        """Initialize class"""

    def count_average_of_missing_pages_FIFO(self, frame):
        """Count average of missing files FIFO"""

        list_of_calculations = []
        sum_of_all = 0

        with open(f"FIFO_results/{frame}.txt", "r") as f:
            for element in f.readlines():
                list_of_calculations.append(int(element.strip()))

            for calculation in list_of_calculations:
                sum_of_all = sum_of_all + calculation

            f.close()

            return sum_of_all / 50

    def count_average_of_missing_pages_LRU(self, frame):
        """Count average of missing files LRU"""

        list_of_calculations = []
        sum_of_all = 0

        with open(f"LRU_results/{frame}.txt", "r") as f:
            for element in f.readlines():
                list_of_calculations.append(int(element.strip()))

            for calculation in list_of_calculations:
                sum_of_all = sum_of_all + calculation

            f.close()

            return sum_of_all / 50

    def count_standard_deviation_FIFO(self, frame):
        """Count standard deviation of missing files FIFO"""

        list_of_calculations = []

        with open(f"FIFO_results/{frame}.txt", "r") as f:
            for element in f.readlines():
                list_of_calculations.append(int(element.strip()))

            f.close()

            return stat.stdev(list_of_calculations)


    def count_standard_deviation_LRU(self, frame):
        """Count standard deviation of missing files LRU"""

        list_of_calculations = []

        with open(f"FIFO_results/{frame}.txt", "r") as f:
            for element in f.readlines():
                list_of_calculations.append(int(element.strip()))

            f.close()

            return stat.stdev(list_of_calculations)

    def save_all_calculations(self):
        """Save all calculations to a file"""

        available_frames = [3, 5, 7]

        for frame in available_frames:
            with open("calculations.txt", "w") as f:
                f.write(f"Average of missing pages FIFO frame: {frame} - {self.count_average_of_missing_pages_FIFO(frame)}\n")
                f.write(f"Average of missing pages LRU frame: {frame} - {self.count_average_of_missing_pages_FIFO(frame)}\n")
                f.write(f"Standard deviation of missing pages FIFO frame: {frame} - {self.count_standard_deviation_FIFO(frame)}\n")
                f.write(f"Standard deviation of missing pages LRU frame: {frame} - {self.count_standard_deviation_LRU(frame)}\n")
                f.close()
